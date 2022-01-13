# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="custom_xml_part_update.py">
#   Copyright (c) 2022 Aspose.Words for Cloud
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


class CustomXmlPartUpdate(object):
    """Custom xml part update.
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
        'data': 'str',
        'id': 'str'
    }

    attribute_map = {
        'link': 'Link',
        'data': 'Data',
        'id': 'Id'
    }

    def __init__(self, link=None, data=None, id=None):  # noqa: E501
        """CustomXmlPartUpdate - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._data = None
        self._id = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if data is not None:
            self.data = data
        if id is not None:
            self.id = id

    @property
    def link(self):
        """Gets the link of this CustomXmlPartUpdate.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The link of this CustomXmlPartUpdate.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this CustomXmlPartUpdate.

        Gets or sets the link to the document.  # noqa: E501

        :param link: The link of this CustomXmlPartUpdate.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link

    @property
    def data(self):
        """Gets the data of this CustomXmlPartUpdate.  # noqa: E501

        Gets or sets the custom xml part data.  # noqa: E501

        :return: The data of this CustomXmlPartUpdate.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CustomXmlPartUpdate.

        Gets or sets the custom xml part data.  # noqa: E501

        :param data: The data of this CustomXmlPartUpdate.  # noqa: E501
        :type: str
        """
        self._data = data

    @property
    def id(self):
        """Gets the id of this CustomXmlPartUpdate.  # noqa: E501

        Gets or sets the custom xml part id.  # noqa: E501

        :return: The id of this CustomXmlPartUpdate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomXmlPartUpdate.

        Gets or sets the custom xml part id.  # noqa: E501

        :param id: The id of this CustomXmlPartUpdate.  # noqa: E501
        :type: str
        """
        self._id = id


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
        if not isinstance(other, CustomXmlPartUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other