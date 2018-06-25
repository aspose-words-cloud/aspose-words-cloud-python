# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="PclSaveOptionsData.py">
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


class PclSaveOptionsData(object):
    """Container class for pcl save options
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'falllback_font_name': 'str',
        'rasterize_transformed_elements': 'bool'
    }

    attribute_map = {
        'falllback_font_name': 'FalllbackFontName',
        'rasterize_transformed_elements': 'RasterizeTransformedElements'
    }

    def __init__(self, falllback_font_name=None, rasterize_transformed_elements=None):  # noqa: E501
        """PclSaveOptionsData - a model defined in Swagger"""  # noqa: E501

        self._falllback_font_name = None
        self._rasterize_transformed_elements = None
        self.discriminator = None

        if falllback_font_name is not None:
            self.falllback_font_name = falllback_font_name
        if rasterize_transformed_elements is not None:
            self.rasterize_transformed_elements = rasterize_transformed_elements

    @property
    def falllback_font_name(self):
        """Gets the falllback_font_name of this PclSaveOptionsData.  # noqa: E501

        Name of the font that will be used if no expected font is found in printer and built-in fonts collections.  # noqa: E501

        :return: The falllback_font_name of this PclSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._falllback_font_name

    @falllback_font_name.setter
    def falllback_font_name(self, falllback_font_name):
        """Sets the falllback_font_name of this PclSaveOptionsData.

        Name of the font that will be used if no expected font is found in printer and built-in fonts collections.  # noqa: E501

        :param falllback_font_name: The falllback_font_name of this PclSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._falllback_font_name = falllback_font_name

    @property
    def rasterize_transformed_elements(self):
        """Gets the rasterize_transformed_elements of this PclSaveOptionsData.  # noqa: E501

        Gets or sets a value determining whether or not complex transformed elements should be rasterized before saving to PCL document.  Default is true.  # noqa: E501

        :return: The rasterize_transformed_elements of this PclSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._rasterize_transformed_elements

    @rasterize_transformed_elements.setter
    def rasterize_transformed_elements(self, rasterize_transformed_elements):
        """Sets the rasterize_transformed_elements of this PclSaveOptionsData.

        Gets or sets a value determining whether or not complex transformed elements should be rasterized before saving to PCL document.  Default is true.  # noqa: E501

        :param rasterize_transformed_elements: The rasterize_transformed_elements of this PclSaveOptionsData.  # noqa: E501
        :type: bool
        """

        self._rasterize_transformed_elements = rasterize_transformed_elements

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
        if not isinstance(other, PclSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
