# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="ErrorDetails.py">
#   Copyright (c) 2019 Aspose.Words for Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------
import pprint
import re  # noqa: F401

import six


class ErrorDetails(object):
    """The error details
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'request_id': 'str',
        'error_date_time': 'datetime'
    }

    attribute_map = {
        'request_id': 'RequestId',
        'error_date_time': 'ErrorDateTime'
    }

    def __init__(self, request_id=None, error_date_time=None):  # noqa: E501
        """ErrorDetails - a model defined in Swagger"""  # noqa: E501

        self._request_id = None
        self._error_date_time = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if error_date_time is not None:
            self.error_date_time = error_date_time

    @property
    def request_id(self):
        """Gets the request_id of this ErrorDetails.  # noqa: E501

        The request id.  # noqa: E501

        :return: The request_id of this ErrorDetails.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ErrorDetails.

        The request id.  # noqa: E501

        :param request_id: The request_id of this ErrorDetails.  # noqa: E501
        :type: str
        """
        self._request_id = request_id
    @property
    def error_date_time(self):
        """Gets the error_date_time of this ErrorDetails.  # noqa: E501

        Error datetime.  # noqa: E501

        :return: The error_date_time of this ErrorDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._error_date_time

    @error_date_time.setter
    def error_date_time(self, error_date_time):
        """Sets the error_date_time of this ErrorDetails.

        Error datetime.  # noqa: E501

        :param error_date_time: The error_date_time of this ErrorDetails.  # noqa: E501
        :type: datetime
        """
        if error_date_time is None:
            raise ValueError("Invalid value for `error_date_time`, must not be `None`")  # noqa: E501
        self._error_date_time = error_date_time
    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, ErrorDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
