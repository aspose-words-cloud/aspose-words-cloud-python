# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="GraphicsQualityOptionsData.py">
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


class GraphicsQualityOptionsData(object):
    """Allows to specify additional System.Drawing.Graphics quality options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'compositing_mode': 'str',
        'compositing_quality': 'str',
        'interpolation_mode': 'str',
        'smoothing_mode': 'str',
        'string_format': 'StringFormatData',
        'text_rendering_hint': 'str'
    }

    attribute_map = {
        'compositing_mode': 'CompositingMode',
        'compositing_quality': 'CompositingQuality',
        'interpolation_mode': 'InterpolationMode',
        'smoothing_mode': 'SmoothingMode',
        'string_format': 'StringFormat',
        'text_rendering_hint': 'TextRenderingHint'
    }

    def __init__(self, compositing_mode=None, compositing_quality=None, interpolation_mode=None, smoothing_mode=None, string_format=None, text_rendering_hint=None):  # noqa: E501
        """GraphicsQualityOptionsData - a model defined in Swagger"""  # noqa: E501

        self._compositing_mode = None
        self._compositing_quality = None
        self._interpolation_mode = None
        self._smoothing_mode = None
        self._string_format = None
        self._text_rendering_hint = None
        self.discriminator = None

        if compositing_mode is not None:
            self.compositing_mode = compositing_mode
        if compositing_quality is not None:
            self.compositing_quality = compositing_quality
        if interpolation_mode is not None:
            self.interpolation_mode = interpolation_mode
        if smoothing_mode is not None:
            self.smoothing_mode = smoothing_mode
        if string_format is not None:
            self.string_format = string_format
        if text_rendering_hint is not None:
            self.text_rendering_hint = text_rendering_hint

    @property
    def compositing_mode(self):
        """Gets the compositing_mode of this GraphicsQualityOptionsData.  # noqa: E501

        Gets or sets a value that specifies how composited images are drawn to this Graphics.  # noqa: E501

        :return: The compositing_mode of this GraphicsQualityOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._compositing_mode

    @compositing_mode.setter
    def compositing_mode(self, compositing_mode):
        """Sets the compositing_mode of this GraphicsQualityOptionsData.

        Gets or sets a value that specifies how composited images are drawn to this Graphics.  # noqa: E501

        :param compositing_mode: The compositing_mode of this GraphicsQualityOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["SourceOver", "SourceCopy"]  # noqa: E501
        if not compositing_mode.isdigit():	
            if compositing_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `compositing_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(compositing_mode, allowed_values))
            self._compositing_mode = compositing_mode
        else:
            self._compositing_mode = allowed_values[int(compositing_mode) if six.PY3 else long(compositing_mode)]
    @property
    def compositing_quality(self):
        """Gets the compositing_quality of this GraphicsQualityOptionsData.  # noqa: E501

        Gets or sets the rendering quality of composited images drawn to this Graphics.  # noqa: E501

        :return: The compositing_quality of this GraphicsQualityOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._compositing_quality

    @compositing_quality.setter
    def compositing_quality(self, compositing_quality):
        """Sets the compositing_quality of this GraphicsQualityOptionsData.

        Gets or sets the rendering quality of composited images drawn to this Graphics.  # noqa: E501

        :param compositing_quality: The compositing_quality of this GraphicsQualityOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Default", "HighSpeed", "HighQuality", "GammaCorrected", "AssumeLinear", "Invalid"]  # noqa: E501
        if not compositing_quality.isdigit():	
            if compositing_quality not in allowed_values:
                raise ValueError(
                    "Invalid value for `compositing_quality` ({0}), must be one of {1}"  # noqa: E501
                    .format(compositing_quality, allowed_values))
            self._compositing_quality = compositing_quality
        else:
            self._compositing_quality = allowed_values[int(compositing_quality) if six.PY3 else long(compositing_quality)]
    @property
    def interpolation_mode(self):
        """Gets the interpolation_mode of this GraphicsQualityOptionsData.  # noqa: E501

        Gets or sets the interpolation mode associated with this Graphics.  # noqa: E501

        :return: The interpolation_mode of this GraphicsQualityOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._interpolation_mode

    @interpolation_mode.setter
    def interpolation_mode(self, interpolation_mode):
        """Sets the interpolation_mode of this GraphicsQualityOptionsData.

        Gets or sets the interpolation mode associated with this Graphics.  # noqa: E501

        :param interpolation_mode: The interpolation_mode of this GraphicsQualityOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Default", "Low", "High", "Bilinear", "Bicubic", "NearestNeighbor", "HighQualityBilinear", "HighQualityBicubic", "Invalid"]  # noqa: E501
        if not interpolation_mode.isdigit():	
            if interpolation_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `interpolation_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(interpolation_mode, allowed_values))
            self._interpolation_mode = interpolation_mode
        else:
            self._interpolation_mode = allowed_values[int(interpolation_mode) if six.PY3 else long(interpolation_mode)]
    @property
    def smoothing_mode(self):
        """Gets the smoothing_mode of this GraphicsQualityOptionsData.  # noqa: E501

        Gets or sets the rendering quality for this Graphics.  # noqa: E501

        :return: The smoothing_mode of this GraphicsQualityOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._smoothing_mode

    @smoothing_mode.setter
    def smoothing_mode(self, smoothing_mode):
        """Sets the smoothing_mode of this GraphicsQualityOptionsData.

        Gets or sets the rendering quality for this Graphics.  # noqa: E501

        :param smoothing_mode: The smoothing_mode of this GraphicsQualityOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Default", "HighSpeed", "HighQuality", "None", "AntiAlias", "Invalid"]  # noqa: E501
        if not smoothing_mode.isdigit():	
            if smoothing_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `smoothing_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(smoothing_mode, allowed_values))
            self._smoothing_mode = smoothing_mode
        else:
            self._smoothing_mode = allowed_values[int(smoothing_mode) if six.PY3 else long(smoothing_mode)]
    @property
    def string_format(self):
        """Gets the string_format of this GraphicsQualityOptionsData.  # noqa: E501

        Gets or sets text layout information (such as alignment, orientation and tab stops) display manipulations (such as ellipsis insertion and national digit substitution) and OpenType features.  # noqa: E501

        :return: The string_format of this GraphicsQualityOptionsData.  # noqa: E501
        :rtype: StringFormatData
        """
        return self._string_format

    @string_format.setter
    def string_format(self, string_format):
        """Sets the string_format of this GraphicsQualityOptionsData.

        Gets or sets text layout information (such as alignment, orientation and tab stops) display manipulations (such as ellipsis insertion and national digit substitution) and OpenType features.  # noqa: E501

        :param string_format: The string_format of this GraphicsQualityOptionsData.  # noqa: E501
        :type: StringFormatData
        """
        self._string_format = string_format
    @property
    def text_rendering_hint(self):
        """Gets the text_rendering_hint of this GraphicsQualityOptionsData.  # noqa: E501

        Gets or sets the rendering mode for text associated with this Graphics.  # noqa: E501

        :return: The text_rendering_hint of this GraphicsQualityOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._text_rendering_hint

    @text_rendering_hint.setter
    def text_rendering_hint(self, text_rendering_hint):
        """Sets the text_rendering_hint of this GraphicsQualityOptionsData.

        Gets or sets the rendering mode for text associated with this Graphics.  # noqa: E501

        :param text_rendering_hint: The text_rendering_hint of this GraphicsQualityOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["SystemDefault", "SingleBitPerPixelGridFit", "SingleBitPerPixel", "AntiAliasGridFit", "AntiAlias", "ClearTypeGridFit"]  # noqa: E501
        if not text_rendering_hint.isdigit():	
            if text_rendering_hint not in allowed_values:
                raise ValueError(
                    "Invalid value for `text_rendering_hint` ({0}), must be one of {1}"  # noqa: E501
                    .format(text_rendering_hint, allowed_values))
            self._text_rendering_hint = text_rendering_hint
        else:
            self._text_rendering_hint = allowed_values[int(text_rendering_hint) if six.PY3 else long(text_rendering_hint)]
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
        if not isinstance(other, GraphicsQualityOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
