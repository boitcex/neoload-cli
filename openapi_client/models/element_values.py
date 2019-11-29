# coding: utf-8

"""
    NeoLoad API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ElementValues(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'count': 'int',
        'element_per_second': 'float',
        'min_duration': 'int',
        'max_duration': 'int',
        'sum_duration': 'int',
        'avg_duration': 'float',
        'min_ttfb': 'int',
        'max_ttfb': 'int',
        'sum_ttfb': 'int',
        'avg_ttfb': 'float',
        'sum_downloaded_bytes': 'int',
        'downloaded_bytes_per_second': 'float',
        'success_count': 'int',
        'success_per_second': 'float',
        'success_rate': 'float',
        'failure_count': 'int',
        'failure_per_second': 'float',
        'failure_rate': 'float',
        'percentile50': 'float',
        'percentile90': 'float',
        'percentile95': 'float',
        'percentile99': 'float'
    }

    attribute_map = {
        'count': 'count',
        'element_per_second': 'elementPerSecond',
        'min_duration': 'minDuration',
        'max_duration': 'maxDuration',
        'sum_duration': 'sumDuration',
        'avg_duration': 'avgDuration',
        'min_ttfb': 'minTTFB',
        'max_ttfb': 'maxTTFB',
        'sum_ttfb': 'sumTTFB',
        'avg_ttfb': 'avgTTFB',
        'sum_downloaded_bytes': 'sumDownloadedBytes',
        'downloaded_bytes_per_second': 'downloadedBytesPerSecond',
        'success_count': 'successCount',
        'success_per_second': 'successPerSecond',
        'success_rate': 'successRate',
        'failure_count': 'failureCount',
        'failure_per_second': 'failurePerSecond',
        'failure_rate': 'failureRate',
        'percentile50': 'percentile50',
        'percentile90': 'percentile90',
        'percentile95': 'percentile95',
        'percentile99': 'percentile99'
    }

    def __init__(self, count=None, element_per_second=None, min_duration=None, max_duration=None, sum_duration=None, avg_duration=None, min_ttfb=None, max_ttfb=None, sum_ttfb=None, avg_ttfb=None, sum_downloaded_bytes=None, downloaded_bytes_per_second=None, success_count=None, success_per_second=None, success_rate=None, failure_count=None, failure_per_second=None, failure_rate=None, percentile50=None, percentile90=None, percentile95=None, percentile99=None, local_vars_configuration=None):  # noqa: E501
        """ElementValues - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._count = None
        self._element_per_second = None
        self._min_duration = None
        self._max_duration = None
        self._sum_duration = None
        self._avg_duration = None
        self._min_ttfb = None
        self._max_ttfb = None
        self._sum_ttfb = None
        self._avg_ttfb = None
        self._sum_downloaded_bytes = None
        self._downloaded_bytes_per_second = None
        self._success_count = None
        self._success_per_second = None
        self._success_rate = None
        self._failure_count = None
        self._failure_per_second = None
        self._failure_rate = None
        self._percentile50 = None
        self._percentile90 = None
        self._percentile95 = None
        self._percentile99 = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if element_per_second is not None:
            self.element_per_second = element_per_second
        if min_duration is not None:
            self.min_duration = min_duration
        if max_duration is not None:
            self.max_duration = max_duration
        if sum_duration is not None:
            self.sum_duration = sum_duration
        if avg_duration is not None:
            self.avg_duration = avg_duration
        if min_ttfb is not None:
            self.min_ttfb = min_ttfb
        if max_ttfb is not None:
            self.max_ttfb = max_ttfb
        if sum_ttfb is not None:
            self.sum_ttfb = sum_ttfb
        if avg_ttfb is not None:
            self.avg_ttfb = avg_ttfb
        if sum_downloaded_bytes is not None:
            self.sum_downloaded_bytes = sum_downloaded_bytes
        if downloaded_bytes_per_second is not None:
            self.downloaded_bytes_per_second = downloaded_bytes_per_second
        if success_count is not None:
            self.success_count = success_count
        if success_per_second is not None:
            self.success_per_second = success_per_second
        if success_rate is not None:
            self.success_rate = success_rate
        if failure_count is not None:
            self.failure_count = failure_count
        if failure_per_second is not None:
            self.failure_per_second = failure_per_second
        if failure_rate is not None:
            self.failure_rate = failure_rate
        if percentile50 is not None:
            self.percentile50 = percentile50
        if percentile90 is not None:
            self.percentile90 = percentile90
        if percentile95 is not None:
            self.percentile95 = percentile95
        if percentile99 is not None:
            self.percentile99 = percentile99

    @property
    def count(self):
        """Gets the count of this ElementValues.  # noqa: E501

        Count statistics are the number of full executions of an element of a User Path. If the element is interrupted (because of error or end of test), then the count number is not incremented.  # noqa: E501

        :return: The count of this ElementValues.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ElementValues.

        Count statistics are the number of full executions of an element of a User Path. If the element is interrupted (because of error or end of test), then the count number is not incremented.  # noqa: E501

        :param count: The count of this ElementValues.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def element_per_second(self):
        """Gets the element_per_second of this ElementValues.  # noqa: E501

        Number of iterations of the element per second.  # noqa: E501

        :return: The element_per_second of this ElementValues.  # noqa: E501
        :rtype: float
        """
        return self._element_per_second

    @element_per_second.setter
    def element_per_second(self, element_per_second):
        """Sets the element_per_second of this ElementValues.

        Number of iterations of the element per second.  # noqa: E501

        :param element_per_second: The element_per_second of this ElementValues.  # noqa: E501
        :type: float
        """

        self._element_per_second = element_per_second

    @property
    def min_duration(self):
        """Gets the min_duration of this ElementValues.  # noqa: E501

        Shortest response time, in milliseconds.  # noqa: E501

        :return: The min_duration of this ElementValues.  # noqa: E501
        :rtype: int
        """
        return self._min_duration

    @min_duration.setter
    def min_duration(self, min_duration):
        """Sets the min_duration of this ElementValues.

        Shortest response time, in milliseconds.  # noqa: E501

        :param min_duration: The min_duration of this ElementValues.  # noqa: E501
        :type: int
        """

        self._min_duration = min_duration

    @property
    def max_duration(self):
        """Gets the max_duration of this ElementValues.  # noqa: E501

        Longest response time, in milliseconds.  # noqa: E501

        :return: The max_duration of this ElementValues.  # noqa: E501
        :rtype: int
        """
        return self._max_duration

    @max_duration.setter
    def max_duration(self, max_duration):
        """Sets the max_duration of this ElementValues.

        Longest response time, in milliseconds.  # noqa: E501

        :param max_duration: The max_duration of this ElementValues.  # noqa: E501
        :type: int
        """

        self._max_duration = max_duration

    @property
    def sum_duration(self):
        """Gets the sum_duration of this ElementValues.  # noqa: E501

        Sum of response time of all iterations, in milliseconds.  # noqa: E501

        :return: The sum_duration of this ElementValues.  # noqa: E501
        :rtype: int
        """
        return self._sum_duration

    @sum_duration.setter
    def sum_duration(self, sum_duration):
        """Sets the sum_duration of this ElementValues.

        Sum of response time of all iterations, in milliseconds.  # noqa: E501

        :param sum_duration: The sum_duration of this ElementValues.  # noqa: E501
        :type: int
        """

        self._sum_duration = sum_duration

    @property
    def avg_duration(self):
        """Gets the avg_duration of this ElementValues.  # noqa: E501

        Average response time, in milliseconds.  # noqa: E501

        :return: The avg_duration of this ElementValues.  # noqa: E501
        :rtype: float
        """
        return self._avg_duration

    @avg_duration.setter
    def avg_duration(self, avg_duration):
        """Sets the avg_duration of this ElementValues.

        Average response time, in milliseconds.  # noqa: E501

        :param avg_duration: The avg_duration of this ElementValues.  # noqa: E501
        :type: float
        """

        self._avg_duration = avg_duration

    @property
    def min_ttfb(self):
        """Gets the min_ttfb of this ElementValues.  # noqa: E501

        Shortest time to first byte, in milliseconds.  # noqa: E501

        :return: The min_ttfb of this ElementValues.  # noqa: E501
        :rtype: int
        """
        return self._min_ttfb

    @min_ttfb.setter
    def min_ttfb(self, min_ttfb):
        """Sets the min_ttfb of this ElementValues.

        Shortest time to first byte, in milliseconds.  # noqa: E501

        :param min_ttfb: The min_ttfb of this ElementValues.  # noqa: E501
        :type: int
        """

        self._min_ttfb = min_ttfb

    @property
    def max_ttfb(self):
        """Gets the max_ttfb of this ElementValues.  # noqa: E501

        Longest time to first byte, in milliseconds.  # noqa: E501

        :return: The max_ttfb of this ElementValues.  # noqa: E501
        :rtype: int
        """
        return self._max_ttfb

    @max_ttfb.setter
    def max_ttfb(self, max_ttfb):
        """Sets the max_ttfb of this ElementValues.

        Longest time to first byte, in milliseconds.  # noqa: E501

        :param max_ttfb: The max_ttfb of this ElementValues.  # noqa: E501
        :type: int
        """

        self._max_ttfb = max_ttfb

    @property
    def sum_ttfb(self):
        """Gets the sum_ttfb of this ElementValues.  # noqa: E501

        Sum of time to first byte of all iterations, in milliseconds.  # noqa: E501

        :return: The sum_ttfb of this ElementValues.  # noqa: E501
        :rtype: int
        """
        return self._sum_ttfb

    @sum_ttfb.setter
    def sum_ttfb(self, sum_ttfb):
        """Sets the sum_ttfb of this ElementValues.

        Sum of time to first byte of all iterations, in milliseconds.  # noqa: E501

        :param sum_ttfb: The sum_ttfb of this ElementValues.  # noqa: E501
        :type: int
        """

        self._sum_ttfb = sum_ttfb

    @property
    def avg_ttfb(self):
        """Gets the avg_ttfb of this ElementValues.  # noqa: E501

        Average time to first byte, in milliseconds.  # noqa: E501

        :return: The avg_ttfb of this ElementValues.  # noqa: E501
        :rtype: float
        """
        return self._avg_ttfb

    @avg_ttfb.setter
    def avg_ttfb(self, avg_ttfb):
        """Sets the avg_ttfb of this ElementValues.

        Average time to first byte, in milliseconds.  # noqa: E501

        :param avg_ttfb: The avg_ttfb of this ElementValues.  # noqa: E501
        :type: float
        """

        self._avg_ttfb = avg_ttfb

    @property
    def sum_downloaded_bytes(self):
        """Gets the sum_downloaded_bytes of this ElementValues.  # noqa: E501

        Total size of network traffic for the element, in bytes.  # noqa: E501

        :return: The sum_downloaded_bytes of this ElementValues.  # noqa: E501
        :rtype: int
        """
        return self._sum_downloaded_bytes

    @sum_downloaded_bytes.setter
    def sum_downloaded_bytes(self, sum_downloaded_bytes):
        """Sets the sum_downloaded_bytes of this ElementValues.

        Total size of network traffic for the element, in bytes.  # noqa: E501

        :param sum_downloaded_bytes: The sum_downloaded_bytes of this ElementValues.  # noqa: E501
        :type: int
        """

        self._sum_downloaded_bytes = sum_downloaded_bytes

    @property
    def downloaded_bytes_per_second(self):
        """Gets the downloaded_bytes_per_second of this ElementValues.  # noqa: E501

        Average size of network traffic for the element, in bytes per seconds.  # noqa: E501

        :return: The downloaded_bytes_per_second of this ElementValues.  # noqa: E501
        :rtype: float
        """
        return self._downloaded_bytes_per_second

    @downloaded_bytes_per_second.setter
    def downloaded_bytes_per_second(self, downloaded_bytes_per_second):
        """Sets the downloaded_bytes_per_second of this ElementValues.

        Average size of network traffic for the element, in bytes per seconds.  # noqa: E501

        :param downloaded_bytes_per_second: The downloaded_bytes_per_second of this ElementValues.  # noqa: E501
        :type: float
        """

        self._downloaded_bytes_per_second = downloaded_bytes_per_second

    @property
    def success_count(self):
        """Gets the success_count of this ElementValues.  # noqa: E501

        Count of succeeded iterations.  # noqa: E501

        :return: The success_count of this ElementValues.  # noqa: E501
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        """Sets the success_count of this ElementValues.

        Count of succeeded iterations.  # noqa: E501

        :param success_count: The success_count of this ElementValues.  # noqa: E501
        :type: int
        """

        self._success_count = success_count

    @property
    def success_per_second(self):
        """Gets the success_per_second of this ElementValues.  # noqa: E501

        Count of succeeded iterations per second.  # noqa: E501

        :return: The success_per_second of this ElementValues.  # noqa: E501
        :rtype: float
        """
        return self._success_per_second

    @success_per_second.setter
    def success_per_second(self, success_per_second):
        """Sets the success_per_second of this ElementValues.

        Count of succeeded iterations per second.  # noqa: E501

        :param success_per_second: The success_per_second of this ElementValues.  # noqa: E501
        :type: float
        """

        self._success_per_second = success_per_second

    @property
    def success_rate(self):
        """Gets the success_rate of this ElementValues.  # noqa: E501

        Percentage of succeeded iterations out of count.  # noqa: E501

        :return: The success_rate of this ElementValues.  # noqa: E501
        :rtype: float
        """
        return self._success_rate

    @success_rate.setter
    def success_rate(self, success_rate):
        """Sets the success_rate of this ElementValues.

        Percentage of succeeded iterations out of count.  # noqa: E501

        :param success_rate: The success_rate of this ElementValues.  # noqa: E501
        :type: float
        """

        self._success_rate = success_rate

    @property
    def failure_count(self):
        """Gets the failure_count of this ElementValues.  # noqa: E501

        Count of failed iterations.  # noqa: E501

        :return: The failure_count of this ElementValues.  # noqa: E501
        :rtype: int
        """
        return self._failure_count

    @failure_count.setter
    def failure_count(self, failure_count):
        """Sets the failure_count of this ElementValues.

        Count of failed iterations.  # noqa: E501

        :param failure_count: The failure_count of this ElementValues.  # noqa: E501
        :type: int
        """

        self._failure_count = failure_count

    @property
    def failure_per_second(self):
        """Gets the failure_per_second of this ElementValues.  # noqa: E501

        Count of failed iterations per second.  # noqa: E501

        :return: The failure_per_second of this ElementValues.  # noqa: E501
        :rtype: float
        """
        return self._failure_per_second

    @failure_per_second.setter
    def failure_per_second(self, failure_per_second):
        """Sets the failure_per_second of this ElementValues.

        Count of failed iterations per second.  # noqa: E501

        :param failure_per_second: The failure_per_second of this ElementValues.  # noqa: E501
        :type: float
        """

        self._failure_per_second = failure_per_second

    @property
    def failure_rate(self):
        """Gets the failure_rate of this ElementValues.  # noqa: E501

        Percentage of failed iterations out of count.  # noqa: E501

        :return: The failure_rate of this ElementValues.  # noqa: E501
        :rtype: float
        """
        return self._failure_rate

    @failure_rate.setter
    def failure_rate(self, failure_rate):
        """Sets the failure_rate of this ElementValues.

        Percentage of failed iterations out of count.  # noqa: E501

        :param failure_rate: The failure_rate of this ElementValues.  # noqa: E501
        :type: float
        """

        self._failure_rate = failure_rate

    @property
    def percentile50(self):
        """Gets the percentile50 of this ElementValues.  # noqa: E501

        50th percentile of the element duration, in milliseconds. Requires at least NeoLoad 7.1. Only available when test is terminated.  # noqa: E501

        :return: The percentile50 of this ElementValues.  # noqa: E501
        :rtype: float
        """
        return self._percentile50

    @percentile50.setter
    def percentile50(self, percentile50):
        """Sets the percentile50 of this ElementValues.

        50th percentile of the element duration, in milliseconds. Requires at least NeoLoad 7.1. Only available when test is terminated.  # noqa: E501

        :param percentile50: The percentile50 of this ElementValues.  # noqa: E501
        :type: float
        """

        self._percentile50 = percentile50

    @property
    def percentile90(self):
        """Gets the percentile90 of this ElementValues.  # noqa: E501

        90th percentile of the element duration, in milliseconds. Requires at least NeoLoad 7.1. Only available when test is terminated.  # noqa: E501

        :return: The percentile90 of this ElementValues.  # noqa: E501
        :rtype: float
        """
        return self._percentile90

    @percentile90.setter
    def percentile90(self, percentile90):
        """Sets the percentile90 of this ElementValues.

        90th percentile of the element duration, in milliseconds. Requires at least NeoLoad 7.1. Only available when test is terminated.  # noqa: E501

        :param percentile90: The percentile90 of this ElementValues.  # noqa: E501
        :type: float
        """

        self._percentile90 = percentile90

    @property
    def percentile95(self):
        """Gets the percentile95 of this ElementValues.  # noqa: E501

        95th percentile of the element duration, in milliseconds. Requires at least NeoLoad 7.1. Only available when test is terminated.  # noqa: E501

        :return: The percentile95 of this ElementValues.  # noqa: E501
        :rtype: float
        """
        return self._percentile95

    @percentile95.setter
    def percentile95(self, percentile95):
        """Sets the percentile95 of this ElementValues.

        95th percentile of the element duration, in milliseconds. Requires at least NeoLoad 7.1. Only available when test is terminated.  # noqa: E501

        :param percentile95: The percentile95 of this ElementValues.  # noqa: E501
        :type: float
        """

        self._percentile95 = percentile95

    @property
    def percentile99(self):
        """Gets the percentile99 of this ElementValues.  # noqa: E501

        99th percentile of the element duration, in milliseconds. Requires at least NeoLoad 7.1. Only available when test is terminated.  # noqa: E501

        :return: The percentile99 of this ElementValues.  # noqa: E501
        :rtype: float
        """
        return self._percentile99

    @percentile99.setter
    def percentile99(self, percentile99):
        """Sets the percentile99 of this ElementValues.

        99th percentile of the element duration, in milliseconds. Requires at least NeoLoad 7.1. Only available when test is terminated.  # noqa: E501

        :param percentile99: The percentile99 of this ElementValues.  # noqa: E501
        :type: float
        """

        self._percentile99 = percentile99

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ElementValues):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElementValues):
            return True

        return self.to_dict() != other.to_dict()
