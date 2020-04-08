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
        'drawing_object': 'str',
        'image_file': 'str'
    }

    attribute_map = {
        'drawing_object': 'drawingObject',
        'image_file': 'imageFile'
    }

    def __init__(self, drawing_object=None, image_file=None):  # noqa: E501
        """Body8 - a model defined in Swagger"""  # noqa: E501

        self._drawing_object = None
        self._image_file = None
        self.discriminator = None

        if drawing_object is not None:
            self.drawing_object = drawing_object
        if image_file is not None:
            self.image_file = image_file

    @property
    def drawing_object(self):
        """Gets the drawing_object of this Body8.  # noqa: E501

        Drawing object parameters  # noqa: E501

        :return: The drawing_object of this Body8.  # noqa: E501
        :rtype: str
        """
        return self._drawing_object

    @drawing_object.setter
    def drawing_object(self, drawing_object):
        """Sets the drawing_object of this Body8.

        Drawing object parameters  # noqa: E501

        :param drawing_object: The drawing_object of this Body8.  # noqa: E501
        :type: str
        """
        if drawing_object is None:
            raise ValueError("Invalid value for `drawing_object`, must not be `None`")  # noqa: E501
        self._drawing_object = drawing_object
    @property
    def image_file(self):
        """Gets the image_file of this Body8.  # noqa: E501

        File with image  # noqa: E501

        :return: The image_file of this Body8.  # noqa: E501
        :rtype: str
        """
        return self._image_file

    @image_file.setter
    def image_file(self, image_file):
        """Sets the image_file of this Body8.

        File with image  # noqa: E501

        :param image_file: The image_file of this Body8.  # noqa: E501
        :type: str
        """
        if image_file is None:
            raise ValueError("Invalid value for `image_file`, must not be `None`")  # noqa: E501
        self._image_file = image_file
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
