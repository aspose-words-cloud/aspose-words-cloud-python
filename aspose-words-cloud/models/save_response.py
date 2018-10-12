# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="SaveResponse.py">
#   Copyright (c) 2018 Aspose.Words for Cloud
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


class SaveResponse(object):
    """Save response.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'int',
        'status': 'str',
        'save_result': 'SaveResult'
    }

    attribute_map = {
        'code': 'Code',
        'status': 'Status',
        'save_result': 'SaveResult'
    }

    def __init__(self, code=None, status=None, save_result=None):  # noqa: E501
        """SaveResponse - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._status = None
        self._save_result = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if status is not None:
            self.status = status
        if save_result is not None:
            self.save_result = save_result

    @property
    def code(self):
        """Gets the code of this SaveResponse.  # noqa: E501

        Response status code.  # noqa: E501

        :return: The code of this SaveResponse.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this SaveResponse.

        Response status code.  # noqa: E501

        :param code: The code of this SaveResponse.  # noqa: E501
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        self._code = code
    @property
    def status(self):
        """Gets the status of this SaveResponse.  # noqa: E501

        Response status.  # noqa: E501

        :return: The status of this SaveResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SaveResponse.

        Response status.  # noqa: E501

        :param status: The status of this SaveResponse.  # noqa: E501
        :type: str
        """
        self._status = status
    @property
    def save_result(self):
        """Gets the save_result of this SaveResponse.  # noqa: E501

        Save result.  # noqa: E501

        :return: The save_result of this SaveResponse.  # noqa: E501
        :rtype: SaveResult
        """
        return self._save_result

    @save_result.setter
    def save_result(self, save_result):
        """Sets the save_result of this SaveResponse.

        Save result.  # noqa: E501

        :param save_result: The save_result of this SaveResponse.  # noqa: E501
        :type: SaveResult
        """
        self._save_result = save_result
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
        if not isinstance(other, SaveResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
