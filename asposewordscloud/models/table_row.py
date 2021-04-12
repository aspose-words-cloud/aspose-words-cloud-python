# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="table_row.py">
#   Copyright (c) 2021 Aspose.Words for Cloud
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


class TableRow(object):
    """DTO container with a table row element.
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
        'node_id': 'str',
        'row_format': 'TableRowFormat',
        'table_cell_list': 'list[TableCell]'
    }

    attribute_map = {
        'link': 'Link',
        'node_id': 'NodeId',
        'row_format': 'RowFormat',
        'table_cell_list': 'TableCellList'
    }

    def __init__(self, link=None, node_id=None, row_format=None, table_cell_list=None):  # noqa: E501
        """TableRow - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._node_id = None
        self._row_format = None
        self._table_cell_list = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if node_id is not None:
            self.node_id = node_id
        if row_format is not None:
            self.row_format = row_format
        if table_cell_list is not None:
            self.table_cell_list = table_cell_list

    @property
    def link(self):
        """Gets the link of this TableRow.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The link of this TableRow.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this TableRow.

        Gets or sets the link to the document.  # noqa: E501

        :param link: The link of this TableRow.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link

    @property
    def node_id(self):
        """Gets the node_id of this TableRow.  # noqa: E501

        Gets or sets the node id.  # noqa: E501

        :return: The node_id of this TableRow.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this TableRow.

        Gets or sets the node id.  # noqa: E501

        :param node_id: The node_id of this TableRow.  # noqa: E501
        :type: str
        """
        self._node_id = node_id

    @property
    def row_format(self):
        """Gets the row_format of this TableRow.  # noqa: E501

        Gets or sets the formatting properties of a row.  # noqa: E501

        :return: The row_format of this TableRow.  # noqa: E501
        :rtype: TableRowFormat
        """
        return self._row_format

    @row_format.setter
    def row_format(self, row_format):
        """Sets the row_format of this TableRow.

        Gets or sets the formatting properties of a row.  # noqa: E501

        :param row_format: The row_format of this TableRow.  # noqa: E501
        :type: TableRowFormat
        """
        self._row_format = row_format

    @property
    def table_cell_list(self):
        """Gets the table_cell_list of this TableRow.  # noqa: E501

        Gets or sets the collection of rows.  # noqa: E501

        :return: The table_cell_list of this TableRow.  # noqa: E501
        :rtype: list[TableCell]
        """
        return self._table_cell_list

    @table_cell_list.setter
    def table_cell_list(self, table_cell_list):
        """Sets the table_cell_list of this TableRow.

        Gets or sets the collection of rows.  # noqa: E501

        :param table_cell_list: The table_cell_list of this TableRow.  # noqa: E501
        :type: list[TableCell]
        """
        self._table_cell_list = table_cell_list


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
        if not isinstance(other, TableRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other