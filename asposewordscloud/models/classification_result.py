# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="classification_result.py">
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

class ClassificationResult(object):
    """Represents a single classification result.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'class_name': 'str',
        'class_probability': 'float'
    }

    attribute_map = {
        'class_name': 'ClassName',
        'class_probability': 'ClassProbability'
    }

    def __init__(self, class_name=None, class_probability=None):  # noqa: E501
        """ClassificationResult - a model defined in Swagger"""  # noqa: E501

        self._class_name = None
        self._class_probability = None
        self.discriminator = None

        if class_name is not None:
            self.class_name = class_name
        if class_probability is not None:
            self.class_probability = class_probability

    @property
    def class_name(self):
        """Gets the class_name of this ClassificationResult.  # noqa: E501

        Gets or sets the name of the class.  # noqa: E501

        :return: The class_name of this ClassificationResult.  # noqa: E501
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this ClassificationResult.

        Gets or sets the name of the class.  # noqa: E501

        :param class_name: The class_name of this ClassificationResult.  # noqa: E501
        :type: str
        """
        self._class_name = class_name

    @property
    def class_probability(self):
        """Gets the class_probability of this ClassificationResult.  # noqa: E501

        Gets or sets the probability of class.  # noqa: E501

        :return: The class_probability of this ClassificationResult.  # noqa: E501
        :rtype: float
        """
        return self._class_probability

    @class_probability.setter
    def class_probability(self, class_probability):
        """Sets the class_probability of this ClassificationResult.

        Gets or sets the probability of class.  # noqa: E501

        :param class_probability: The class_probability of this ClassificationResult.  # noqa: E501
        :type: float
        """
        self._class_probability = class_probability


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
        if not isinstance(other, ClassificationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other