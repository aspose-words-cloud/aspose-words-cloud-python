# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="PdfSaveOptionsData.py">
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


class PdfSaveOptionsData(object):
    """container class for pdf save options
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'compliance': 'str',
        'create_note_hyperlinks': 'bool',
        'custom_properties_export': 'str',
        'digital_signature_details': 'PdfDigitalSignatureDetailsData',
        'display_doc_title': 'bool',
        'downsample_options': 'DownsampleOptionsData',
        'embed_full_fonts': 'bool',
        'encryption_details': 'PdfEncryptionDetailsData',
        'export_document_structure': 'bool',
        'font_embedding_mode': 'str',
        'image_color_space_export_mode': 'str',
        'image_compression': 'str',
        'open_hyperlinks_in_new_window': 'bool',
        'outline_options': 'OutlineOptionsData',
        'page_mode': 'str',
        'preblend_images': 'bool',
        'preserve_form_fields': 'bool',
        'text_compression': 'str',
        'use_book_fold_printing_settings': 'bool',
        'use_core_fonts': 'bool',
        'zoom_behavior': 'str',
        'zoom_factor': 'int'
    }

    attribute_map = {
        'compliance': 'Compliance',
        'create_note_hyperlinks': 'CreateNoteHyperlinks',
        'custom_properties_export': 'CustomPropertiesExport',
        'digital_signature_details': 'DigitalSignatureDetails',
        'display_doc_title': 'DisplayDocTitle',
        'downsample_options': 'DownsampleOptions',
        'embed_full_fonts': 'EmbedFullFonts',
        'encryption_details': 'EncryptionDetails',
        'export_document_structure': 'ExportDocumentStructure',
        'font_embedding_mode': 'FontEmbeddingMode',
        'image_color_space_export_mode': 'ImageColorSpaceExportMode',
        'image_compression': 'ImageCompression',
        'open_hyperlinks_in_new_window': 'OpenHyperlinksInNewWindow',
        'outline_options': 'OutlineOptions',
        'page_mode': 'PageMode',
        'preblend_images': 'PreblendImages',
        'preserve_form_fields': 'PreserveFormFields',
        'text_compression': 'TextCompression',
        'use_book_fold_printing_settings': 'UseBookFoldPrintingSettings',
        'use_core_fonts': 'UseCoreFonts',
        'zoom_behavior': 'ZoomBehavior',
        'zoom_factor': 'ZoomFactor'
    }

    def __init__(self, compliance=None, create_note_hyperlinks=None, custom_properties_export=None, digital_signature_details=None, display_doc_title=None, downsample_options=None, embed_full_fonts=None, encryption_details=None, export_document_structure=None, font_embedding_mode=None, image_color_space_export_mode=None, image_compression=None, open_hyperlinks_in_new_window=None, outline_options=None, page_mode=None, preblend_images=None, preserve_form_fields=None, text_compression=None, use_book_fold_printing_settings=None, use_core_fonts=None, zoom_behavior=None, zoom_factor=None):  # noqa: E501
        """PdfSaveOptionsData - a model defined in Swagger"""  # noqa: E501

        self._compliance = None
        self._create_note_hyperlinks = None
        self._custom_properties_export = None
        self._digital_signature_details = None
        self._display_doc_title = None
        self._downsample_options = None
        self._embed_full_fonts = None
        self._encryption_details = None
        self._export_document_structure = None
        self._font_embedding_mode = None
        self._image_color_space_export_mode = None
        self._image_compression = None
        self._open_hyperlinks_in_new_window = None
        self._outline_options = None
        self._page_mode = None
        self._preblend_images = None
        self._preserve_form_fields = None
        self._text_compression = None
        self._use_book_fold_printing_settings = None
        self._use_core_fonts = None
        self._zoom_behavior = None
        self._zoom_factor = None
        self.discriminator = None

        if compliance is not None:
            self.compliance = compliance
        if create_note_hyperlinks is not None:
            self.create_note_hyperlinks = create_note_hyperlinks
        if custom_properties_export is not None:
            self.custom_properties_export = custom_properties_export
        if digital_signature_details is not None:
            self.digital_signature_details = digital_signature_details
        if display_doc_title is not None:
            self.display_doc_title = display_doc_title
        if downsample_options is not None:
            self.downsample_options = downsample_options
        if embed_full_fonts is not None:
            self.embed_full_fonts = embed_full_fonts
        if encryption_details is not None:
            self.encryption_details = encryption_details
        if export_document_structure is not None:
            self.export_document_structure = export_document_structure
        if font_embedding_mode is not None:
            self.font_embedding_mode = font_embedding_mode
        if image_color_space_export_mode is not None:
            self.image_color_space_export_mode = image_color_space_export_mode
        if image_compression is not None:
            self.image_compression = image_compression
        if open_hyperlinks_in_new_window is not None:
            self.open_hyperlinks_in_new_window = open_hyperlinks_in_new_window
        if outline_options is not None:
            self.outline_options = outline_options
        if page_mode is not None:
            self.page_mode = page_mode
        if preblend_images is not None:
            self.preblend_images = preblend_images
        if preserve_form_fields is not None:
            self.preserve_form_fields = preserve_form_fields
        if text_compression is not None:
            self.text_compression = text_compression
        if use_book_fold_printing_settings is not None:
            self.use_book_fold_printing_settings = use_book_fold_printing_settings
        if use_core_fonts is not None:
            self.use_core_fonts = use_core_fonts
        if zoom_behavior is not None:
            self.zoom_behavior = zoom_behavior
        if zoom_factor is not None:
            self.zoom_factor = zoom_factor

    @property
    def compliance(self):
        """Gets the compliance of this PdfSaveOptionsData.  # noqa: E501

        Specifies the PDF standards compliance level for output documents  # noqa: E501

        :return: The compliance of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._compliance

    @compliance.setter
    def compliance(self, compliance):
        """Sets the compliance of this PdfSaveOptionsData.

        Specifies the PDF standards compliance level for output documents  # noqa: E501

        :param compliance: The compliance of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._compliance = compliance

    @property
    def create_note_hyperlinks(self):
        """Gets the create_note_hyperlinks of this PdfSaveOptionsData.  # noqa: E501

        Specifies whether to convert footnote/endnote references in main text story into active hyperlinks. When clicked the hyperlink will lead to the corresponding footnote/endnote. Default is false.  # noqa: E501

        :return: The create_note_hyperlinks of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._create_note_hyperlinks

    @create_note_hyperlinks.setter
    def create_note_hyperlinks(self, create_note_hyperlinks):
        """Sets the create_note_hyperlinks of this PdfSaveOptionsData.

        Specifies whether to convert footnote/endnote references in main text story into active hyperlinks. When clicked the hyperlink will lead to the corresponding footnote/endnote. Default is false.  # noqa: E501

        :param create_note_hyperlinks: The create_note_hyperlinks of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """

        self._create_note_hyperlinks = create_note_hyperlinks

    @property
    def custom_properties_export(self):
        """Gets the custom_properties_export of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets a value determining the way  are exported to PDF file. Default value is .  # noqa: E501

        :return: The custom_properties_export of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._custom_properties_export

    @custom_properties_export.setter
    def custom_properties_export(self, custom_properties_export):
        """Sets the custom_properties_export of this PdfSaveOptionsData.

        Gets or sets a value determining the way  are exported to PDF file. Default value is .  # noqa: E501

        :param custom_properties_export: The custom_properties_export of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._custom_properties_export = custom_properties_export

    @property
    def digital_signature_details(self):
        """Gets the digital_signature_details of this PdfSaveOptionsData.  # noqa: E501

        Specifies the details for signing the output PDF document  # noqa: E501

        :return: The digital_signature_details of this PdfSaveOptionsData.  # noqa: E501
        :rtype: PdfDigitalSignatureDetailsData
        """
        return self._digital_signature_details

    @digital_signature_details.setter
    def digital_signature_details(self, digital_signature_details):
        """Sets the digital_signature_details of this PdfSaveOptionsData.

        Specifies the details for signing the output PDF document  # noqa: E501

        :param digital_signature_details: The digital_signature_details of this PdfSaveOptionsData.  # noqa: E501
        :type: PdfDigitalSignatureDetailsData
        """

        self._digital_signature_details = digital_signature_details

    @property
    def display_doc_title(self):
        """Gets the display_doc_title of this PdfSaveOptionsData.  # noqa: E501

        A flag specifying whether the window’s title bar should display the document title taken from the Title entry of the document information dictionary.  # noqa: E501

        :return: The display_doc_title of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._display_doc_title

    @display_doc_title.setter
    def display_doc_title(self, display_doc_title):
        """Sets the display_doc_title of this PdfSaveOptionsData.

        A flag specifying whether the window’s title bar should display the document title taken from the Title entry of the document information dictionary.  # noqa: E501

        :param display_doc_title: The display_doc_title of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """

        self._display_doc_title = display_doc_title

    @property
    def downsample_options(self):
        """Gets the downsample_options of this PdfSaveOptionsData.  # noqa: E501

        Allows to specify downsample options.  # noqa: E501

        :return: The downsample_options of this PdfSaveOptionsData.  # noqa: E501
        :rtype: DownsampleOptionsData
        """
        return self._downsample_options

    @downsample_options.setter
    def downsample_options(self, downsample_options):
        """Sets the downsample_options of this PdfSaveOptionsData.

        Allows to specify downsample options.  # noqa: E501

        :param downsample_options: The downsample_options of this PdfSaveOptionsData.  # noqa: E501
        :type: DownsampleOptionsData
        """

        self._downsample_options = downsample_options

    @property
    def embed_full_fonts(self):
        """Gets the embed_full_fonts of this PdfSaveOptionsData.  # noqa: E501

        Controls how fonts are embedded into the resulting PDF documents  # noqa: E501

        :return: The embed_full_fonts of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._embed_full_fonts

    @embed_full_fonts.setter
    def embed_full_fonts(self, embed_full_fonts):
        """Sets the embed_full_fonts of this PdfSaveOptionsData.

        Controls how fonts are embedded into the resulting PDF documents  # noqa: E501

        :param embed_full_fonts: The embed_full_fonts of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """

        self._embed_full_fonts = embed_full_fonts

    @property
    def encryption_details(self):
        """Gets the encryption_details of this PdfSaveOptionsData.  # noqa: E501

        Specifies the details for encrypting the output PDF document  # noqa: E501

        :return: The encryption_details of this PdfSaveOptionsData.  # noqa: E501
        :rtype: PdfEncryptionDetailsData
        """
        return self._encryption_details

    @encryption_details.setter
    def encryption_details(self, encryption_details):
        """Sets the encryption_details of this PdfSaveOptionsData.

        Specifies the details for encrypting the output PDF document  # noqa: E501

        :param encryption_details: The encryption_details of this PdfSaveOptionsData.  # noqa: E501
        :type: PdfEncryptionDetailsData
        """

        self._encryption_details = encryption_details

    @property
    def export_document_structure(self):
        """Gets the export_document_structure of this PdfSaveOptionsData.  # noqa: E501

        Determines whether or not to export document structure  # noqa: E501

        :return: The export_document_structure of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_document_structure

    @export_document_structure.setter
    def export_document_structure(self, export_document_structure):
        """Sets the export_document_structure of this PdfSaveOptionsData.

        Determines whether or not to export document structure  # noqa: E501

        :param export_document_structure: The export_document_structure of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """

        self._export_document_structure = export_document_structure

    @property
    def font_embedding_mode(self):
        """Gets the font_embedding_mode of this PdfSaveOptionsData.  # noqa: E501

        Specifies the font embedding mode  # noqa: E501

        :return: The font_embedding_mode of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._font_embedding_mode

    @font_embedding_mode.setter
    def font_embedding_mode(self, font_embedding_mode):
        """Sets the font_embedding_mode of this PdfSaveOptionsData.

        Specifies the font embedding mode  # noqa: E501

        :param font_embedding_mode: The font_embedding_mode of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._font_embedding_mode = font_embedding_mode

    @property
    def image_color_space_export_mode(self):
        """Gets the image_color_space_export_mode of this PdfSaveOptionsData.  # noqa: E501

        Specifies how the color space will be selected for the images in PDF document.  # noqa: E501

        :return: The image_color_space_export_mode of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._image_color_space_export_mode

    @image_color_space_export_mode.setter
    def image_color_space_export_mode(self, image_color_space_export_mode):
        """Sets the image_color_space_export_mode of this PdfSaveOptionsData.

        Specifies how the color space will be selected for the images in PDF document.  # noqa: E501

        :param image_color_space_export_mode: The image_color_space_export_mode of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._image_color_space_export_mode = image_color_space_export_mode

    @property
    def image_compression(self):
        """Gets the image_compression of this PdfSaveOptionsData.  # noqa: E501

        Specifies compression type to be used for all images in the document  # noqa: E501

        :return: The image_compression of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._image_compression

    @image_compression.setter
    def image_compression(self, image_compression):
        """Sets the image_compression of this PdfSaveOptionsData.

        Specifies compression type to be used for all images in the document  # noqa: E501

        :param image_compression: The image_compression of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._image_compression = image_compression

    @property
    def open_hyperlinks_in_new_window(self):
        """Gets the open_hyperlinks_in_new_window of this PdfSaveOptionsData.  # noqa: E501

        Determines whether hyperlinks in the output Pdf document are forced to be opened in a new window (or tab) of a browser  # noqa: E501

        :return: The open_hyperlinks_in_new_window of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._open_hyperlinks_in_new_window

    @open_hyperlinks_in_new_window.setter
    def open_hyperlinks_in_new_window(self, open_hyperlinks_in_new_window):
        """Sets the open_hyperlinks_in_new_window of this PdfSaveOptionsData.

        Determines whether hyperlinks in the output Pdf document are forced to be opened in a new window (or tab) of a browser  # noqa: E501

        :param open_hyperlinks_in_new_window: The open_hyperlinks_in_new_window of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """

        self._open_hyperlinks_in_new_window = open_hyperlinks_in_new_window

    @property
    def outline_options(self):
        """Gets the outline_options of this PdfSaveOptionsData.  # noqa: E501

        Allows to specify outline options  # noqa: E501

        :return: The outline_options of this PdfSaveOptionsData.  # noqa: E501
        :rtype: OutlineOptionsData
        """
        return self._outline_options

    @outline_options.setter
    def outline_options(self, outline_options):
        """Sets the outline_options of this PdfSaveOptionsData.

        Allows to specify outline options  # noqa: E501

        :param outline_options: The outline_options of this PdfSaveOptionsData.  # noqa: E501
        :type: OutlineOptionsData
        """

        self._outline_options = outline_options

    @property
    def page_mode(self):
        """Gets the page_mode of this PdfSaveOptionsData.  # noqa: E501

        Specifies how the PDF document should be displayed when opened in the PDF reader  # noqa: E501

        :return: The page_mode of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._page_mode

    @page_mode.setter
    def page_mode(self, page_mode):
        """Sets the page_mode of this PdfSaveOptionsData.

        Specifies how the PDF document should be displayed when opened in the PDF reader  # noqa: E501

        :param page_mode: The page_mode of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._page_mode = page_mode

    @property
    def preblend_images(self):
        """Gets the preblend_images of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets a value determining whether or not to preblend transparent images with black background color.  # noqa: E501

        :return: The preblend_images of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._preblend_images

    @preblend_images.setter
    def preblend_images(self, preblend_images):
        """Sets the preblend_images of this PdfSaveOptionsData.

        Gets or sets a value determining whether or not to preblend transparent images with black background color.  # noqa: E501

        :param preblend_images: The preblend_images of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """

        self._preblend_images = preblend_images

    @property
    def preserve_form_fields(self):
        """Gets the preserve_form_fields of this PdfSaveOptionsData.  # noqa: E501

        Specifies whether to preserve Microsoft Word form fields as form fields in PDF or convert them to text  # noqa: E501

        :return: The preserve_form_fields of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._preserve_form_fields

    @preserve_form_fields.setter
    def preserve_form_fields(self, preserve_form_fields):
        """Sets the preserve_form_fields of this PdfSaveOptionsData.

        Specifies whether to preserve Microsoft Word form fields as form fields in PDF or convert them to text  # noqa: E501

        :param preserve_form_fields: The preserve_form_fields of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """

        self._preserve_form_fields = preserve_form_fields

    @property
    def text_compression(self):
        """Gets the text_compression of this PdfSaveOptionsData.  # noqa: E501

        Specifies compression type to be used for all textual content in the document  # noqa: E501

        :return: The text_compression of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._text_compression

    @text_compression.setter
    def text_compression(self, text_compression):
        """Sets the text_compression of this PdfSaveOptionsData.

        Specifies compression type to be used for all textual content in the document  # noqa: E501

        :param text_compression: The text_compression of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._text_compression = text_compression

    @property
    def use_book_fold_printing_settings(self):
        """Gets the use_book_fold_printing_settings of this PdfSaveOptionsData.  # noqa: E501

        Determines whether the document should be saved using a booklet printing layout  # noqa: E501

        :return: The use_book_fold_printing_settings of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._use_book_fold_printing_settings

    @use_book_fold_printing_settings.setter
    def use_book_fold_printing_settings(self, use_book_fold_printing_settings):
        """Sets the use_book_fold_printing_settings of this PdfSaveOptionsData.

        Determines whether the document should be saved using a booklet printing layout  # noqa: E501

        :param use_book_fold_printing_settings: The use_book_fold_printing_settings of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """

        self._use_book_fold_printing_settings = use_book_fold_printing_settings

    @property
    def use_core_fonts(self):
        """Gets the use_core_fonts of this PdfSaveOptionsData.  # noqa: E501

        Determines whether or not to substitute TrueType fonts Arial, Times New Roman, Courier New and Symbol with core PDF Type 1 fonts  # noqa: E501

        :return: The use_core_fonts of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._use_core_fonts

    @use_core_fonts.setter
    def use_core_fonts(self, use_core_fonts):
        """Sets the use_core_fonts of this PdfSaveOptionsData.

        Determines whether or not to substitute TrueType fonts Arial, Times New Roman, Courier New and Symbol with core PDF Type 1 fonts  # noqa: E501

        :param use_core_fonts: The use_core_fonts of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """

        self._use_core_fonts = use_core_fonts

    @property
    def zoom_behavior(self):
        """Gets the zoom_behavior of this PdfSaveOptionsData.  # noqa: E501

        Determines what type of zoom should be applied when a document is opened with a PDF viewer  # noqa: E501

        :return: The zoom_behavior of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._zoom_behavior

    @zoom_behavior.setter
    def zoom_behavior(self, zoom_behavior):
        """Sets the zoom_behavior of this PdfSaveOptionsData.

        Determines what type of zoom should be applied when a document is opened with a PDF viewer  # noqa: E501

        :param zoom_behavior: The zoom_behavior of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._zoom_behavior = zoom_behavior

    @property
    def zoom_factor(self):
        """Gets the zoom_factor of this PdfSaveOptionsData.  # noqa: E501

        Determines zoom factor (in percentages) for a document  # noqa: E501

        :return: The zoom_factor of this PdfSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._zoom_factor

    @zoom_factor.setter
    def zoom_factor(self, zoom_factor):
        """Sets the zoom_factor of this PdfSaveOptionsData.

        Determines zoom factor (in percentages) for a document  # noqa: E501

        :param zoom_factor: The zoom_factor of this PdfSaveOptionsData.  # noqa: E501
        :type: int
        """

        self._zoom_factor = zoom_factor

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
        if not isinstance(other, PdfSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
