# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="Body8.py">
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


class Body8(object):
    """Body8
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'template': 'str',
        'data': 'str',
        'report_engine_settings': 'ReportEngineSettings'
    }

    attribute_map = {
        'template': 'template',
        'data': 'data',
        'report_engine_settings': 'reportEngineSettings'
    }

    def __init__(self, template=None, data=None, report_engine_settings=None):  # noqa: E501
        """Body8 - a model defined in Swagger"""  # noqa: E501

        self._template = None
        self._data = None
        self._report_engine_settings = None
        self.discriminator = None

        if template is not None:
            self.template = template
        if data is not None:
            self.data = data
        if report_engine_settings is not None:
            self.report_engine_settings = report_engine_settings

    @property
    def template(self):
        """Gets the template of this Body8.  # noqa: E501

        File with template  # noqa: E501

        :return: The template of this Body8.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this Body8.

        File with template  # noqa: E501

        :param template: The template of this Body8.  # noqa: E501
        :type: str
        """
        if template is None:
            raise ValueError("Invalid value for `template`, must not be `None`")  # noqa: E501
        self._template = template
    @property
    def data(self):
        """Gets the data of this Body8.  # noqa: E501

        A string providing a data to populate the specified template. The string must be of one of the following types: xml, json, csv  # noqa: E501

        :return: The data of this Body8.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Body8.

        A string providing a data to populate the specified template. The string must be of one of the following types: xml, json, csv  # noqa: E501

        :param data: The data of this Body8.  # noqa: E501
        :type: str
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501
        self._data = data
    @property
    def report_engine_settings(self):
        """Gets the report_engine_settings of this Body8.  # noqa: E501

        Gets or sets report_engine_settings.  # noqa: E501

        :return: The report_engine_settings of this Body8.  # noqa: E501
        :rtype: ReportEngineSettings
        """
        return self._report_engine_settings

    @report_engine_settings.setter
    def report_engine_settings(self, report_engine_settings):
        """Sets the report_engine_settings of this Body8.

        Gets or sets report_engine_settings.  # noqa: E501

        :param report_engine_settings: The report_engine_settings of this Body8.  # noqa: E501
        :type: ReportEngineSettings
        """
        if report_engine_settings is None:
            raise ValueError("Invalid value for `report_engine_settings`, must not be `None`")  # noqa: E501
        self._report_engine_settings = report_engine_settings
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
        if not isinstance(other, Body8):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
