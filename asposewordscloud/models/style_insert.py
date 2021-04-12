# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="style_insert.py">
#   Copyright (c) 2021 Aspose.Words for Cloud
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

import datetime
import six
import json


class StyleInsert(object):
    """Represents a single document style to insert.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'style_name': 'str',
        'style_type': 'str'
    }

    attribute_map = {
        'style_name': 'StyleName',
        'style_type': 'StyleType'
    }

    def __init__(self, style_name=None, style_type=None):  # noqa: E501
        """StyleInsert - a model defined in Swagger"""  # noqa: E501

        self._style_name = None
        self._style_type = None
        self.discriminator = None

        if style_name is not None:
            self.style_name = style_name
        if style_type is not None:
            self.style_type = style_type

    @property
    def style_name(self):
        """Gets the style_name of this StyleInsert.  # noqa: E501

        Gets or sets the case sensitive name of the style to create.  # noqa: E501

        :return: The style_name of this StyleInsert.  # noqa: E501
        :rtype: str
        """
        return self._style_name

    @style_name.setter
    def style_name(self, style_name):
        """Sets the style_name of this StyleInsert.

        Gets or sets the case sensitive name of the style to create.  # noqa: E501

        :param style_name: The style_name of this StyleInsert.  # noqa: E501
        :type: str
        """
        self._style_name = style_name

    @property
    def style_type(self):
        """Gets the style_type of this StyleInsert.  # noqa: E501

        Gets or sets the StyleType value that specifies the type of the style to create.  # noqa: E501

        :return: The style_type of this StyleInsert.  # noqa: E501
        :rtype: str
        """
        return self._style_type

    @style_type.setter
    def style_type(self, style_type):
        """Sets the style_type of this StyleInsert.

        Gets or sets the StyleType value that specifies the type of the style to create.  # noqa: E501

        :param style_type: The style_type of this StyleInsert.  # noqa: E501
        :type: str
        """
        allowed_values = ["Paragraph", "Character", "Table", "List"]  # noqa: E501
        if not style_type.isdigit():
            if style_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `style_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(style_type, allowed_values))
            self._style_type = style_type
        else:
            self._style_type = allowed_values[int(style_type) if six.PY3 else long(style_type)]


    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if value is None:
                continue
            if isinstance(value, list):
                result[self.attribute_map[attr]] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map[attr]] = value.to_dict()
            elif isinstance(value, dict):
                result[self.attribute_map[attr]] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            elif isinstance(value, (datetime.datetime, datetime.date)):
                result[self.attribute_map[attr]] = value.isoformat()
            else:
                result[self.attribute_map[attr]] = value

        return result

    def to_json(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map[attr]] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map[attr]] = value.to_dict()
            elif isinstance(value, dict):
                result[self.attribute_map[attr]] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            elif isinstance(value, (datetime.datetime, datetime.date)):
                result[self.attribute_map[attr]] = value.isoformat()
            else:
                result[self.attribute_map[attr]] = value

        return json.dumps(result)

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StyleInsert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other