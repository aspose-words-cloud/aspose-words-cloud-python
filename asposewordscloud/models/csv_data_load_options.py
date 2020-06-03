# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="CsvDataLoadOptions.py">
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


class CsvDataLoadOptions(object):
    """Represents options for parsing CSV data.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'has_headers': 'bool',
        'delimiter': 'str',
        'quote_char': 'str',
        'comment_char': 'str'
    }

    attribute_map = {
        'has_headers': 'HasHeaders',
        'delimiter': 'Delimiter',
        'quote_char': 'QuoteChar',
        'comment_char': 'CommentChar'
    }

    def __init__(self, has_headers=None, delimiter=None, quote_char=None, comment_char=None):  # noqa: E501
        """CsvDataLoadOptions - a model defined in Swagger"""  # noqa: E501

        self._has_headers = None
        self._delimiter = None
        self._quote_char = None
        self._comment_char = None
        self.discriminator = None

        if has_headers is not None:
            self.has_headers = has_headers
        if delimiter is not None:
            self.delimiter = delimiter
        if quote_char is not None:
            self.quote_char = quote_char
        if comment_char is not None:
            self.comment_char = comment_char

    @property
    def has_headers(self):
        """Gets the has_headers of this CsvDataLoadOptions.  # noqa: E501

        Gets or sets a value indicating whether the first record of CSV data contains column names.  # noqa: E501

        :return: The has_headers of this CsvDataLoadOptions.  # noqa: E501
        :rtype: bool
        """
        return self._has_headers

    @has_headers.setter
    def has_headers(self, has_headers):
        """Sets the has_headers of this CsvDataLoadOptions.

        Gets or sets a value indicating whether the first record of CSV data contains column names.  # noqa: E501

        :param has_headers: The has_headers of this CsvDataLoadOptions.  # noqa: E501
        :type: bool
        """
        self._has_headers = has_headers
    @property
    def delimiter(self):
        """Gets the delimiter of this CsvDataLoadOptions.  # noqa: E501

        Gets or sets the character to be used as a column delimiter.  # noqa: E501

        :return: The delimiter of this CsvDataLoadOptions.  # noqa: E501
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        """Sets the delimiter of this CsvDataLoadOptions.

        Gets or sets the character to be used as a column delimiter.  # noqa: E501

        :param delimiter: The delimiter of this CsvDataLoadOptions.  # noqa: E501
        :type: str
        """
        self._delimiter = delimiter
    @property
    def quote_char(self):
        """Gets the quote_char of this CsvDataLoadOptions.  # noqa: E501

        Gets or sets the character that is used to quote field values.  # noqa: E501

        :return: The quote_char of this CsvDataLoadOptions.  # noqa: E501
        :rtype: str
        """
        return self._quote_char

    @quote_char.setter
    def quote_char(self, quote_char):
        """Sets the quote_char of this CsvDataLoadOptions.

        Gets or sets the character that is used to quote field values.  # noqa: E501

        :param quote_char: The quote_char of this CsvDataLoadOptions.  # noqa: E501
        :type: str
        """
        self._quote_char = quote_char
    @property
    def comment_char(self):
        """Gets the comment_char of this CsvDataLoadOptions.  # noqa: E501

        Gets or sets the character that is used to comment lines of CSV data.  # noqa: E501

        :return: The comment_char of this CsvDataLoadOptions.  # noqa: E501
        :rtype: str
        """
        return self._comment_char

    @comment_char.setter
    def comment_char(self, comment_char):
        """Sets the comment_char of this CsvDataLoadOptions.

        Gets or sets the character that is used to comment lines of CSV data.  # noqa: E501

        :param comment_char: The comment_char of this CsvDataLoadOptions.  # noqa: E501
        :type: str
        """
        self._comment_char = comment_char
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
        if not isinstance(other, CsvDataLoadOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
