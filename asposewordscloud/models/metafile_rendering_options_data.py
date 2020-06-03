# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="MetafileRenderingOptionsData.py">
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


class MetafileRenderingOptionsData(object):
    """container class for options of metafile rendering.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'emf_plus_dual_rendering_mode': 'str',
        'emulate_raster_operations': 'bool',
        'rendering_mode': 'str',
        'use_emf_embedded_to_wmf': 'bool',
        'scale_wmf_fonts_to_metafile_size': 'bool'
    }

    attribute_map = {
        'emf_plus_dual_rendering_mode': 'EmfPlusDualRenderingMode',
        'emulate_raster_operations': 'EmulateRasterOperations',
        'rendering_mode': 'RenderingMode',
        'use_emf_embedded_to_wmf': 'UseEmfEmbeddedToWmf',
        'scale_wmf_fonts_to_metafile_size': 'ScaleWmfFontsToMetafileSize'
    }

    def __init__(self, emf_plus_dual_rendering_mode=None, emulate_raster_operations=None, rendering_mode=None, use_emf_embedded_to_wmf=None, scale_wmf_fonts_to_metafile_size=None):  # noqa: E501
        """MetafileRenderingOptionsData - a model defined in Swagger"""  # noqa: E501

        self._emf_plus_dual_rendering_mode = None
        self._emulate_raster_operations = None
        self._rendering_mode = None
        self._use_emf_embedded_to_wmf = None
        self._scale_wmf_fonts_to_metafile_size = None
        self.discriminator = None

        if emf_plus_dual_rendering_mode is not None:
            self.emf_plus_dual_rendering_mode = emf_plus_dual_rendering_mode
        if emulate_raster_operations is not None:
            self.emulate_raster_operations = emulate_raster_operations
        if rendering_mode is not None:
            self.rendering_mode = rendering_mode
        if use_emf_embedded_to_wmf is not None:
            self.use_emf_embedded_to_wmf = use_emf_embedded_to_wmf
        if scale_wmf_fonts_to_metafile_size is not None:
            self.scale_wmf_fonts_to_metafile_size = scale_wmf_fonts_to_metafile_size

    @property
    def emf_plus_dual_rendering_mode(self):
        """Gets the emf_plus_dual_rendering_mode of this MetafileRenderingOptionsData.  # noqa: E501

        Gets or sets determines how EMF+ Dual metafiles should be rendered.  # noqa: E501

        :return: The emf_plus_dual_rendering_mode of this MetafileRenderingOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._emf_plus_dual_rendering_mode

    @emf_plus_dual_rendering_mode.setter
    def emf_plus_dual_rendering_mode(self, emf_plus_dual_rendering_mode):
        """Sets the emf_plus_dual_rendering_mode of this MetafileRenderingOptionsData.

        Gets or sets determines how EMF+ Dual metafiles should be rendered.  # noqa: E501

        :param emf_plus_dual_rendering_mode: The emf_plus_dual_rendering_mode of this MetafileRenderingOptionsData.  # noqa: E501
        :type: str
        """
        self._emf_plus_dual_rendering_mode = emf_plus_dual_rendering_mode
    @property
    def emulate_raster_operations(self):
        """Gets the emulate_raster_operations of this MetafileRenderingOptionsData.  # noqa: E501

        Gets or sets a value determining whether or not the raster operations should be emulated.               # noqa: E501

        :return: The emulate_raster_operations of this MetafileRenderingOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._emulate_raster_operations

    @emulate_raster_operations.setter
    def emulate_raster_operations(self, emulate_raster_operations):
        """Sets the emulate_raster_operations of this MetafileRenderingOptionsData.

        Gets or sets a value determining whether or not the raster operations should be emulated.               # noqa: E501

        :param emulate_raster_operations: The emulate_raster_operations of this MetafileRenderingOptionsData.  # noqa: E501
        :type: bool
        """
        self._emulate_raster_operations = emulate_raster_operations
    @property
    def rendering_mode(self):
        """Gets the rendering_mode of this MetafileRenderingOptionsData.  # noqa: E501

        Gets or sets determines how metafile images should be rendered.  # noqa: E501

        :return: The rendering_mode of this MetafileRenderingOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._rendering_mode

    @rendering_mode.setter
    def rendering_mode(self, rendering_mode):
        """Sets the rendering_mode of this MetafileRenderingOptionsData.

        Gets or sets determines how metafile images should be rendered.  # noqa: E501

        :param rendering_mode: The rendering_mode of this MetafileRenderingOptionsData.  # noqa: E501
        :type: str
        """
        self._rendering_mode = rendering_mode
    @property
    def use_emf_embedded_to_wmf(self):
        """Gets the use_emf_embedded_to_wmf of this MetafileRenderingOptionsData.  # noqa: E501

        Gets or sets determines how WMF metafiles with embedded EMF metafiles should be rendered.  # noqa: E501

        :return: The use_emf_embedded_to_wmf of this MetafileRenderingOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._use_emf_embedded_to_wmf

    @use_emf_embedded_to_wmf.setter
    def use_emf_embedded_to_wmf(self, use_emf_embedded_to_wmf):
        """Sets the use_emf_embedded_to_wmf of this MetafileRenderingOptionsData.

        Gets or sets determines how WMF metafiles with embedded EMF metafiles should be rendered.  # noqa: E501

        :param use_emf_embedded_to_wmf: The use_emf_embedded_to_wmf of this MetafileRenderingOptionsData.  # noqa: E501
        :type: bool
        """
        self._use_emf_embedded_to_wmf = use_emf_embedded_to_wmf
    @property
    def scale_wmf_fonts_to_metafile_size(self):
        """Gets the scale_wmf_fonts_to_metafile_size of this MetafileRenderingOptionsData.  # noqa: E501

        Gets or sets a value determining whether or not to scale fonts in WMF metafile according to metafile size on the page. The default value is true.  # noqa: E501

        :return: The scale_wmf_fonts_to_metafile_size of this MetafileRenderingOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._scale_wmf_fonts_to_metafile_size

    @scale_wmf_fonts_to_metafile_size.setter
    def scale_wmf_fonts_to_metafile_size(self, scale_wmf_fonts_to_metafile_size):
        """Sets the scale_wmf_fonts_to_metafile_size of this MetafileRenderingOptionsData.

        Gets or sets a value determining whether or not to scale fonts in WMF metafile according to metafile size on the page. The default value is true.  # noqa: E501

        :param scale_wmf_fonts_to_metafile_size: The scale_wmf_fonts_to_metafile_size of this MetafileRenderingOptionsData.  # noqa: E501
        :type: bool
        """
        self._scale_wmf_fonts_to_metafile_size = scale_wmf_fonts_to_metafile_size
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
        if not isinstance(other, MetafileRenderingOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
