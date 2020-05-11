# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="ReportEngineSettings.py">
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


class ReportEngineSettings(object):
    """Report engine settings.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'data_source_type': 'str',
        'report_build_options': 'list[ReportBuildOptions]',
        'data_source_name': 'str',
        'csv_data_load_options': 'CsvDataLoadOptions'
    }

    attribute_map = {
        'data_source_type': 'DataSourceType',
        'report_build_options': 'ReportBuildOptions',
        'data_source_name': 'DataSourceName',
        'csv_data_load_options': 'CsvDataLoadOptions'
    }

    def __init__(self, data_source_type=None, report_build_options=None, data_source_name=None, csv_data_load_options=None):  # noqa: E501
        """ReportEngineSettings - a model defined in Swagger"""  # noqa: E501

        self._data_source_type = None
        self._report_build_options = None
        self._data_source_name = None
        self._csv_data_load_options = None
        self.discriminator = None

        if data_source_type is not None:
            self.data_source_type = data_source_type
        if report_build_options is not None:
            self.report_build_options = report_build_options
        if data_source_name is not None:
            self.data_source_name = data_source_name
        if csv_data_load_options is not None:
            self.csv_data_load_options = csv_data_load_options

    @property
    def data_source_type(self):
        """Gets the data_source_type of this ReportEngineSettings.  # noqa: E501

        Gets or sets type of datasource.  # noqa: E501

        :return: The data_source_type of this ReportEngineSettings.  # noqa: E501
        :rtype: str
        """
        return self._data_source_type

    @data_source_type.setter
    def data_source_type(self, data_source_type):
        """Sets the data_source_type of this ReportEngineSettings.

        Gets or sets type of datasource.  # noqa: E501

        :param data_source_type: The data_source_type of this ReportEngineSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["Xml", "Json", "Csv"]  # noqa: E501
        if not data_source_type.isdigit():	
            if data_source_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `data_source_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(data_source_type, allowed_values))
            self._data_source_type = data_source_type
        else:
            self._data_source_type = allowed_values[int(data_source_type) if six.PY3 else long(data_source_type)]
    @property
    def report_build_options(self):
        """Gets the report_build_options of this ReportEngineSettings.  # noqa: E501

        Gets or sets type of options to build report.  # noqa: E501

        :return: The report_build_options of this ReportEngineSettings.  # noqa: E501
        :rtype: list[ReportBuildOptions]
        """
        return self._report_build_options

    @report_build_options.setter
    def report_build_options(self, report_build_options):
        """Sets the report_build_options of this ReportEngineSettings.

        Gets or sets type of options to build report.  # noqa: E501

        :param report_build_options: The report_build_options of this ReportEngineSettings.  # noqa: E501
        :type: list[ReportBuildOptions]
        """
        self._report_build_options = report_build_options
    @property
    def data_source_name(self):
        """Gets the data_source_name of this ReportEngineSettings.  # noqa: E501

        Gets or sets a name to reference the data source object in the template.  # noqa: E501

        :return: The data_source_name of this ReportEngineSettings.  # noqa: E501
        :rtype: str
        """
        return self._data_source_name

    @data_source_name.setter
    def data_source_name(self, data_source_name):
        """Sets the data_source_name of this ReportEngineSettings.

        Gets or sets a name to reference the data source object in the template.  # noqa: E501

        :param data_source_name: The data_source_name of this ReportEngineSettings.  # noqa: E501
        :type: str
        """
        self._data_source_name = data_source_name
    @property
    def csv_data_load_options(self):
        """Gets the csv_data_load_options of this ReportEngineSettings.  # noqa: E501

        Gets or sets csv_data_load_options.  # noqa: E501

        :return: The csv_data_load_options of this ReportEngineSettings.  # noqa: E501
        :rtype: CsvDataLoadOptions
        """
        return self._csv_data_load_options

    @csv_data_load_options.setter
    def csv_data_load_options(self, csv_data_load_options):
        """Sets the csv_data_load_options of this ReportEngineSettings.

        Gets or sets csv_data_load_options.  # noqa: E501

        :param csv_data_load_options: The csv_data_load_options of this ReportEngineSettings.  # noqa: E501
        :type: CsvDataLoadOptions
        """
        self._csv_data_load_options = csv_data_load_options
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
        if not isinstance(other, ReportEngineSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other