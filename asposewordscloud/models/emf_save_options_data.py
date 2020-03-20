# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="EmfSaveOptionsData.py">
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


class EmfSaveOptionsData(object):
    """Container class for emf save options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'graphics_quality_options': 'GraphicsQualityOptionsData',
        'horizontal_resolution': 'float',
        'image_brightness': 'float',
        'image_color_mode': 'str',
        'image_contrast': 'float',
        'paper_color': 'str',
        'pixel_format': 'str',
        'resolution': 'float',
        'scale': 'float',
        'use_anti_aliasing': 'bool',
        'use_gdi_emf_renderer': 'bool',
        'use_high_quality_rendering': 'bool',
        'vertical_resolution': 'float'
    }

    attribute_map = {
        'graphics_quality_options': 'GraphicsQualityOptions',
        'horizontal_resolution': 'HorizontalResolution',
        'image_brightness': 'ImageBrightness',
        'image_color_mode': 'ImageColorMode',
        'image_contrast': 'ImageContrast',
        'paper_color': 'PaperColor',
        'pixel_format': 'PixelFormat',
        'resolution': 'Resolution',
        'scale': 'Scale',
        'use_anti_aliasing': 'UseAntiAliasing',
        'use_gdi_emf_renderer': 'UseGdiEmfRenderer',
        'use_high_quality_rendering': 'UseHighQualityRendering',
        'vertical_resolution': 'VerticalResolution'
    }

    def __init__(self, graphics_quality_options=None, horizontal_resolution=None, image_brightness=None, image_color_mode=None, image_contrast=None, paper_color=None, pixel_format=None, resolution=None, scale=None, use_anti_aliasing=None, use_gdi_emf_renderer=None, use_high_quality_rendering=None, vertical_resolution=None):  # noqa: E501
        """EmfSaveOptionsData - a model defined in Swagger"""  # noqa: E501

        self._graphics_quality_options = None
        self._horizontal_resolution = None
        self._image_brightness = None
        self._image_color_mode = None
        self._image_contrast = None
        self._paper_color = None
        self._pixel_format = None
        self._resolution = None
        self._scale = None
        self._use_anti_aliasing = None
        self._use_gdi_emf_renderer = None
        self._use_high_quality_rendering = None
        self._vertical_resolution = None
        self.discriminator = None

        if graphics_quality_options is not None:
            self.graphics_quality_options = graphics_quality_options
        if horizontal_resolution is not None:
            self.horizontal_resolution = horizontal_resolution
        if image_brightness is not None:
            self.image_brightness = image_brightness
        if image_color_mode is not None:
            self.image_color_mode = image_color_mode
        if image_contrast is not None:
            self.image_contrast = image_contrast
        if paper_color is not None:
            self.paper_color = paper_color
        if pixel_format is not None:
            self.pixel_format = pixel_format
        if resolution is not None:
            self.resolution = resolution
        if scale is not None:
            self.scale = scale
        if use_anti_aliasing is not None:
            self.use_anti_aliasing = use_anti_aliasing
        if use_gdi_emf_renderer is not None:
            self.use_gdi_emf_renderer = use_gdi_emf_renderer
        if use_high_quality_rendering is not None:
            self.use_high_quality_rendering = use_high_quality_rendering
        if vertical_resolution is not None:
            self.vertical_resolution = vertical_resolution

    @property
    def graphics_quality_options(self):
        """Gets the graphics_quality_options of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets graphics_quality_options.  # noqa: E501

        :return: The graphics_quality_options of this EmfSaveOptionsData.  # noqa: E501
        :rtype: GraphicsQualityOptionsData
        """
        return self._graphics_quality_options

    @graphics_quality_options.setter
    def graphics_quality_options(self, graphics_quality_options):
        """Sets the graphics_quality_options of this EmfSaveOptionsData.

        Gets or sets graphics_quality_options.  # noqa: E501

        :param graphics_quality_options: The graphics_quality_options of this EmfSaveOptionsData.  # noqa: E501
        :type: GraphicsQualityOptionsData
        """
        self._graphics_quality_options = graphics_quality_options
    @property
    def horizontal_resolution(self):
        """Gets the horizontal_resolution of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the horizontal resolution for the generated images, in dots per inch.  This property has effect only when saving to raster image formats. The default value is 96.  # noqa: E501

        :return: The horizontal_resolution of this EmfSaveOptionsData.  # noqa: E501
        :rtype: float
        """
        return self._horizontal_resolution

    @horizontal_resolution.setter
    def horizontal_resolution(self, horizontal_resolution):
        """Sets the horizontal_resolution of this EmfSaveOptionsData.

        Gets or sets the horizontal resolution for the generated images, in dots per inch.  This property has effect only when saving to raster image formats. The default value is 96.  # noqa: E501

        :param horizontal_resolution: The horizontal_resolution of this EmfSaveOptionsData.  # noqa: E501
        :type: float
        """
        self._horizontal_resolution = horizontal_resolution
    @property
    def image_brightness(self):
        """Gets the image_brightness of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets brightness of image.  # noqa: E501

        :return: The image_brightness of this EmfSaveOptionsData.  # noqa: E501
        :rtype: float
        """
        return self._image_brightness

    @image_brightness.setter
    def image_brightness(self, image_brightness):
        """Sets the image_brightness of this EmfSaveOptionsData.

        Gets or sets brightness of image.  # noqa: E501

        :param image_brightness: The image_brightness of this EmfSaveOptionsData.  # noqa: E501
        :type: float
        """
        self._image_brightness = image_brightness
    @property
    def image_color_mode(self):
        """Gets the image_color_mode of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets color mode of image.  # noqa: E501

        :return: The image_color_mode of this EmfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._image_color_mode

    @image_color_mode.setter
    def image_color_mode(self, image_color_mode):
        """Sets the image_color_mode of this EmfSaveOptionsData.

        Gets or sets color mode of image.  # noqa: E501

        :param image_color_mode: The image_color_mode of this EmfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._image_color_mode = image_color_mode
    @property
    def image_contrast(self):
        """Gets the image_contrast of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets contrast of image.  # noqa: E501

        :return: The image_contrast of this EmfSaveOptionsData.  # noqa: E501
        :rtype: float
        """
        return self._image_contrast

    @image_contrast.setter
    def image_contrast(self, image_contrast):
        """Sets the image_contrast of this EmfSaveOptionsData.

        Gets or sets contrast of image.  # noqa: E501

        :param image_contrast: The image_contrast of this EmfSaveOptionsData.  # noqa: E501
        :type: float
        """
        self._image_contrast = image_contrast
    @property
    def paper_color(self):
        """Gets the paper_color of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets background (paper) color of image.  # noqa: E501

        :return: The paper_color of this EmfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._paper_color

    @paper_color.setter
    def paper_color(self, paper_color):
        """Sets the paper_color of this EmfSaveOptionsData.

        Gets or sets background (paper) color of image.  # noqa: E501

        :param paper_color: The paper_color of this EmfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._paper_color = paper_color
    @property
    def pixel_format(self):
        """Gets the pixel_format of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets pixel format of image.  # noqa: E501

        :return: The pixel_format of this EmfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._pixel_format

    @pixel_format.setter
    def pixel_format(self, pixel_format):
        """Sets the pixel_format of this EmfSaveOptionsData.

        Gets or sets pixel format of image.  # noqa: E501

        :param pixel_format: The pixel_format of this EmfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._pixel_format = pixel_format
    @property
    def resolution(self):
        """Gets the resolution of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets both horizontal and vertical resolution for the generated images, in dots per inch.  This property has effect only when saving to raster image formats. The default value is 96.  # noqa: E501

        :return: The resolution of this EmfSaveOptionsData.  # noqa: E501
        :rtype: float
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this EmfSaveOptionsData.

        Gets or sets both horizontal and vertical resolution for the generated images, in dots per inch.  This property has effect only when saving to raster image formats. The default value is 96.  # noqa: E501

        :param resolution: The resolution of this EmfSaveOptionsData.  # noqa: E501
        :type: float
        """
        self._resolution = resolution
    @property
    def scale(self):
        """Gets the scale of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets zoom factor of image.  # noqa: E501

        :return: The scale of this EmfSaveOptionsData.  # noqa: E501
        :rtype: float
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this EmfSaveOptionsData.

        Gets or sets zoom factor of image.  # noqa: E501

        :param scale: The scale of this EmfSaveOptionsData.  # noqa: E501
        :type: float
        """
        self._scale = scale
    @property
    def use_anti_aliasing(self):
        """Gets the use_anti_aliasing of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets determine whether or not to use anti-aliasing for rendering.  # noqa: E501

        :return: The use_anti_aliasing of this EmfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._use_anti_aliasing

    @use_anti_aliasing.setter
    def use_anti_aliasing(self, use_anti_aliasing):
        """Sets the use_anti_aliasing of this EmfSaveOptionsData.

        Gets or sets determine whether or not to use anti-aliasing for rendering.  # noqa: E501

        :param use_anti_aliasing: The use_anti_aliasing of this EmfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._use_anti_aliasing = use_anti_aliasing
    @property
    def use_gdi_emf_renderer(self):
        """Gets the use_gdi_emf_renderer of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets a value determining whether to use GDI+ or Aspose.Words metafile renderer when saving to EMF.  # noqa: E501

        :return: The use_gdi_emf_renderer of this EmfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._use_gdi_emf_renderer

    @use_gdi_emf_renderer.setter
    def use_gdi_emf_renderer(self, use_gdi_emf_renderer):
        """Sets the use_gdi_emf_renderer of this EmfSaveOptionsData.

        Gets or sets a value determining whether to use GDI+ or Aspose.Words metafile renderer when saving to EMF.  # noqa: E501

        :param use_gdi_emf_renderer: The use_gdi_emf_renderer of this EmfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._use_gdi_emf_renderer = use_gdi_emf_renderer
    @property
    def use_high_quality_rendering(self):
        """Gets the use_high_quality_rendering of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets determine whether or not to use high quality (i.e. slow) rendering algorithms.  # noqa: E501

        :return: The use_high_quality_rendering of this EmfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._use_high_quality_rendering

    @use_high_quality_rendering.setter
    def use_high_quality_rendering(self, use_high_quality_rendering):
        """Sets the use_high_quality_rendering of this EmfSaveOptionsData.

        Gets or sets determine whether or not to use high quality (i.e. slow) rendering algorithms.  # noqa: E501

        :param use_high_quality_rendering: The use_high_quality_rendering of this EmfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._use_high_quality_rendering = use_high_quality_rendering
    @property
    def vertical_resolution(self):
        """Gets the vertical_resolution of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the vertical resolution for the generated images, in dots per inch.  This property has effect only when saving to raster image formats. The default value is 96.  # noqa: E501

        :return: The vertical_resolution of this EmfSaveOptionsData.  # noqa: E501
        :rtype: float
        """
        return self._vertical_resolution

    @vertical_resolution.setter
    def vertical_resolution(self, vertical_resolution):
        """Sets the vertical_resolution of this EmfSaveOptionsData.

        Gets or sets the vertical resolution for the generated images, in dots per inch.  This property has effect only when saving to raster image formats. The default value is 96.  # noqa: E501

        :param vertical_resolution: The vertical_resolution of this EmfSaveOptionsData.  # noqa: E501
        :type: float
        """
        self._vertical_resolution = vertical_resolution
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
        if not isinstance(other, EmfSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
