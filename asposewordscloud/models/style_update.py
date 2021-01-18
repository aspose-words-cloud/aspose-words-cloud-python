# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="style_update.py">
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


class StyleUpdate(object):
    """Represents a single document style properties to update.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'base_style_name': 'str',
        'is_quick_style': 'bool',
        'name': 'str',
        'next_paragraph_style_name': 'str'
    }

    attribute_map = {
        'base_style_name': 'BaseStyleName',
        'is_quick_style': 'IsQuickStyle',
        'name': 'Name',
        'next_paragraph_style_name': 'NextParagraphStyleName'
    }

    def __init__(self, base_style_name=None, is_quick_style=None, name=None, next_paragraph_style_name=None):  # noqa: E501
        """StyleUpdate - a model defined in Swagger"""  # noqa: E501

        self._base_style_name = None
        self._is_quick_style = None
        self._name = None
        self._next_paragraph_style_name = None
        self.discriminator = None

        if base_style_name is not None:
            self.base_style_name = base_style_name
        if is_quick_style is not None:
            self.is_quick_style = is_quick_style
        if name is not None:
            self.name = name
        if next_paragraph_style_name is not None:
            self.next_paragraph_style_name = next_paragraph_style_name

    @property
    def base_style_name(self):
        """Gets the base_style_name of this StyleUpdate.  # noqa: E501

        Gets or sets the name of the style this style is based on.  # noqa: E501

        :return: The base_style_name of this StyleUpdate.  # noqa: E501
        :rtype: str
        """
        return self._base_style_name

    @base_style_name.setter
    def base_style_name(self, base_style_name):
        """Sets the base_style_name of this StyleUpdate.

        Gets or sets the name of the style this style is based on.  # noqa: E501

        :param base_style_name: The base_style_name of this StyleUpdate.  # noqa: E501
        :type: str
        """
        self._base_style_name = base_style_name

    @property
    def is_quick_style(self):
        """Gets the is_quick_style of this StyleUpdate.  # noqa: E501

        Gets or sets a value indicating whether this style is shown in the Quick Style gallery inside MS Word UI.  # noqa: E501

        :return: The is_quick_style of this StyleUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._is_quick_style

    @is_quick_style.setter
    def is_quick_style(self, is_quick_style):
        """Sets the is_quick_style of this StyleUpdate.

        Gets or sets a value indicating whether this style is shown in the Quick Style gallery inside MS Word UI.  # noqa: E501

        :param is_quick_style: The is_quick_style of this StyleUpdate.  # noqa: E501
        :type: bool
        """
        self._is_quick_style = is_quick_style

    @property
    def name(self):
        """Gets the name of this StyleUpdate.  # noqa: E501

        Gets or sets the name of the style.  # noqa: E501

        :return: The name of this StyleUpdate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StyleUpdate.

        Gets or sets the name of the style.  # noqa: E501

        :param name: The name of this StyleUpdate.  # noqa: E501
        :type: str
        """
        self._name = name

    @property
    def next_paragraph_style_name(self):
        """Gets the next_paragraph_style_name of this StyleUpdate.  # noqa: E501

        Gets or sets the name of the style to be applied automatically to a new paragraph inserted after a paragraph formatted with the specified style.  # noqa: E501

        :return: The next_paragraph_style_name of this StyleUpdate.  # noqa: E501
        :rtype: str
        """
        return self._next_paragraph_style_name

    @next_paragraph_style_name.setter
    def next_paragraph_style_name(self, next_paragraph_style_name):
        """Sets the next_paragraph_style_name of this StyleUpdate.

        Gets or sets the name of the style to be applied automatically to a new paragraph inserted after a paragraph formatted with the specified style.  # noqa: E501

        :param next_paragraph_style_name: The next_paragraph_style_name of this StyleUpdate.  # noqa: E501
        :type: str
        """
        self._next_paragraph_style_name = next_paragraph_style_name


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
        if not isinstance(other, StyleUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other