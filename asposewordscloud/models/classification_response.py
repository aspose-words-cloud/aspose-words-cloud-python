# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="classification_response.py">
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

class ClassificationResponse(object):
    """The REST response with data on multi-class text classification.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'request_id': 'str',
        'best_class_name': 'str',
        'best_class_probability': 'float',
        'best_results': 'list[ClassificationResult]'
    }

    attribute_map = {
        'request_id': 'RequestId',
        'best_class_name': 'BestClassName',
        'best_class_probability': 'BestClassProbability',
        'best_results': 'BestResults'
    }

    def __init__(self, request_id=None, best_class_name=None, best_class_probability=None, best_results=None):  # noqa: E501
        """ClassificationResponse - a model defined in Swagger"""  # noqa: E501

        self._request_id = None
        self._best_class_name = None
        self._best_class_probability = None
        self._best_results = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if best_class_name is not None:
            self.best_class_name = best_class_name
        if best_class_probability is not None:
            self.best_class_probability = best_class_probability
        if best_results is not None:
            self.best_results = best_results

    @property
    def request_id(self):
        """Gets the request_id of this ClassificationResponse.  # noqa: E501

        Gets or sets the request Id.  # noqa: E501

        :return: The request_id of this ClassificationResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ClassificationResponse.

        Gets or sets the request Id.  # noqa: E501

        :param request_id: The request_id of this ClassificationResponse.  # noqa: E501
        :type: str
        """
        self._request_id = request_id

    @property
    def best_class_name(self):
        """Gets the best_class_name of this ClassificationResponse.  # noqa: E501

        Gets or sets the best class name.  # noqa: E501

        :return: The best_class_name of this ClassificationResponse.  # noqa: E501
        :rtype: str
        """
        return self._best_class_name

    @best_class_name.setter
    def best_class_name(self, best_class_name):
        """Sets the best_class_name of this ClassificationResponse.

        Gets or sets the best class name.  # noqa: E501

        :param best_class_name: The best_class_name of this ClassificationResponse.  # noqa: E501
        :type: str
        """
        self._best_class_name = best_class_name

    @property
    def best_class_probability(self):
        """Gets the best_class_probability of this ClassificationResponse.  # noqa: E501

        Gets or sets the best class probability.  # noqa: E501

        :return: The best_class_probability of this ClassificationResponse.  # noqa: E501
        :rtype: float
        """
        return self._best_class_probability

    @best_class_probability.setter
    def best_class_probability(self, best_class_probability):
        """Sets the best_class_probability of this ClassificationResponse.

        Gets or sets the best class probability.  # noqa: E501

        :param best_class_probability: The best_class_probability of this ClassificationResponse.  # noqa: E501
        :type: float
        """
        self._best_class_probability = best_class_probability

    @property
    def best_results(self):
        """Gets the best_results of this ClassificationResponse.  # noqa: E501

        Gets or sets the array of best classes results.  # noqa: E501

        :return: The best_results of this ClassificationResponse.  # noqa: E501
        :rtype: list[ClassificationResult]
        """
        return self._best_results

    @best_results.setter
    def best_results(self, best_results):
        """Sets the best_results of this ClassificationResponse.

        Gets or sets the array of best classes results.  # noqa: E501

        :param best_results: The best_results of this ClassificationResponse.  # noqa: E501
        :type: list[ClassificationResult]
        """
        self._best_results = best_results


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
        if not isinstance(other, ClassificationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other