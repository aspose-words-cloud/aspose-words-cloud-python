# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="OutlineOptionsData.py">
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


class OutlineOptionsData(object):
    """container class for outline options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bookmarks_outline_levels': 'list[BookmarksOutlineLevelData]',
        'default_bookmarks_outline_level': 'int',
        'create_missing_outline_levels': 'bool',
        'create_outlines_for_headings_in_tables': 'bool',
        'expanded_outline_levels': 'int',
        'headings_outline_levels': 'int'
    }

    attribute_map = {
        'bookmarks_outline_levels': 'BookmarksOutlineLevels',
        'default_bookmarks_outline_level': 'DefaultBookmarksOutlineLevel',
        'create_missing_outline_levels': 'CreateMissingOutlineLevels',
        'create_outlines_for_headings_in_tables': 'CreateOutlinesForHeadingsInTables',
        'expanded_outline_levels': 'ExpandedOutlineLevels',
        'headings_outline_levels': 'HeadingsOutlineLevels'
    }

    def __init__(self, bookmarks_outline_levels=None, default_bookmarks_outline_level=None, create_missing_outline_levels=None, create_outlines_for_headings_in_tables=None, expanded_outline_levels=None, headings_outline_levels=None):  # noqa: E501
        """OutlineOptionsData - a model defined in Swagger"""  # noqa: E501

        self._bookmarks_outline_levels = None
        self._default_bookmarks_outline_level = None
        self._create_missing_outline_levels = None
        self._create_outlines_for_headings_in_tables = None
        self._expanded_outline_levels = None
        self._headings_outline_levels = None
        self.discriminator = None

        if bookmarks_outline_levels is not None:
            self.bookmarks_outline_levels = bookmarks_outline_levels
        if default_bookmarks_outline_level is not None:
            self.default_bookmarks_outline_level = default_bookmarks_outline_level
        if create_missing_outline_levels is not None:
            self.create_missing_outline_levels = create_missing_outline_levels
        if create_outlines_for_headings_in_tables is not None:
            self.create_outlines_for_headings_in_tables = create_outlines_for_headings_in_tables
        if expanded_outline_levels is not None:
            self.expanded_outline_levels = expanded_outline_levels
        if headings_outline_levels is not None:
            self.headings_outline_levels = headings_outline_levels

    @property
    def bookmarks_outline_levels(self):
        """Gets the bookmarks_outline_levels of this OutlineOptionsData.  # noqa: E501

        Gets or sets allows to specify individual bookmarks outline level.  # noqa: E501

        :return: The bookmarks_outline_levels of this OutlineOptionsData.  # noqa: E501
        :rtype: list[BookmarksOutlineLevelData]
        """
        return self._bookmarks_outline_levels

    @bookmarks_outline_levels.setter
    def bookmarks_outline_levels(self, bookmarks_outline_levels):
        """Sets the bookmarks_outline_levels of this OutlineOptionsData.

        Gets or sets allows to specify individual bookmarks outline level.  # noqa: E501

        :param bookmarks_outline_levels: The bookmarks_outline_levels of this OutlineOptionsData.  # noqa: E501
        :type: list[BookmarksOutlineLevelData]
        """
        self._bookmarks_outline_levels = bookmarks_outline_levels
    @property
    def default_bookmarks_outline_level(self):
        """Gets the default_bookmarks_outline_level of this OutlineOptionsData.  # noqa: E501

        Gets or sets specifies the default level in the document outline at which to display Word bookmarks.  # noqa: E501

        :return: The default_bookmarks_outline_level of this OutlineOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._default_bookmarks_outline_level

    @default_bookmarks_outline_level.setter
    def default_bookmarks_outline_level(self, default_bookmarks_outline_level):
        """Sets the default_bookmarks_outline_level of this OutlineOptionsData.

        Gets or sets specifies the default level in the document outline at which to display Word bookmarks.  # noqa: E501

        :param default_bookmarks_outline_level: The default_bookmarks_outline_level of this OutlineOptionsData.  # noqa: E501
        :type: int
        """
        self._default_bookmarks_outline_level = default_bookmarks_outline_level
    @property
    def create_missing_outline_levels(self):
        """Gets the create_missing_outline_levels of this OutlineOptionsData.  # noqa: E501

        Gets or sets a value determining whether or not to create missing outline levels     when the document is exported.     Default value for this property is false.  # noqa: E501

        :return: The create_missing_outline_levels of this OutlineOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._create_missing_outline_levels

    @create_missing_outline_levels.setter
    def create_missing_outline_levels(self, create_missing_outline_levels):
        """Sets the create_missing_outline_levels of this OutlineOptionsData.

        Gets or sets a value determining whether or not to create missing outline levels     when the document is exported.     Default value for this property is false.  # noqa: E501

        :param create_missing_outline_levels: The create_missing_outline_levels of this OutlineOptionsData.  # noqa: E501
        :type: bool
        """
        self._create_missing_outline_levels = create_missing_outline_levels
    @property
    def create_outlines_for_headings_in_tables(self):
        """Gets the create_outlines_for_headings_in_tables of this OutlineOptionsData.  # noqa: E501

        Gets or sets specifies whether or not to create outlines for headings (paragraphs formatted     with the Heading styles) inside tables.  # noqa: E501

        :return: The create_outlines_for_headings_in_tables of this OutlineOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._create_outlines_for_headings_in_tables

    @create_outlines_for_headings_in_tables.setter
    def create_outlines_for_headings_in_tables(self, create_outlines_for_headings_in_tables):
        """Sets the create_outlines_for_headings_in_tables of this OutlineOptionsData.

        Gets or sets specifies whether or not to create outlines for headings (paragraphs formatted     with the Heading styles) inside tables.  # noqa: E501

        :param create_outlines_for_headings_in_tables: The create_outlines_for_headings_in_tables of this OutlineOptionsData.  # noqa: E501
        :type: bool
        """
        self._create_outlines_for_headings_in_tables = create_outlines_for_headings_in_tables
    @property
    def expanded_outline_levels(self):
        """Gets the expanded_outline_levels of this OutlineOptionsData.  # noqa: E501

        Gets or sets specifies how many levels in the document outline to show expanded when the file is viewed.  # noqa: E501

        :return: The expanded_outline_levels of this OutlineOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._expanded_outline_levels

    @expanded_outline_levels.setter
    def expanded_outline_levels(self, expanded_outline_levels):
        """Sets the expanded_outline_levels of this OutlineOptionsData.

        Gets or sets specifies how many levels in the document outline to show expanded when the file is viewed.  # noqa: E501

        :param expanded_outline_levels: The expanded_outline_levels of this OutlineOptionsData.  # noqa: E501
        :type: int
        """
        self._expanded_outline_levels = expanded_outline_levels
    @property
    def headings_outline_levels(self):
        """Gets the headings_outline_levels of this OutlineOptionsData.  # noqa: E501

        Gets or sets specifies how many levels of headings (paragraphs formatted with the Heading styles) to include in the document outline.  # noqa: E501

        :return: The headings_outline_levels of this OutlineOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._headings_outline_levels

    @headings_outline_levels.setter
    def headings_outline_levels(self, headings_outline_levels):
        """Sets the headings_outline_levels of this OutlineOptionsData.

        Gets or sets specifies how many levels of headings (paragraphs formatted with the Heading styles) to include in the document outline.  # noqa: E501

        :param headings_outline_levels: The headings_outline_levels of this OutlineOptionsData.  # noqa: E501
        :type: int
        """
        self._headings_outline_levels = headings_outline_levels
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
        if not isinstance(other, OutlineOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
