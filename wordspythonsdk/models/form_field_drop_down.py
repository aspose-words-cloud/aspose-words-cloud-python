# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="FormFieldDropDown.py">
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


class FormFieldDropDown(object):
    """FormField dropdownlist element
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'drop_down_items': 'list[str]',
        'drop_down_selected_index': 'int'
    }

    attribute_map = {
        'drop_down_items': 'DropDownItems',
        'drop_down_selected_index': 'DropDownSelectedIndex'
    }

    def __init__(self, drop_down_items=None, drop_down_selected_index=None):  # noqa: E501
        """FormFieldDropDown - a model defined in Swagger"""  # noqa: E501

        self._drop_down_items = None
        self._drop_down_selected_index = None
        self.discriminator = None

        if drop_down_items is not None:
            self.drop_down_items = drop_down_items
        if drop_down_selected_index is not None:
            self.drop_down_selected_index = drop_down_selected_index

    @property
    def drop_down_items(self):
        """Gets the drop_down_items of this FormFieldDropDown.  # noqa: E501

        Provides access to the items of a dropdown form field.  # noqa: E501

        :return: The drop_down_items of this FormFieldDropDown.  # noqa: E501
        :rtype: list[str]
        """
        return self._drop_down_items

    @drop_down_items.setter
    def drop_down_items(self, drop_down_items):
        """Sets the drop_down_items of this FormFieldDropDown.

        Provides access to the items of a dropdown form field.  # noqa: E501

        :param drop_down_items: The drop_down_items of this FormFieldDropDown.  # noqa: E501
        :type: list[str]
        """

        self._drop_down_items = drop_down_items

    @property
    def drop_down_selected_index(self):
        """Gets the drop_down_selected_index of this FormFieldDropDown.  # noqa: E501

        Gets or sets the index specifying the currently selected item in a dropdown form field.  # noqa: E501

        :return: The drop_down_selected_index of this FormFieldDropDown.  # noqa: E501
        :rtype: int
        """
        return self._drop_down_selected_index

    @drop_down_selected_index.setter
    def drop_down_selected_index(self, drop_down_selected_index):
        """Sets the drop_down_selected_index of this FormFieldDropDown.

        Gets or sets the index specifying the currently selected item in a dropdown form field.  # noqa: E501

        :param drop_down_selected_index: The drop_down_selected_index of this FormFieldDropDown.  # noqa: E501
        :type: int
        """

        self._drop_down_selected_index = drop_down_selected_index

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
        if not isinstance(other, FormFieldDropDown):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
