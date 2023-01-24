# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="metafile_rendering_options_data.py">
#   Copyright (c) 2023 Aspose.Words for Cloud
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

import datetime
import six
import json

class MetafileRenderingOptionsData(object):
    """Container class for options of metafile rendering.
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
        'scale_wmf_fonts_to_metafile_size': 'bool',
        'use_emf_embedded_to_wmf': 'bool'
    }

    attribute_map = {
        'emf_plus_dual_rendering_mode': 'EmfPlusDualRenderingMode',
        'emulate_raster_operations': 'EmulateRasterOperations',
        'rendering_mode': 'RenderingMode',
        'scale_wmf_fonts_to_metafile_size': 'ScaleWmfFontsToMetafileSize',
        'use_emf_embedded_to_wmf': 'UseEmfEmbeddedToWmf'
    }

    def __init__(self, emf_plus_dual_rendering_mode=None, emulate_raster_operations=None, rendering_mode=None, scale_wmf_fonts_to_metafile_size=None, use_emf_embedded_to_wmf=None):  # noqa: E501
        """MetafileRenderingOptionsData - a model defined in Swagger"""  # noqa: E501

        self._emf_plus_dual_rendering_mode = None
        self._emulate_raster_operations = None
        self._rendering_mode = None
        self._scale_wmf_fonts_to_metafile_size = None
        self._use_emf_embedded_to_wmf = None
        self.discriminator = None

        if emf_plus_dual_rendering_mode is not None:
            self.emf_plus_dual_rendering_mode = emf_plus_dual_rendering_mode
        if emulate_raster_operations is not None:
            self.emulate_raster_operations = emulate_raster_operations
        if rendering_mode is not None:
            self.rendering_mode = rendering_mode
        if scale_wmf_fonts_to_metafile_size is not None:
            self.scale_wmf_fonts_to_metafile_size = scale_wmf_fonts_to_metafile_size
        if use_emf_embedded_to_wmf is not None:
            self.use_emf_embedded_to_wmf = use_emf_embedded_to_wmf

    @property
    def emf_plus_dual_rendering_mode(self):
        """Gets the emf_plus_dual_rendering_mode of this MetafileRenderingOptionsData.  # noqa: E501

        Gets or sets the option that controls how EMF+ Dual metafiles should be rendered.  # noqa: E501

        :return: The emf_plus_dual_rendering_mode of this MetafileRenderingOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._emf_plus_dual_rendering_mode

    @emf_plus_dual_rendering_mode.setter
    def emf_plus_dual_rendering_mode(self, emf_plus_dual_rendering_mode):
        """Sets the emf_plus_dual_rendering_mode of this MetafileRenderingOptionsData.

        Gets or sets the option that controls how EMF+ Dual metafiles should be rendered.  # noqa: E501

        :param emf_plus_dual_rendering_mode: The emf_plus_dual_rendering_mode of this MetafileRenderingOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["EmfPlusWithFallback", "EmfPlus", "Emf"]  # noqa: E501
        if not emf_plus_dual_rendering_mode.isdigit():
            if emf_plus_dual_rendering_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `emf_plus_dual_rendering_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(emf_plus_dual_rendering_mode, allowed_values))
            self._emf_plus_dual_rendering_mode = emf_plus_dual_rendering_mode
        else:
            self._emf_plus_dual_rendering_mode = allowed_values[int(emf_plus_dual_rendering_mode) if six.PY3 else long(emf_plus_dual_rendering_mode)]

    @property
    def emulate_raster_operations(self):
        """Gets the emulate_raster_operations of this MetafileRenderingOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the raster operations should be emulated.  # noqa: E501

        :return: The emulate_raster_operations of this MetafileRenderingOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._emulate_raster_operations

    @emulate_raster_operations.setter
    def emulate_raster_operations(self, emulate_raster_operations):
        """Sets the emulate_raster_operations of this MetafileRenderingOptionsData.

        Gets or sets a value indicating whether the raster operations should be emulated.  # noqa: E501

        :param emulate_raster_operations: The emulate_raster_operations of this MetafileRenderingOptionsData.  # noqa: E501
        :type: bool
        """
        self._emulate_raster_operations = emulate_raster_operations

    @property
    def rendering_mode(self):
        """Gets the rendering_mode of this MetafileRenderingOptionsData.  # noqa: E501

        Gets or sets the option that controls how metafile images should be rendered.  # noqa: E501

        :return: The rendering_mode of this MetafileRenderingOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._rendering_mode

    @rendering_mode.setter
    def rendering_mode(self, rendering_mode):
        """Sets the rendering_mode of this MetafileRenderingOptionsData.

        Gets or sets the option that controls how metafile images should be rendered.  # noqa: E501

        :param rendering_mode: The rendering_mode of this MetafileRenderingOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["VectorWithFallback", "Vector", "Bitmap"]  # noqa: E501
        if not rendering_mode.isdigit():
            if rendering_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `rendering_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(rendering_mode, allowed_values))
            self._rendering_mode = rendering_mode
        else:
            self._rendering_mode = allowed_values[int(rendering_mode) if six.PY3 else long(rendering_mode)]

    @property
    def scale_wmf_fonts_to_metafile_size(self):
        """Gets the scale_wmf_fonts_to_metafile_size of this MetafileRenderingOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to scale fonts in WMF metafile according to metafile size on the page. The default value is true.  # noqa: E501

        :return: The scale_wmf_fonts_to_metafile_size of this MetafileRenderingOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._scale_wmf_fonts_to_metafile_size

    @scale_wmf_fonts_to_metafile_size.setter
    def scale_wmf_fonts_to_metafile_size(self, scale_wmf_fonts_to_metafile_size):
        """Sets the scale_wmf_fonts_to_metafile_size of this MetafileRenderingOptionsData.

        Gets or sets a value indicating whether to scale fonts in WMF metafile according to metafile size on the page. The default value is true.  # noqa: E501

        :param scale_wmf_fonts_to_metafile_size: The scale_wmf_fonts_to_metafile_size of this MetafileRenderingOptionsData.  # noqa: E501
        :type: bool
        """
        self._scale_wmf_fonts_to_metafile_size = scale_wmf_fonts_to_metafile_size

    @property
    def use_emf_embedded_to_wmf(self):
        """Gets the use_emf_embedded_to_wmf of this MetafileRenderingOptionsData.  # noqa: E501

        Gets or sets the flag, that controls how WMF metafiles with embedded EMF metafiles should be rendered.  # noqa: E501

        :return: The use_emf_embedded_to_wmf of this MetafileRenderingOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._use_emf_embedded_to_wmf

    @use_emf_embedded_to_wmf.setter
    def use_emf_embedded_to_wmf(self, use_emf_embedded_to_wmf):
        """Sets the use_emf_embedded_to_wmf of this MetafileRenderingOptionsData.

        Gets or sets the flag, that controls how WMF metafiles with embedded EMF metafiles should be rendered.  # noqa: E501

        :param use_emf_embedded_to_wmf: The use_emf_embedded_to_wmf of this MetafileRenderingOptionsData.  # noqa: E501
        :type: bool
        """
        self._use_emf_embedded_to_wmf = use_emf_embedded_to_wmf


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if value is None:
                continue
            if isinstance(value, list):
                result[self.attribute_map[attr]] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map[attr]] = value.to_dict()
            elif isinstance(value, dict):
                result[self.attribute_map[attr]] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            elif isinstance(value, (datetime.datetime, datetime.date)):
                result[self.attribute_map[attr]] = value.isoformat()
            else:
                result[self.attribute_map[attr]] = value

        return result

    def to_json(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map[attr]] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map[attr]] = value.to_dict()
            elif isinstance(value, dict):
                result[self.attribute_map[attr]] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            elif isinstance(value, (datetime.datetime, datetime.date)):
                result[self.attribute_map[attr]] = value.isoformat()
            else:
                result[self.attribute_map[attr]] = value

        return json.dumps(result)

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