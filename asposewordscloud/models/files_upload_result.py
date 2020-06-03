# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="FilesUploadResult.py">
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


class FilesUploadResult(object):
    """File upload result
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'uploaded': 'list[str]',
        'errors': 'list[Error]'
    }

    attribute_map = {
        'uploaded': 'Uploaded',
        'errors': 'Errors'
    }

    def __init__(self, uploaded=None, errors=None):  # noqa: E501
        """FilesUploadResult - a model defined in Swagger"""  # noqa: E501

        self._uploaded = None
        self._errors = None
        self.discriminator = None

        if uploaded is not None:
            self.uploaded = uploaded
        if errors is not None:
            self.errors = errors

    @property
    def uploaded(self):
        """Gets the uploaded of this FilesUploadResult.  # noqa: E501

        List of uploaded file names  # noqa: E501

        :return: The uploaded of this FilesUploadResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._uploaded

    @uploaded.setter
    def uploaded(self, uploaded):
        """Sets the uploaded of this FilesUploadResult.

        List of uploaded file names  # noqa: E501

        :param uploaded: The uploaded of this FilesUploadResult.  # noqa: E501
        :type: list[str]
        """
        self._uploaded = uploaded
    @property
    def errors(self):
        """Gets the errors of this FilesUploadResult.  # noqa: E501

        List of errors.  # noqa: E501

        :return: The errors of this FilesUploadResult.  # noqa: E501
        :rtype: list[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this FilesUploadResult.

        List of errors.  # noqa: E501

        :param errors: The errors of this FilesUploadResult.  # noqa: E501
        :type: list[Error]
        """
        self._errors = errors
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
        if not isinstance(other, FilesUploadResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
