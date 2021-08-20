import os
import tempfile
import zipfile

import logging
from gitignore_parser import parse_gitignore,rule_from_pattern

from neoload_cli_lib import rest_crud, tools, cli_exception
import shutil
import time

from pathlib import Path

intrinsic_ignore_spec = """
/recorded-requests/
/recorded-responses/
/recorded-screenshots/
.git/
.svn/
/results/
/comparative-summary/
/reports/
recorded-artifacts/
.bak
.bak.old
.DS_Store
"""

def is_not_to_be_included(path: str, intrinsic_ignore_matcher, nl_ignore_matcher):
    if intrinsic_ignore_matcher(path):
        logging.debug("intrinsic ignored: '" + path + "'")
        return True
    if nl_ignore_matcher is not None and nl_ignore_matcher(path):
        logging.debug(".nlignore'd: '" + path + "'")
        return True
    return False

def get_intrinsic_ignore_matcher(path):
    return parse_gitignore_string(intrinsic_ignore_spec, path)

def zip_dir(path,save):

    # validate save parameter, if provided, is a zip
    if save is not None:
        save = os.path.abspath(save)
        if not save.endswith(".zip"):
            raise cli_exception.CliException('If you specify where to save the zip file, it must end with .zip')

    # find and load .nlignore
    ignore_file = os.path.join(path, '.nlignore')
    nl_ignore_matcher = parse_gitignore(ignore_file) if os.path.exists(ignore_file) else None
    intrinsic_ignore_matcher = get_intrinsic_ignore_matcher(path)

    # always to work in a separate file, if save is provided, or otherwise
    temp_zip = tempfile.NamedTemporaryFile('w+b',delete=False)
    ziph = zipfile.ZipFile(temp_zip, 'x', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if not is_not_to_be_included(file_path, intrinsic_ignore_matcher, nl_ignore_matcher):
                ziph.write(file_path, file_path.replace(str(path), ''))
    ziph.close()

    # by default we return the temp file
    file_stream = temp_zip
    logging.debug(type(temp_zip))

    # if save file specified, copy temp to the specified save file
    if save is not None:
        # only delete the specified save if temp was created
        temp_zip.close()
        shutil.move(temp_zip.name, save)
        # return an open file stream to the new file specified by save
        file_stream = open(save, 'rb')

    # always ensure that stream starts at beginning
    file_stream.seek(0)

    return file_stream


def upload_project(path, endpoint, save=None):
    filename = os.path.basename(path)
    if str(path).endswith(('.zip', '.yaml', '.yml')):
        file = open(path, "b+r")
    else:
        filename += '.zip'
        file = zip_dir(path,save)

    display_project(rest_crud.post_binary_files_storage(endpoint, file, filename))

def display_project(res):
    if 299 > res.status_code > 199:
        tools.print_json(res.json())
    else:
        print(res.text)
        raise cli_exception.CliException("Error during get meta data code: " + res.status_code)


def parse_gitignore_string(spec_string, base_dir):
    rules = []
    ignore_lines = spec_string.split("\n")
    counter = 0
    for line in ignore_lines:
        counter += 1
        line = line.rstrip('\n').rstrip('\r')
        rule = rule_from_pattern(line, base_path=Path(base_dir).resolve(),
                                 source=(spec_string, counter))
        if rule:
            logging.debug(line)
            rules.append(rule)

    if not any(r.negation for r in rules):
        return lambda file_path: any(r.match(file_path) for r in rules)
    else:
        # We have negation rules. We can't use a simple "any" to evaluate them.
        # Later rules override earlier rules.
        return lambda file_path: handle_negation(file_path, rules)
