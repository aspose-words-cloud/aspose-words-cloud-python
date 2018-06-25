# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="HtmlFixedSaveOptionsData.py">
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


class HtmlFixedSaveOptionsData(object):
    """container class for fixed html save options
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'css_class_names_prefix': 'str',
        'encoding': 'str',
        'export_embedded_css': 'bool',
        'export_embedded_fonts': 'bool',
        'export_embedded_images': 'bool',
        'export_form_fields': 'bool',
        'font_format': 'str',
        'page_horizontal_alignment': 'str',
        'page_margins': 'float',
        'resources_folder': 'str',
        'resources_folder_alias': 'str',
        'show_page_border': 'bool'
    }

    attribute_map = {
        'css_class_names_prefix': 'CssClassNamesPrefix',
        'encoding': 'Encoding',
        'export_embedded_css': 'ExportEmbeddedCss',
        'export_embedded_fonts': 'ExportEmbeddedFonts',
        'export_embedded_images': 'ExportEmbeddedImages',
        'export_form_fields': 'ExportFormFields',
        'font_format': 'FontFormat',
        'page_horizontal_alignment': 'PageHorizontalAlignment',
        'page_margins': 'PageMargins',
        'resources_folder': 'ResourcesFolder',
        'resources_folder_alias': 'ResourcesFolderAlias',
        'show_page_border': 'ShowPageBorder'
    }

    def __init__(self, css_class_names_prefix=None, encoding=None, export_embedded_css=None, export_embedded_fonts=None, export_embedded_images=None, export_form_fields=None, font_format=None, page_horizontal_alignment=None, page_margins=None, resources_folder=None, resources_folder_alias=None, show_page_border=None):  # noqa: E501
        """HtmlFixedSaveOptionsData - a model defined in Swagger"""  # noqa: E501

        self._css_class_names_prefix = None
        self._encoding = None
        self._export_embedded_css = None
        self._export_embedded_fonts = None
        self._export_embedded_images = None
        self._export_form_fields = None
        self._font_format = None
        self._page_horizontal_alignment = None
        self._page_margins = None
        self._resources_folder = None
        self._resources_folder_alias = None
        self._show_page_border = None
        self.discriminator = None

        if css_class_names_prefix is not None:
            self.css_class_names_prefix = css_class_names_prefix
        if encoding is not None:
            self.encoding = encoding
        if export_embedded_css is not None:
            self.export_embedded_css = export_embedded_css
        if export_embedded_fonts is not None:
            self.export_embedded_fonts = export_embedded_fonts
        if export_embedded_images is not None:
            self.export_embedded_images = export_embedded_images
        if export_form_fields is not None:
            self.export_form_fields = export_form_fields
        if font_format is not None:
            self.font_format = font_format
        if page_horizontal_alignment is not None:
            self.page_horizontal_alignment = page_horizontal_alignment
        if page_margins is not None:
            self.page_margins = page_margins
        if resources_folder is not None:
            self.resources_folder = resources_folder
        if resources_folder_alias is not None:
            self.resources_folder_alias = resources_folder_alias
        if show_page_border is not None:
            self.show_page_border = show_page_border

    @property
    def css_class_names_prefix(self):
        """Gets the css_class_names_prefix of this HtmlFixedSaveOptionsData.  # noqa: E501

        Specifies prefix which is added to all class names in style.css file. Default value is \"aw\".  # noqa: E501

        :return: The css_class_names_prefix of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._css_class_names_prefix

    @css_class_names_prefix.setter
    def css_class_names_prefix(self, css_class_names_prefix):
        """Sets the css_class_names_prefix of this HtmlFixedSaveOptionsData.

        Specifies prefix which is added to all class names in style.css file. Default value is \"aw\".  # noqa: E501

        :param css_class_names_prefix: The css_class_names_prefix of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._css_class_names_prefix = css_class_names_prefix

    @property
    def encoding(self):
        """Gets the encoding of this HtmlFixedSaveOptionsData.  # noqa: E501

        Encoding.  # noqa: E501

        :return: The encoding of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this HtmlFixedSaveOptionsData.

        Encoding.  # noqa: E501

        :param encoding: The encoding of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._encoding = encoding

    @property
    def export_embedded_css(self):
        """Gets the export_embedded_css of this HtmlFixedSaveOptionsData.  # noqa: E501

        Specifies whether the CSS (Cascading Style Sheet) should be embedded into Html document.  # noqa: E501

        :return: The export_embedded_css of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_embedded_css

    @export_embedded_css.setter
    def export_embedded_css(self, export_embedded_css):
        """Sets the export_embedded_css of this HtmlFixedSaveOptionsData.

        Specifies whether the CSS (Cascading Style Sheet) should be embedded into Html document.  # noqa: E501

        :param export_embedded_css: The export_embedded_css of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: bool
        """

        self._export_embedded_css = export_embedded_css

    @property
    def export_embedded_fonts(self):
        """Gets the export_embedded_fonts of this HtmlFixedSaveOptionsData.  # noqa: E501

        Specifies whether fonts should be embedded into Html document in Base64 format.  # noqa: E501

        :return: The export_embedded_fonts of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_embedded_fonts

    @export_embedded_fonts.setter
    def export_embedded_fonts(self, export_embedded_fonts):
        """Sets the export_embedded_fonts of this HtmlFixedSaveOptionsData.

        Specifies whether fonts should be embedded into Html document in Base64 format.  # noqa: E501

        :param export_embedded_fonts: The export_embedded_fonts of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: bool
        """

        self._export_embedded_fonts = export_embedded_fonts

    @property
    def export_embedded_images(self):
        """Gets the export_embedded_images of this HtmlFixedSaveOptionsData.  # noqa: E501

        Specifies whether images should be embedded into Html document in Base64 format.  # noqa: E501

        :return: The export_embedded_images of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_embedded_images

    @export_embedded_images.setter
    def export_embedded_images(self, export_embedded_images):
        """Sets the export_embedded_images of this HtmlFixedSaveOptionsData.

        Specifies whether images should be embedded into Html document in Base64 format.  # noqa: E501

        :param export_embedded_images: The export_embedded_images of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: bool
        """

        self._export_embedded_images = export_embedded_images

    @property
    def export_form_fields(self):
        """Gets the export_form_fields of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets indication of whether form fields are exported as interactive items (as 'input' tag) rather than converted to text or graphics.  # noqa: E501

        :return: The export_form_fields of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_form_fields

    @export_form_fields.setter
    def export_form_fields(self, export_form_fields):
        """Sets the export_form_fields of this HtmlFixedSaveOptionsData.

        Gets or sets indication of whether form fields are exported as interactive items (as 'input' tag) rather than converted to text or graphics.  # noqa: E501

        :param export_form_fields: The export_form_fields of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: bool
        """

        self._export_form_fields = export_form_fields

    @property
    def font_format(self):
        """Gets the font_format of this HtmlFixedSaveOptionsData.  # noqa: E501

        Specifies export format of fonts  # noqa: E501

        :return: The font_format of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._font_format

    @font_format.setter
    def font_format(self, font_format):
        """Sets the font_format of this HtmlFixedSaveOptionsData.

        Specifies export format of fonts  # noqa: E501

        :param font_format: The font_format of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._font_format = font_format

    @property
    def page_horizontal_alignment(self):
        """Gets the page_horizontal_alignment of this HtmlFixedSaveOptionsData.  # noqa: E501

        Specifies the horizontal alignment of pages in an HTML document. Default value is HtmlFixedHorizontalPageAlignment.Center.  # noqa: E501

        :return: The page_horizontal_alignment of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._page_horizontal_alignment

    @page_horizontal_alignment.setter
    def page_horizontal_alignment(self, page_horizontal_alignment):
        """Sets the page_horizontal_alignment of this HtmlFixedSaveOptionsData.

        Specifies the horizontal alignment of pages in an HTML document. Default value is HtmlFixedHorizontalPageAlignment.Center.  # noqa: E501

        :param page_horizontal_alignment: The page_horizontal_alignment of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._page_horizontal_alignment = page_horizontal_alignment

    @property
    def page_margins(self):
        """Gets the page_margins of this HtmlFixedSaveOptionsData.  # noqa: E501

        Specifies the margins around pages in an HTML document. The margins value is measured in points and should be equal to or greater than 0. Default value is 10 points.  # noqa: E501

        :return: The page_margins of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: float
        """
        return self._page_margins

    @page_margins.setter
    def page_margins(self, page_margins):
        """Sets the page_margins of this HtmlFixedSaveOptionsData.

        Specifies the margins around pages in an HTML document. The margins value is measured in points and should be equal to or greater than 0. Default value is 10 points.  # noqa: E501

        :param page_margins: The page_margins of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: float
        """

        self._page_margins = page_margins

    @property
    def resources_folder(self):
        """Gets the resources_folder of this HtmlFixedSaveOptionsData.  # noqa: E501

        Specifies the physical folder where resources are saved when exporting a document  # noqa: E501

        :return: The resources_folder of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._resources_folder

    @resources_folder.setter
    def resources_folder(self, resources_folder):
        """Sets the resources_folder of this HtmlFixedSaveOptionsData.

        Specifies the physical folder where resources are saved when exporting a document  # noqa: E501

        :param resources_folder: The resources_folder of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._resources_folder = resources_folder

    @property
    def resources_folder_alias(self):
        """Gets the resources_folder_alias of this HtmlFixedSaveOptionsData.  # noqa: E501

        Specifies the name of the folder used to construct resource URIs  # noqa: E501

        :return: The resources_folder_alias of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._resources_folder_alias

    @resources_folder_alias.setter
    def resources_folder_alias(self, resources_folder_alias):
        """Sets the resources_folder_alias of this HtmlFixedSaveOptionsData.

        Specifies the name of the folder used to construct resource URIs  # noqa: E501

        :param resources_folder_alias: The resources_folder_alias of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._resources_folder_alias = resources_folder_alias

    @property
    def show_page_border(self):
        """Gets the show_page_border of this HtmlFixedSaveOptionsData.  # noqa: E501

        Specifies whether border around pages should be shown.  # noqa: E501

        :return: The show_page_border of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._show_page_border

    @show_page_border.setter
    def show_page_border(self, show_page_border):
        """Sets the show_page_border of this HtmlFixedSaveOptionsData.

        Specifies whether border around pages should be shown.  # noqa: E501

        :param show_page_border: The show_page_border of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: bool
        """

        self._show_page_border = show_page_border

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
        if not isinstance(other, HtmlFixedSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
