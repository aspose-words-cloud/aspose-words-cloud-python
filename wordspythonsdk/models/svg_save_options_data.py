# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="SvgSaveOptionsData.py">
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


class SvgSaveOptionsData(object):
    """container class for svg save options
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'export_embedded_images': 'bool',
        'fit_to_view_port': 'bool',
        'resources_folder': 'str',
        'resources_folder_alias': 'str',
        'show_page_border': 'bool',
        'text_output_mode': 'str'
    }

    attribute_map = {
        'export_embedded_images': 'ExportEmbeddedImages',
        'fit_to_view_port': 'FitToViewPort',
        'resources_folder': 'ResourcesFolder',
        'resources_folder_alias': 'ResourcesFolderAlias',
        'show_page_border': 'ShowPageBorder',
        'text_output_mode': 'TextOutputMode'
    }

    def __init__(self, export_embedded_images=None, fit_to_view_port=None, resources_folder=None, resources_folder_alias=None, show_page_border=None, text_output_mode=None):  # noqa: E501
        """SvgSaveOptionsData - a model defined in Swagger"""  # noqa: E501

        self._export_embedded_images = None
        self._fit_to_view_port = None
        self._resources_folder = None
        self._resources_folder_alias = None
        self._show_page_border = None
        self._text_output_mode = None
        self.discriminator = None

        if export_embedded_images is not None:
            self.export_embedded_images = export_embedded_images
        if fit_to_view_port is not None:
            self.fit_to_view_port = fit_to_view_port
        if resources_folder is not None:
            self.resources_folder = resources_folder
        if resources_folder_alias is not None:
            self.resources_folder_alias = resources_folder_alias
        if show_page_border is not None:
            self.show_page_border = show_page_border
        if text_output_mode is not None:
            self.text_output_mode = text_output_mode

    @property
    def export_embedded_images(self):
        """Gets the export_embedded_images of this SvgSaveOptionsData.  # noqa: E501

        Specified whether images should be embedded into SVG document as base64  # noqa: E501

        :return: The export_embedded_images of this SvgSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_embedded_images

    @export_embedded_images.setter
    def export_embedded_images(self, export_embedded_images):
        """Sets the export_embedded_images of this SvgSaveOptionsData.

        Specified whether images should be embedded into SVG document as base64  # noqa: E501

        :param export_embedded_images: The export_embedded_images of this SvgSaveOptionsData.  # noqa: E501
        :type: bool
        """

        self._export_embedded_images = export_embedded_images

    @property
    def fit_to_view_port(self):
        """Gets the fit_to_view_port of this SvgSaveOptionsData.  # noqa: E501

        Specifies if the output SVG should fill the available viewport area (browser window or container). When set to true width and height of output SVG are set to 100%.  # noqa: E501

        :return: The fit_to_view_port of this SvgSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._fit_to_view_port

    @fit_to_view_port.setter
    def fit_to_view_port(self, fit_to_view_port):
        """Sets the fit_to_view_port of this SvgSaveOptionsData.

        Specifies if the output SVG should fill the available viewport area (browser window or container). When set to true width and height of output SVG are set to 100%.  # noqa: E501

        :param fit_to_view_port: The fit_to_view_port of this SvgSaveOptionsData.  # noqa: E501
        :type: bool
        """

        self._fit_to_view_port = fit_to_view_port

    @property
    def resources_folder(self):
        """Gets the resources_folder of this SvgSaveOptionsData.  # noqa: E501

        Specifies the physical folder where resources (images) are saved when exporting  # noqa: E501

        :return: The resources_folder of this SvgSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._resources_folder

    @resources_folder.setter
    def resources_folder(self, resources_folder):
        """Sets the resources_folder of this SvgSaveOptionsData.

        Specifies the physical folder where resources (images) are saved when exporting  # noqa: E501

        :param resources_folder: The resources_folder of this SvgSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._resources_folder = resources_folder

    @property
    def resources_folder_alias(self):
        """Gets the resources_folder_alias of this SvgSaveOptionsData.  # noqa: E501

        Specifies the name of the folder used to construct image URIs  # noqa: E501

        :return: The resources_folder_alias of this SvgSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._resources_folder_alias

    @resources_folder_alias.setter
    def resources_folder_alias(self, resources_folder_alias):
        """Sets the resources_folder_alias of this SvgSaveOptionsData.

        Specifies the name of the folder used to construct image URIs  # noqa: E501

        :param resources_folder_alias: The resources_folder_alias of this SvgSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._resources_folder_alias = resources_folder_alias

    @property
    def show_page_border(self):
        """Gets the show_page_border of this SvgSaveOptionsData.  # noqa: E501

        Show/hide page stepper  # noqa: E501

        :return: The show_page_border of this SvgSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._show_page_border

    @show_page_border.setter
    def show_page_border(self, show_page_border):
        """Sets the show_page_border of this SvgSaveOptionsData.

        Show/hide page stepper  # noqa: E501

        :param show_page_border: The show_page_border of this SvgSaveOptionsData.  # noqa: E501
        :type: bool
        """

        self._show_page_border = show_page_border

    @property
    def text_output_mode(self):
        """Gets the text_output_mode of this SvgSaveOptionsData.  # noqa: E501

        Determines how text should be rendered  # noqa: E501

        :return: The text_output_mode of this SvgSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._text_output_mode

    @text_output_mode.setter
    def text_output_mode(self, text_output_mode):
        """Sets the text_output_mode of this SvgSaveOptionsData.

        Determines how text should be rendered  # noqa: E501

        :param text_output_mode: The text_output_mode of this SvgSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._text_output_mode = text_output_mode

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
        if not isinstance(other, SvgSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
