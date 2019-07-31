# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="StringFormatData.py">
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


class StringFormatData(object):
    """Allows to specify System.Drawing.StringFormat options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'alignment': 'str',
        'format_flags': 'str',
        'hotkey_prefix': 'str',
        'line_alignment': 'str',
        'trimming': 'str'
    }

    attribute_map = {
        'alignment': 'Alignment',
        'format_flags': 'FormatFlags',
        'hotkey_prefix': 'HotkeyPrefix',
        'line_alignment': 'LineAlignment',
        'trimming': 'Trimming'
    }

    def __init__(self, alignment=None, format_flags=None, hotkey_prefix=None, line_alignment=None, trimming=None):  # noqa: E501
        """StringFormatData - a model defined in Swagger"""  # noqa: E501

        self._alignment = None
        self._format_flags = None
        self._hotkey_prefix = None
        self._line_alignment = None
        self._trimming = None
        self.discriminator = None

        if alignment is not None:
            self.alignment = alignment
        if format_flags is not None:
            self.format_flags = format_flags
        if hotkey_prefix is not None:
            self.hotkey_prefix = hotkey_prefix
        if line_alignment is not None:
            self.line_alignment = line_alignment
        if trimming is not None:
            self.trimming = trimming

    @property
    def alignment(self):
        """Gets the alignment of this StringFormatData.  # noqa: E501

        Gets or sets horizontal alignment of the string.  # noqa: E501

        :return: The alignment of this StringFormatData.  # noqa: E501
        :rtype: str
        """
        return self._alignment

    @alignment.setter
    def alignment(self, alignment):
        """Sets the alignment of this StringFormatData.

        Gets or sets horizontal alignment of the string.  # noqa: E501

        :param alignment: The alignment of this StringFormatData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Near", "Center", "Far"]  # noqa: E501
        if not alignment.isdigit():	
            if alignment not in allowed_values:
                raise ValueError(
                    "Invalid value for `alignment` ({0}), must be one of {1}"  # noqa: E501
                    .format(alignment, allowed_values))
            self._alignment = alignment
        else:
            self._alignment = allowed_values[int(alignment) if six.PY3 else long(alignment)]
    @property
    def format_flags(self):
        """Gets the format_flags of this StringFormatData.  # noqa: E501

        Gets or sets a System.Drawing.StringFormatFlags enumeration that contains formatting information.  # noqa: E501

        :return: The format_flags of this StringFormatData.  # noqa: E501
        :rtype: str
        """
        return self._format_flags

    @format_flags.setter
    def format_flags(self, format_flags):
        """Sets the format_flags of this StringFormatData.

        Gets or sets a System.Drawing.StringFormatFlags enumeration that contains formatting information.  # noqa: E501

        :param format_flags: The format_flags of this StringFormatData.  # noqa: E501
        :type: str
        """
        allowed_values = ["DirectionRightToLeft", "DirectionVertical", "FitBlackBox", "DisplayFormatControl", "NoFontFallback", "MeasureTrailingSpaces", "NoWrap", "LineLimit", "NoClip"]  # noqa: E501
        if not format_flags.isdigit():	
            if format_flags not in allowed_values:
                raise ValueError(
                    "Invalid value for `format_flags` ({0}), must be one of {1}"  # noqa: E501
                    .format(format_flags, allowed_values))
            self._format_flags = format_flags
        else:
            self._format_flags = allowed_values[int(format_flags) if six.PY3 else long(format_flags)]
    @property
    def hotkey_prefix(self):
        """Gets the hotkey_prefix of this StringFormatData.  # noqa: E501

        Gets or sets the System.Drawing.Text.HotkeyPrefix object for this System.Drawing.StringFormat object.  # noqa: E501

        :return: The hotkey_prefix of this StringFormatData.  # noqa: E501
        :rtype: str
        """
        return self._hotkey_prefix

    @hotkey_prefix.setter
    def hotkey_prefix(self, hotkey_prefix):
        """Sets the hotkey_prefix of this StringFormatData.

        Gets or sets the System.Drawing.Text.HotkeyPrefix object for this System.Drawing.StringFormat object.  # noqa: E501

        :param hotkey_prefix: The hotkey_prefix of this StringFormatData.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Show", "Hide"]  # noqa: E501
        if not hotkey_prefix.isdigit():	
            if hotkey_prefix not in allowed_values:
                raise ValueError(
                    "Invalid value for `hotkey_prefix` ({0}), must be one of {1}"  # noqa: E501
                    .format(hotkey_prefix, allowed_values))
            self._hotkey_prefix = hotkey_prefix
        else:
            self._hotkey_prefix = allowed_values[int(hotkey_prefix) if six.PY3 else long(hotkey_prefix)]
    @property
    def line_alignment(self):
        """Gets the line_alignment of this StringFormatData.  # noqa: E501

        Gets or sets the vertical alignment of the string.  # noqa: E501

        :return: The line_alignment of this StringFormatData.  # noqa: E501
        :rtype: str
        """
        return self._line_alignment

    @line_alignment.setter
    def line_alignment(self, line_alignment):
        """Sets the line_alignment of this StringFormatData.

        Gets or sets the vertical alignment of the string.  # noqa: E501

        :param line_alignment: The line_alignment of this StringFormatData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Near", "Center", "Far"]  # noqa: E501
        if not line_alignment.isdigit():	
            if line_alignment not in allowed_values:
                raise ValueError(
                    "Invalid value for `line_alignment` ({0}), must be one of {1}"  # noqa: E501
                    .format(line_alignment, allowed_values))
            self._line_alignment = line_alignment
        else:
            self._line_alignment = allowed_values[int(line_alignment) if six.PY3 else long(line_alignment)]
    @property
    def trimming(self):
        """Gets the trimming of this StringFormatData.  # noqa: E501

        Gets or sets the System.Drawing.StringTrimming enumeration for this System.Drawing.StringFormat object.  # noqa: E501

        :return: The trimming of this StringFormatData.  # noqa: E501
        :rtype: str
        """
        return self._trimming

    @trimming.setter
    def trimming(self, trimming):
        """Sets the trimming of this StringFormatData.

        Gets or sets the System.Drawing.StringTrimming enumeration for this System.Drawing.StringFormat object.  # noqa: E501

        :param trimming: The trimming of this StringFormatData.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Character", "Word", "EllipsisCharacter", "EllipsisWord", "EllipsisPath"]  # noqa: E501
        if not trimming.isdigit():	
            if trimming not in allowed_values:
                raise ValueError(
                    "Invalid value for `trimming` ({0}), must be one of {1}"  # noqa: E501
                    .format(trimming, allowed_values))
            self._trimming = trimming
        else:
            self._trimming = allowed_values[int(trimming) if six.PY3 else long(trimming)]
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
        if not isinstance(other, StringFormatData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
