# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="compare_data.py">
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

class CompareData(object):
    """Container class for compare documents.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'author': 'str',
        'compare_options': 'CompareOptions',
        'comparing_with_document': 'str',
        'date_time': 'datetime',
        'result_document_format': 'str'
    }

    attribute_map = {
        'author': 'Author',
        'compare_options': 'CompareOptions',
        'comparing_with_document': 'ComparingWithDocument',
        'date_time': 'DateTime',
        'result_document_format': 'ResultDocumentFormat'
    }

    def __init__(self, author=None, compare_options=None, comparing_with_document=None, date_time=None, result_document_format=None):  # noqa: E501
        """CompareData - a model defined in Swagger"""  # noqa: E501

        self._author = None
        self._compare_options = None
        self._comparing_with_document = None
        self._date_time = None
        self._result_document_format = None
        self.discriminator = None

        if author is not None:
            self.author = author
        if compare_options is not None:
            self.compare_options = compare_options
        if comparing_with_document is not None:
            self.comparing_with_document = comparing_with_document
        if date_time is not None:
            self.date_time = date_time
        if result_document_format is not None:
            self.result_document_format = result_document_format

    @property
    def author(self):
        """Gets the author of this CompareData.  # noqa: E501

        Gets or sets the initials of the author to use for revisions.  # noqa: E501

        :return: The author of this CompareData.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this CompareData.

        Gets or sets the initials of the author to use for revisions.  # noqa: E501

        :param author: The author of this CompareData.  # noqa: E501
        :type: str
        """
        self._author = author

    @property
    def compare_options(self):
        """Gets the compare_options of this CompareData.  # noqa: E501

        Gets or sets the compare options.  # noqa: E501

        :return: The compare_options of this CompareData.  # noqa: E501
        :rtype: CompareOptions
        """
        return self._compare_options

    @compare_options.setter
    def compare_options(self, compare_options):
        """Sets the compare_options of this CompareData.

        Gets or sets the compare options.  # noqa: E501

        :param compare_options: The compare_options of this CompareData.  # noqa: E501
        :type: CompareOptions
        """
        self._compare_options = compare_options

    @property
    def comparing_with_document(self):
        """Gets the comparing_with_document of this CompareData.  # noqa: E501

        Gets or sets the path to document to compare at the server.  # noqa: E501

        :return: The comparing_with_document of this CompareData.  # noqa: E501
        :rtype: str
        """
        return self._comparing_with_document

    @comparing_with_document.setter
    def comparing_with_document(self, comparing_with_document):
        """Sets the comparing_with_document of this CompareData.

        Gets or sets the path to document to compare at the server.  # noqa: E501

        :param comparing_with_document: The comparing_with_document of this CompareData.  # noqa: E501
        :type: str
        """
        self._comparing_with_document = comparing_with_document

    @property
    def date_time(self):
        """Gets the date_time of this CompareData.  # noqa: E501

        Gets or sets the date and time to use for revisions.  # noqa: E501

        :return: The date_time of this CompareData.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this CompareData.

        Gets or sets the date and time to use for revisions.  # noqa: E501

        :param date_time: The date_time of this CompareData.  # noqa: E501
        :type: datetime
        """
        self._date_time = date_time

    @property
    def result_document_format(self):
        """Gets the result_document_format of this CompareData.  # noqa: E501

        Gets or sets the result document format.  # noqa: E501

        :return: The result_document_format of this CompareData.  # noqa: E501
        :rtype: str
        """
        return self._result_document_format

    @result_document_format.setter
    def result_document_format(self, result_document_format):
        """Sets the result_document_format of this CompareData.

        Gets or sets the result document format.  # noqa: E501

        :param result_document_format: The result_document_format of this CompareData.  # noqa: E501
        :type: str
        """
        self._result_document_format = result_document_format


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
        if not isinstance(other, CompareData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other