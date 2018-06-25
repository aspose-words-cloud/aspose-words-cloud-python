# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="XamlFlowSaveOptionsData.py">
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


class XamlFlowSaveOptionsData(object):
    """container class for xaml flow save options
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'images_folder': 'str',
        'images_folder_alias': 'str'
    }

    attribute_map = {
        'images_folder': 'ImagesFolder',
        'images_folder_alias': 'ImagesFolderAlias'
    }

    def __init__(self, images_folder=None, images_folder_alias=None):  # noqa: E501
        """XamlFlowSaveOptionsData - a model defined in Swagger"""  # noqa: E501

        self._images_folder = None
        self._images_folder_alias = None
        self.discriminator = None

        if images_folder is not None:
            self.images_folder = images_folder
        if images_folder_alias is not None:
            self.images_folder_alias = images_folder_alias

    @property
    def images_folder(self):
        """Gets the images_folder of this XamlFlowSaveOptionsData.  # noqa: E501

        Specifies the physical folder where images are saved when exporting  # noqa: E501

        :return: The images_folder of this XamlFlowSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._images_folder

    @images_folder.setter
    def images_folder(self, images_folder):
        """Sets the images_folder of this XamlFlowSaveOptionsData.

        Specifies the physical folder where images are saved when exporting  # noqa: E501

        :param images_folder: The images_folder of this XamlFlowSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._images_folder = images_folder

    @property
    def images_folder_alias(self):
        """Gets the images_folder_alias of this XamlFlowSaveOptionsData.  # noqa: E501

        Specifies the name of the folder used to construct image URIs  # noqa: E501

        :return: The images_folder_alias of this XamlFlowSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._images_folder_alias

    @images_folder_alias.setter
    def images_folder_alias(self, images_folder_alias):
        """Sets the images_folder_alias of this XamlFlowSaveOptionsData.

        Specifies the name of the folder used to construct image URIs  # noqa: E501

        :param images_folder_alias: The images_folder_alias of this XamlFlowSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._images_folder_alias = images_folder_alias

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
        if not isinstance(other, XamlFlowSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
