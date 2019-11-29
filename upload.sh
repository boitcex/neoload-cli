#!/bin/bash

version_id=$(cat ./setup.py | grep -oE "(?:version=')(.*?)(?:')")
version_id=$(echo "${version_id/version=/}")
version_id=$(echo "${version_id//\'/}")

if [ -z "$version_id"]; then
    echo "No version found"
    exit 1
fi

#rm -rf dist/*
python setup.py sdist bdist_wheel
if [ "$?" -ne "0" ]; then
    echo "Packaging to wheel step failed"
    exit 2
fi
twine check dist/*
if [ "$?" -ne "0" ]; then
  echo "Checks on wheel failed"
  exit 3
fi
twine upload dist/*$version_id*
if [ "$?" -ne "0" ]; then
  echo "Twine upload failed"
  exit 4
fi
