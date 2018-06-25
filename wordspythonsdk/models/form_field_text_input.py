# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="FormFieldTextInput.py">
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


class FormFieldTextInput(object):
    """FormField text input element
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'max_length': 'int',
        'text_input_default': 'str',
        'text_input_format': 'str',
        'text_input_type': 'str'
    }

    attribute_map = {
        'max_length': 'MaxLength',
        'text_input_default': 'TextInputDefault',
        'text_input_format': 'TextInputFormat',
        'text_input_type': 'TextInputType'
    }

    def __init__(self, max_length=None, text_input_default=None, text_input_format=None, text_input_type=None):  # noqa: E501
        """FormFieldTextInput - a model defined in Swagger"""  # noqa: E501

        self._max_length = None
        self._text_input_default = None
        self._text_input_format = None
        self._text_input_type = None
        self.discriminator = None

        if max_length is not None:
            self.max_length = max_length
        if text_input_default is not None:
            self.text_input_default = text_input_default
        if text_input_format is not None:
            self.text_input_format = text_input_format
        if text_input_type is not None:
            self.text_input_type = text_input_type

    @property
    def max_length(self):
        """Gets the max_length of this FormFieldTextInput.  # noqa: E501

        Maximum length for the text field. Zero when the length is not limited.  # noqa: E501

        :return: The max_length of this FormFieldTextInput.  # noqa: E501
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this FormFieldTextInput.

        Maximum length for the text field. Zero when the length is not limited.  # noqa: E501

        :param max_length: The max_length of this FormFieldTextInput.  # noqa: E501
        :type: int
        """

        self._max_length = max_length

    @property
    def text_input_default(self):
        """Gets the text_input_default of this FormFieldTextInput.  # noqa: E501

        Gets or sets the default string or a calculation expression of a text form field.   # noqa: E501

        :return: The text_input_default of this FormFieldTextInput.  # noqa: E501
        :rtype: str
        """
        return self._text_input_default

    @text_input_default.setter
    def text_input_default(self, text_input_default):
        """Sets the text_input_default of this FormFieldTextInput.

        Gets or sets the default string or a calculation expression of a text form field.   # noqa: E501

        :param text_input_default: The text_input_default of this FormFieldTextInput.  # noqa: E501
        :type: str
        """

        self._text_input_default = text_input_default

    @property
    def text_input_format(self):
        """Gets the text_input_format of this FormFieldTextInput.  # noqa: E501

        Returns or sets the text formatting for a text form field.  # noqa: E501

        :return: The text_input_format of this FormFieldTextInput.  # noqa: E501
        :rtype: str
        """
        return self._text_input_format

    @text_input_format.setter
    def text_input_format(self, text_input_format):
        """Sets the text_input_format of this FormFieldTextInput.

        Returns or sets the text formatting for a text form field.  # noqa: E501

        :param text_input_format: The text_input_format of this FormFieldTextInput.  # noqa: E501
        :type: str
        """

        self._text_input_format = text_input_format

    @property
    def text_input_type(self):
        """Gets the text_input_type of this FormFieldTextInput.  # noqa: E501

        Gets or sets the type of a text form field.  # noqa: E501

        :return: The text_input_type of this FormFieldTextInput.  # noqa: E501
        :rtype: str
        """
        return self._text_input_type

    @text_input_type.setter
    def text_input_type(self, text_input_type):
        """Sets the text_input_type of this FormFieldTextInput.

        Gets or sets the type of a text form field.  # noqa: E501

        :param text_input_type: The text_input_type of this FormFieldTextInput.  # noqa: E501
        :type: str
        """
        allowed_values = ["Regular", "Number", "Date", "CurrentDate", "CurrentTime", "Calculated"]  # noqa: E501
        if text_input_type not in allowed_values:
            raise ValueError(
                "Invalid value for `text_input_type` ({0}), must be one of {1}"  # noqa: E501
                .format(text_input_type, allowed_values)
            )

        self._text_input_type = text_input_type

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
        if not isinstance(other, FormFieldTextInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
