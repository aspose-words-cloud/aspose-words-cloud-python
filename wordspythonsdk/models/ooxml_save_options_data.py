# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="OoxmlSaveOptionsData.py">
#   Copyright (c) 2018 Aspose.Words for Cloud
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


class OoxmlSaveOptionsData(object):
    """container class for docx/docm/dotx/dotm/flatopc save options
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'compliance': 'str',
        'password': 'str',
        'pretty_format': 'bool'
    }

    attribute_map = {
        'compliance': 'Compliance',
        'password': 'Password',
        'pretty_format': 'PrettyFormat'
    }

    def __init__(self, compliance=None, password=None, pretty_format=None):  # noqa: E501
        """OoxmlSaveOptionsData - a model defined in Swagger"""  # noqa: E501

        self._compliance = None
        self._password = None
        self._pretty_format = None
        self.discriminator = None

        if compliance is not None:
            self.compliance = compliance
        if password is not None:
            self.password = password
        if pretty_format is not None:
            self.pretty_format = pretty_format

    @property
    def compliance(self):
        """Gets the compliance of this OoxmlSaveOptionsData.  # noqa: E501

        Specifies the OOXML version for the output document  # noqa: E501

        :return: The compliance of this OoxmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._compliance

    @compliance.setter
    def compliance(self, compliance):
        """Sets the compliance of this OoxmlSaveOptionsData.

        Specifies the OOXML version for the output document  # noqa: E501

        :param compliance: The compliance of this OoxmlSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._compliance = compliance

    @property
    def password(self):
        """Gets the password of this OoxmlSaveOptionsData.  # noqa: E501

        Specifies a password to encrypt document using ECMA376 Standard encryption algorithm  # noqa: E501

        :return: The password of this OoxmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this OoxmlSaveOptionsData.

        Specifies a password to encrypt document using ECMA376 Standard encryption algorithm  # noqa: E501

        :param password: The password of this OoxmlSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def pretty_format(self):
        """Gets the pretty_format of this OoxmlSaveOptionsData.  # noqa: E501

        Specifies whether or not use pretty formats output  # noqa: E501

        :return: The pretty_format of this OoxmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._pretty_format

    @pretty_format.setter
    def pretty_format(self, pretty_format):
        """Sets the pretty_format of this OoxmlSaveOptionsData.

        Specifies whether or not use pretty formats output  # noqa: E501

        :param pretty_format: The pretty_format of this OoxmlSaveOptionsData.  # noqa: E501
        :type: bool
        """

        self._pretty_format = pretty_format

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
        if not isinstance(other, OoxmlSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
