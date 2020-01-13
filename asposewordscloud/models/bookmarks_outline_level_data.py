# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="BookmarksOutlineLevelData.py">
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


class BookmarksOutlineLevelData(object):
    """container class for individual bookmarks outline level.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'bookmarks_outline_level': 'int'
    }

    attribute_map = {
        'name': 'Name',
        'bookmarks_outline_level': 'BookmarksOutlineLevel'
    }

    def __init__(self, name=None, bookmarks_outline_level=None):  # noqa: E501
        """BookmarksOutlineLevelData - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._bookmarks_outline_level = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if bookmarks_outline_level is not None:
            self.bookmarks_outline_level = bookmarks_outline_level

    @property
    def name(self):
        """Gets the name of this BookmarksOutlineLevelData.  # noqa: E501

        Gets or sets specify the bookmark's name.  # noqa: E501

        :return: The name of this BookmarksOutlineLevelData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BookmarksOutlineLevelData.

        Gets or sets specify the bookmark's name.  # noqa: E501

        :param name: The name of this BookmarksOutlineLevelData.  # noqa: E501
        :type: str
        """
        self._name = name
    @property
    def bookmarks_outline_level(self):
        """Gets the bookmarks_outline_level of this BookmarksOutlineLevelData.  # noqa: E501

        Gets or sets specify the bookmark's level.  # noqa: E501

        :return: The bookmarks_outline_level of this BookmarksOutlineLevelData.  # noqa: E501
        :rtype: int
        """
        return self._bookmarks_outline_level

    @bookmarks_outline_level.setter
    def bookmarks_outline_level(self, bookmarks_outline_level):
        """Sets the bookmarks_outline_level of this BookmarksOutlineLevelData.

        Gets or sets specify the bookmark's level.  # noqa: E501

        :param bookmarks_outline_level: The bookmarks_outline_level of this BookmarksOutlineLevelData.  # noqa: E501
        :type: int
        """
        if bookmarks_outline_level is None:
            raise ValueError("Invalid value for `bookmarks_outline_level`, must not be `None`")  # noqa: E501
        self._bookmarks_outline_level = bookmarks_outline_level
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
        if not isinstance(other, BookmarksOutlineLevelData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
