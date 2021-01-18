# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="field.py">
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


class Field(object):
    """DTO container with a field.
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
        'field_code': 'str',
        'locale_id': 'str',
        'result': 'str'
    }

    attribute_map = {
        'link': 'Link',
        'node_id': 'NodeId',
        'field_code': 'FieldCode',
        'locale_id': 'LocaleId',
        'result': 'Result'
    }

    def __init__(self, link=None, node_id=None, field_code=None, locale_id=None, result=None):  # noqa: E501
        """Field - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._node_id = None
        self._field_code = None
        self._locale_id = None
        self._result = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if node_id is not None:
            self.node_id = node_id
        if field_code is not None:
            self.field_code = field_code
        if locale_id is not None:
            self.locale_id = locale_id
        if result is not None:
            self.result = result

    @property
    def link(self):
        """Gets the link of this Field.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The link of this Field.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this Field.

        Gets or sets the link to the document.  # noqa: E501

        :param link: The link of this Field.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link

    @property
    def node_id(self):
        """Gets the node_id of this Field.  # noqa: E501

        Gets or sets the node id.  # noqa: E501

        :return: The node_id of this Field.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this Field.

        Gets or sets the node id.  # noqa: E501

        :param node_id: The node_id of this Field.  # noqa: E501
        :type: str
        """
        self._node_id = node_id

    @property
    def field_code(self):
        """Gets the field_code of this Field.  # noqa: E501

        Gets or sets the field code.  # noqa: E501

        :return: The field_code of this Field.  # noqa: E501
        :rtype: str
        """
        return self._field_code

    @field_code.setter
    def field_code(self, field_code):
        """Sets the field_code of this Field.

        Gets or sets the field code.  # noqa: E501

        :param field_code: The field_code of this Field.  # noqa: E501
        :type: str
        """
        self._field_code = field_code

    @property
    def locale_id(self):
        """Gets the locale_id of this Field.  # noqa: E501

        Gets or sets the LCID of the field.  # noqa: E501

        :return: The locale_id of this Field.  # noqa: E501
        :rtype: str
        """
        return self._locale_id

    @locale_id.setter
    def locale_id(self, locale_id):
        """Sets the locale_id of this Field.

        Gets or sets the LCID of the field.  # noqa: E501

        :param locale_id: The locale_id of this Field.  # noqa: E501
        :type: str
        """
        self._locale_id = locale_id

    @property
    def result(self):
        """Gets the result of this Field.  # noqa: E501

        Gets or sets the field result.  # noqa: E501

        :return: The result of this Field.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this Field.

        Gets or sets the field result.  # noqa: E501

        :param result: The result of this Field.  # noqa: E501
        :type: str
        """
        self._result = result


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
        if not isinstance(other, Field):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other