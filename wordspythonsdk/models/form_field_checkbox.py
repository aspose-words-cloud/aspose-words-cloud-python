# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="FormFieldCheckbox.py">
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


class FormFieldCheckbox(object):
    """FormField checkbox element
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'check_box_size': 'float',
        'checked': 'bool',
        'is_check_box_exact_size': 'bool'
    }

    attribute_map = {
        'check_box_size': 'CheckBoxSize',
        'checked': 'Checked',
        'is_check_box_exact_size': 'IsCheckBoxExactSize'
    }

    def __init__(self, check_box_size=None, checked=None, is_check_box_exact_size=None):  # noqa: E501
        """FormFieldCheckbox - a model defined in Swagger"""  # noqa: E501

        self._check_box_size = None
        self._checked = None
        self._is_check_box_exact_size = None
        self.discriminator = None

        if check_box_size is not None:
            self.check_box_size = check_box_size
        if checked is not None:
            self.checked = checked
        if is_check_box_exact_size is not None:
            self.is_check_box_exact_size = is_check_box_exact_size

    @property
    def check_box_size(self):
        """Gets the check_box_size of this FormFieldCheckbox.  # noqa: E501

        Gets or sets the size of the checkbox in points. Has effect only when  is true.  # noqa: E501

        :return: The check_box_size of this FormFieldCheckbox.  # noqa: E501
        :rtype: float
        """
        return self._check_box_size

    @check_box_size.setter
    def check_box_size(self, check_box_size):
        """Sets the check_box_size of this FormFieldCheckbox.

        Gets or sets the size of the checkbox in points. Has effect only when  is true.  # noqa: E501

        :param check_box_size: The check_box_size of this FormFieldCheckbox.  # noqa: E501
        :type: float
        """

        self._check_box_size = check_box_size

    @property
    def checked(self):
        """Gets the checked of this FormFieldCheckbox.  # noqa: E501

        Gets or sets the checked status of the check box form field.  # noqa: E501

        :return: The checked of this FormFieldCheckbox.  # noqa: E501
        :rtype: bool
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        """Sets the checked of this FormFieldCheckbox.

        Gets or sets the checked status of the check box form field.  # noqa: E501

        :param checked: The checked of this FormFieldCheckbox.  # noqa: E501
        :type: bool
        """

        self._checked = checked

    @property
    def is_check_box_exact_size(self):
        """Gets the is_check_box_exact_size of this FormFieldCheckbox.  # noqa: E501

        Gets or sets the boolean value that indicates whether the size of the textbox is automatic or specified explicitly.  # noqa: E501

        :return: The is_check_box_exact_size of this FormFieldCheckbox.  # noqa: E501
        :rtype: bool
        """
        return self._is_check_box_exact_size

    @is_check_box_exact_size.setter
    def is_check_box_exact_size(self, is_check_box_exact_size):
        """Sets the is_check_box_exact_size of this FormFieldCheckbox.

        Gets or sets the boolean value that indicates whether the size of the textbox is automatic or specified explicitly.  # noqa: E501

        :param is_check_box_exact_size: The is_check_box_exact_size of this FormFieldCheckbox.  # noqa: E501
        :type: bool
        """

        self._is_check_box_exact_size = is_check_box_exact_size

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
        if not isinstance(other, FormFieldCheckbox):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
