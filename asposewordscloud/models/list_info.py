# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="list_info.py">
#   Copyright (c) 2023 Aspose.Words for Cloud
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

class ListInfo(object):
    """DTO container with a single document list.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'link': 'WordsApiLink',
        'is_list_style_definition': 'bool',
        'is_list_style_reference': 'bool',
        'is_multi_level': 'bool',
        'is_restart_at_each_section': 'bool',
        'list_id': 'int',
        'list_levels': 'ListLevels',
        'style': 'Style'
    }

    attribute_map = {
        'link': 'Link',
        'is_list_style_definition': 'IsListStyleDefinition',
        'is_list_style_reference': 'IsListStyleReference',
        'is_multi_level': 'IsMultiLevel',
        'is_restart_at_each_section': 'IsRestartAtEachSection',
        'list_id': 'ListId',
        'list_levels': 'ListLevels',
        'style': 'Style'
    }

    def __init__(self, link=None, is_list_style_definition=None, is_list_style_reference=None, is_multi_level=None, is_restart_at_each_section=None, list_id=None, list_levels=None, style=None):  # noqa: E501
        """ListInfo - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._is_list_style_definition = None
        self._is_list_style_reference = None
        self._is_multi_level = None
        self._is_restart_at_each_section = None
        self._list_id = None
        self._list_levels = None
        self._style = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if is_list_style_definition is not None:
            self.is_list_style_definition = is_list_style_definition
        if is_list_style_reference is not None:
            self.is_list_style_reference = is_list_style_reference
        if is_multi_level is not None:
            self.is_multi_level = is_multi_level
        if is_restart_at_each_section is not None:
            self.is_restart_at_each_section = is_restart_at_each_section
        if list_id is not None:
            self.list_id = list_id
        if list_levels is not None:
            self.list_levels = list_levels
        if style is not None:
            self.style = style

    @property
    def link(self):
        """Gets the link of this ListInfo.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The link of this ListInfo.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this ListInfo.

        Gets or sets the link to the document.  # noqa: E501

        :param link: The link of this ListInfo.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link

    @property
    def is_list_style_definition(self):
        """Gets the is_list_style_definition of this ListInfo.  # noqa: E501

        Gets or sets a value indicating whether this list is a definition of a list style.  # noqa: E501

        :return: The is_list_style_definition of this ListInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_list_style_definition

    @is_list_style_definition.setter
    def is_list_style_definition(self, is_list_style_definition):
        """Sets the is_list_style_definition of this ListInfo.

        Gets or sets a value indicating whether this list is a definition of a list style.  # noqa: E501

        :param is_list_style_definition: The is_list_style_definition of this ListInfo.  # noqa: E501
        :type: bool
        """
        self._is_list_style_definition = is_list_style_definition

    @property
    def is_list_style_reference(self):
        """Gets the is_list_style_reference of this ListInfo.  # noqa: E501

        Gets or sets a value indicating whether this list is a reference to a list style.  # noqa: E501

        :return: The is_list_style_reference of this ListInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_list_style_reference

    @is_list_style_reference.setter
    def is_list_style_reference(self, is_list_style_reference):
        """Sets the is_list_style_reference of this ListInfo.

        Gets or sets a value indicating whether this list is a reference to a list style.  # noqa: E501

        :param is_list_style_reference: The is_list_style_reference of this ListInfo.  # noqa: E501
        :type: bool
        """
        self._is_list_style_reference = is_list_style_reference

    @property
    def is_multi_level(self):
        """Gets the is_multi_level of this ListInfo.  # noqa: E501

        Gets or sets a value indicating whether the list contains 9 levels; false when 1 level.  # noqa: E501

        :return: The is_multi_level of this ListInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_multi_level

    @is_multi_level.setter
    def is_multi_level(self, is_multi_level):
        """Sets the is_multi_level of this ListInfo.

        Gets or sets a value indicating whether the list contains 9 levels; false when 1 level.  # noqa: E501

        :param is_multi_level: The is_multi_level of this ListInfo.  # noqa: E501
        :type: bool
        """
        self._is_multi_level = is_multi_level

    @property
    def is_restart_at_each_section(self):
        """Gets the is_restart_at_each_section of this ListInfo.  # noqa: E501

        Gets or sets a value indicating whether list should be restarted at each section. The default value is false.  # noqa: E501

        :return: The is_restart_at_each_section of this ListInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_restart_at_each_section

    @is_restart_at_each_section.setter
    def is_restart_at_each_section(self, is_restart_at_each_section):
        """Sets the is_restart_at_each_section of this ListInfo.

        Gets or sets a value indicating whether list should be restarted at each section. The default value is false.  # noqa: E501

        :param is_restart_at_each_section: The is_restart_at_each_section of this ListInfo.  # noqa: E501
        :type: bool
        """
        self._is_restart_at_each_section = is_restart_at_each_section

    @property
    def list_id(self):
        """Gets the list_id of this ListInfo.  # noqa: E501

        Gets or sets the unique identifier of the list.  # noqa: E501

        :return: The list_id of this ListInfo.  # noqa: E501
        :rtype: int
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this ListInfo.

        Gets or sets the unique identifier of the list.  # noqa: E501

        :param list_id: The list_id of this ListInfo.  # noqa: E501
        :type: int
        """
        self._list_id = list_id

    @property
    def list_levels(self):
        """Gets the list_levels of this ListInfo.  # noqa: E501

        Gets or sets the collection of list levels for this list.  # noqa: E501

        :return: The list_levels of this ListInfo.  # noqa: E501
        :rtype: ListLevels
        """
        return self._list_levels

    @list_levels.setter
    def list_levels(self, list_levels):
        """Sets the list_levels of this ListInfo.

        Gets or sets the collection of list levels for this list.  # noqa: E501

        :param list_levels: The list_levels of this ListInfo.  # noqa: E501
        :type: ListLevels
        """
        self._list_levels = list_levels

    @property
    def style(self):
        """Gets the style of this ListInfo.  # noqa: E501

        Gets or sets the list style that this list references or defines.  # noqa: E501

        :return: The style of this ListInfo.  # noqa: E501
        :rtype: Style
        """
        return self._style

    @style.setter
    def style(self, style):
        """Sets the style of this ListInfo.

        Gets or sets the list style that this list references or defines.  # noqa: E501

        :param style: The style of this ListInfo.  # noqa: E501
        :type: Style
        """
        self._style = style


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

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
        if not isinstance(other, ListInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other