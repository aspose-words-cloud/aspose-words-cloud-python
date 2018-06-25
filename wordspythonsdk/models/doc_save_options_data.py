# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="DocSaveOptionsData.py">
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


class DocSaveOptionsData(object):
    """container class for doc/dot save options
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'password': 'str',
        'save_routing_slip': 'bool'
    }

    attribute_map = {
        'password': 'Password',
        'save_routing_slip': 'SaveRoutingSlip'
    }

    def __init__(self, password=None, save_routing_slip=None):  # noqa: E501
        """DocSaveOptionsData - a model defined in Swagger"""  # noqa: E501

        self._password = None
        self._save_routing_slip = None
        self.discriminator = None

        if password is not None:
            self.password = password
        if save_routing_slip is not None:
            self.save_routing_slip = save_routing_slip

    @property
    def password(self):
        """Gets the password of this DocSaveOptionsData.  # noqa: E501

        Password  # noqa: E501

        :return: The password of this DocSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this DocSaveOptionsData.

        Password  # noqa: E501

        :param password: The password of this DocSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def save_routing_slip(self):
        """Gets the save_routing_slip of this DocSaveOptionsData.  # noqa: E501

        Determine whether or not save RoutingSlip data saved to output document  # noqa: E501

        :return: The save_routing_slip of this DocSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._save_routing_slip

    @save_routing_slip.setter
    def save_routing_slip(self, save_routing_slip):
        """Sets the save_routing_slip of this DocSaveOptionsData.

        Determine whether or not save RoutingSlip data saved to output document  # noqa: E501

        :param save_routing_slip: The save_routing_slip of this DocSaveOptionsData.  # noqa: E501
        :type: bool
        """

        self._save_routing_slip = save_routing_slip

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
        if not isinstance(other, DocSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
