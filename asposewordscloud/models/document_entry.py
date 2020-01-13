# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="DocumentEntry.py">
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


class DocumentEntry(object):
    """Represents a document which will be appended to the original resource document.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'href': 'str',
        'import_format_mode': 'str'
    }

    attribute_map = {
        'href': 'Href',
        'import_format_mode': 'ImportFormatMode'
    }

    def __init__(self, href=None, import_format_mode=None):  # noqa: E501
        """DocumentEntry - a model defined in Swagger"""  # noqa: E501

        self._href = None
        self._import_format_mode = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if import_format_mode is not None:
            self.import_format_mode = import_format_mode

    @property
    def href(self):
        """Gets the href of this DocumentEntry.  # noqa: E501

        Gets or sets path to document to append at the server.  # noqa: E501

        :return: The href of this DocumentEntry.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this DocumentEntry.

        Gets or sets path to document to append at the server.  # noqa: E501

        :param href: The href of this DocumentEntry.  # noqa: E501
        :type: str
        """
        self._href = href
    @property
    def import_format_mode(self):
        """Gets the import_format_mode of this DocumentEntry.  # noqa: E501

        Gets or sets defines which formatting will be used: appended or destination document.Can be KeepSourceFormatting or UseDestinationStyles.  # noqa: E501

        :return: The import_format_mode of this DocumentEntry.  # noqa: E501
        :rtype: str
        """
        return self._import_format_mode

    @import_format_mode.setter
    def import_format_mode(self, import_format_mode):
        """Sets the import_format_mode of this DocumentEntry.

        Gets or sets defines which formatting will be used: appended or destination document.Can be KeepSourceFormatting or UseDestinationStyles.  # noqa: E501

        :param import_format_mode: The import_format_mode of this DocumentEntry.  # noqa: E501
        :type: str
        """
        self._import_format_mode = import_format_mode
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
        if not isinstance(other, DocumentEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
