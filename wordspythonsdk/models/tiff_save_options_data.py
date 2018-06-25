# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="TiffSaveOptionsData.py">
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


class TiffSaveOptionsData(object):
    """Container class for tiff save options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'tiff_binarization_method': 'str',
        'tiff_compression': 'str'
    }

    attribute_map = {
        'tiff_binarization_method': 'TiffBinarizationMethod',
        'tiff_compression': 'TiffCompression'
    }

    def __init__(self, tiff_binarization_method=None, tiff_compression=None):  # noqa: E501
        """TiffSaveOptionsData - a model defined in Swagger"""  # noqa: E501

        self._tiff_binarization_method = None
        self._tiff_compression = None
        self.discriminator = None

        if tiff_binarization_method is not None:
            self.tiff_binarization_method = tiff_binarization_method
        if tiff_compression is not None:
            self.tiff_compression = tiff_compression

    @property
    def tiff_binarization_method(self):
        """Gets the tiff_binarization_method of this TiffSaveOptionsData.  # noqa: E501

        Specifies method used while converting images to 1 bpp format.  # noqa: E501

        :return: The tiff_binarization_method of this TiffSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._tiff_binarization_method

    @tiff_binarization_method.setter
    def tiff_binarization_method(self, tiff_binarization_method):
        """Sets the tiff_binarization_method of this TiffSaveOptionsData.

        Specifies method used while converting images to 1 bpp format.  # noqa: E501

        :param tiff_binarization_method: The tiff_binarization_method of this TiffSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._tiff_binarization_method = tiff_binarization_method

    @property
    def tiff_compression(self):
        """Gets the tiff_compression of this TiffSaveOptionsData.  # noqa: E501

        Type of compression.  # noqa: E501

        :return: The tiff_compression of this TiffSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._tiff_compression

    @tiff_compression.setter
    def tiff_compression(self, tiff_compression):
        """Sets the tiff_compression of this TiffSaveOptionsData.

        Type of compression.  # noqa: E501

        :param tiff_compression: The tiff_compression of this TiffSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._tiff_compression = tiff_compression

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
        if not isinstance(other, TiffSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
