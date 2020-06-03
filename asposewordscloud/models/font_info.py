# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="FontInfo.py">
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


class FontInfo(object):
    """Font info.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'font_family_name': 'str',
        'full_font_name': 'str',
        'version': 'str',
        'file_path': 'str'
    }

    attribute_map = {
        'font_family_name': 'FontFamilyName',
        'full_font_name': 'FullFontName',
        'version': 'Version',
        'file_path': 'FilePath'
    }

    def __init__(self, font_family_name=None, full_font_name=None, version=None, file_path=None):  # noqa: E501
        """FontInfo - a model defined in Swagger"""  # noqa: E501

        self._font_family_name = None
        self._full_font_name = None
        self._version = None
        self._file_path = None
        self.discriminator = None

        if font_family_name is not None:
            self.font_family_name = font_family_name
        if full_font_name is not None:
            self.full_font_name = full_font_name
        if version is not None:
            self.version = version
        if file_path is not None:
            self.file_path = file_path

    @property
    def font_family_name(self):
        """Gets the font_family_name of this FontInfo.  # noqa: E501

        Gets or sets family name of the font.  # noqa: E501

        :return: The font_family_name of this FontInfo.  # noqa: E501
        :rtype: str
        """
        return self._font_family_name

    @font_family_name.setter
    def font_family_name(self, font_family_name):
        """Sets the font_family_name of this FontInfo.

        Gets or sets family name of the font.  # noqa: E501

        :param font_family_name: The font_family_name of this FontInfo.  # noqa: E501
        :type: str
        """
        self._font_family_name = font_family_name
    @property
    def full_font_name(self):
        """Gets the full_font_name of this FontInfo.  # noqa: E501

        Gets or sets full name of the font.  # noqa: E501

        :return: The full_font_name of this FontInfo.  # noqa: E501
        :rtype: str
        """
        return self._full_font_name

    @full_font_name.setter
    def full_font_name(self, full_font_name):
        """Sets the full_font_name of this FontInfo.

        Gets or sets full name of the font.  # noqa: E501

        :param full_font_name: The full_font_name of this FontInfo.  # noqa: E501
        :type: str
        """
        self._full_font_name = full_font_name
    @property
    def version(self):
        """Gets the version of this FontInfo.  # noqa: E501

        Gets or sets version string of the font.  # noqa: E501

        :return: The version of this FontInfo.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FontInfo.

        Gets or sets version string of the font.  # noqa: E501

        :param version: The version of this FontInfo.  # noqa: E501
        :type: str
        """
        self._version = version
    @property
    def file_path(self):
        """Gets the file_path of this FontInfo.  # noqa: E501

        Gets or sets path to the font file if any.  # noqa: E501

        :return: The file_path of this FontInfo.  # noqa: E501
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this FontInfo.

        Gets or sets path to the font file if any.  # noqa: E501

        :param file_path: The file_path of this FontInfo.  # noqa: E501
        :type: str
        """
        self._file_path = file_path
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
        if not isinstance(other, FontInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
