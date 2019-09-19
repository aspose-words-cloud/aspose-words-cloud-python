# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="PageStatData.py">
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


class PageStatData(object):
    """Container for the page&#39;s statistical data.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'page_number': 'int',
        'word_count': 'int',
        'paragraph_count': 'int',
        'footnotes_stat_data': 'FootnotesStatData'
    }

    attribute_map = {
        'page_number': 'PageNumber',
        'word_count': 'WordCount',
        'paragraph_count': 'ParagraphCount',
        'footnotes_stat_data': 'FootnotesStatData'
    }

    def __init__(self, page_number=None, word_count=None, paragraph_count=None, footnotes_stat_data=None):  # noqa: E501
        """PageStatData - a model defined in Swagger"""  # noqa: E501

        self._page_number = None
        self._word_count = None
        self._paragraph_count = None
        self._footnotes_stat_data = None
        self.discriminator = None

        if page_number is not None:
            self.page_number = page_number
        if word_count is not None:
            self.word_count = word_count
        if paragraph_count is not None:
            self.paragraph_count = paragraph_count
        if footnotes_stat_data is not None:
            self.footnotes_stat_data = footnotes_stat_data

    @property
    def page_number(self):
        """Gets the page_number of this PageStatData.  # noqa: E501

        Gets or sets page number.  # noqa: E501

        :return: The page_number of this PageStatData.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this PageStatData.

        Gets or sets page number.  # noqa: E501

        :param page_number: The page_number of this PageStatData.  # noqa: E501
        :type: int
        """
        if page_number is None:
            raise ValueError("Invalid value for `page_number`, must not be `None`")  # noqa: E501
        self._page_number = page_number
    @property
    def word_count(self):
        """Gets the word_count of this PageStatData.  # noqa: E501

        Gets or sets total count of words in the page.  # noqa: E501

        :return: The word_count of this PageStatData.  # noqa: E501
        :rtype: int
        """
        return self._word_count

    @word_count.setter
    def word_count(self, word_count):
        """Sets the word_count of this PageStatData.

        Gets or sets total count of words in the page.  # noqa: E501

        :param word_count: The word_count of this PageStatData.  # noqa: E501
        :type: int
        """
        if word_count is None:
            raise ValueError("Invalid value for `word_count`, must not be `None`")  # noqa: E501
        self._word_count = word_count
    @property
    def paragraph_count(self):
        """Gets the paragraph_count of this PageStatData.  # noqa: E501

        Gets or sets total count of paragraphs in the page.  # noqa: E501

        :return: The paragraph_count of this PageStatData.  # noqa: E501
        :rtype: int
        """
        return self._paragraph_count

    @paragraph_count.setter
    def paragraph_count(self, paragraph_count):
        """Sets the paragraph_count of this PageStatData.

        Gets or sets total count of paragraphs in the page.  # noqa: E501

        :param paragraph_count: The paragraph_count of this PageStatData.  # noqa: E501
        :type: int
        """
        if paragraph_count is None:
            raise ValueError("Invalid value for `paragraph_count`, must not be `None`")  # noqa: E501
        self._paragraph_count = paragraph_count
    @property
    def footnotes_stat_data(self):
        """Gets the footnotes_stat_data of this PageStatData.  # noqa: E501

        Gets or sets detailed statistics of footnotes.  # noqa: E501

        :return: The footnotes_stat_data of this PageStatData.  # noqa: E501
        :rtype: FootnotesStatData
        """
        return self._footnotes_stat_data

    @footnotes_stat_data.setter
    def footnotes_stat_data(self, footnotes_stat_data):
        """Sets the footnotes_stat_data of this PageStatData.

        Gets or sets detailed statistics of footnotes.  # noqa: E501

        :param footnotes_stat_data: The footnotes_stat_data of this PageStatData.  # noqa: E501
        :type: FootnotesStatData
        """
        self._footnotes_stat_data = footnotes_stat_data
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
        if not isinstance(other, PageStatData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
