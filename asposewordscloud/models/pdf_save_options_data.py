# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="pdf_save_options_data.py">
#   Copyright (c) 2021 Aspose.Words for Cloud
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


class PdfSaveOptionsData(object):
    """Container class for pdf save options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'allow_embedding_post_script_fonts': 'bool',
        'custom_time_zone_info_data': 'TimeZoneInfoData',
        'dml3_d_effects_rendering_mode': 'str',
        'dml_effects_rendering_mode': 'str',
        'dml_rendering_mode': 'str',
        'file_name': 'str',
        'flat_opc_xml_mapping_only': 'bool',
        'iml_rendering_mode': 'str',
        'save_format': 'str',
        'update_created_time_property': 'bool',
        'update_fields': 'bool',
        'update_last_printed_property': 'bool',
        'update_last_saved_time_property': 'bool',
        'update_sdt_content': 'bool',
        'zip_output': 'bool',
        'color_mode': 'str',
        'jpeg_quality': 'int',
        'metafile_rendering_options': 'MetafileRenderingOptionsData',
        'numeral_format': 'str',
        'optimize_output': 'bool',
        'page_count': 'int',
        'page_index': 'int',
        'compliance': 'str',
        'create_note_hyperlinks': 'bool',
        'custom_properties_export': 'str',
        'digital_signature_details': 'PdfDigitalSignatureDetailsData',
        'display_doc_title': 'bool',
        'downsample_options': 'DownsampleOptionsData',
        'embed_full_fonts': 'bool',
        'encryption_details': 'PdfEncryptionDetailsData',
        'export_document_structure': 'bool',
        'export_language_to_span_tag': 'bool',
        'font_embedding_mode': 'str',
        'header_footer_bookmarks_export_mode': 'str',
        'image_color_space_export_mode': 'str',
        'image_compression': 'str',
        'interpolate_images': 'bool',
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
        'allow_embedding_post_script_fonts': 'AllowEmbeddingPostScriptFonts',
        'custom_time_zone_info_data': 'CustomTimeZoneInfoData',
        'dml3_d_effects_rendering_mode': 'Dml3DEffectsRenderingMode',
        'dml_effects_rendering_mode': 'DmlEffectsRenderingMode',
        'dml_rendering_mode': 'DmlRenderingMode',
        'file_name': 'FileName',
        'flat_opc_xml_mapping_only': 'FlatOpcXmlMappingOnly',
        'iml_rendering_mode': 'ImlRenderingMode',
        'save_format': 'SaveFormat',
        'update_created_time_property': 'UpdateCreatedTimeProperty',
        'update_fields': 'UpdateFields',
        'update_last_printed_property': 'UpdateLastPrintedProperty',
        'update_last_saved_time_property': 'UpdateLastSavedTimeProperty',
        'update_sdt_content': 'UpdateSdtContent',
        'zip_output': 'ZipOutput',
        'color_mode': 'ColorMode',
        'jpeg_quality': 'JpegQuality',
        'metafile_rendering_options': 'MetafileRenderingOptions',
        'numeral_format': 'NumeralFormat',
        'optimize_output': 'OptimizeOutput',
        'page_count': 'PageCount',
        'page_index': 'PageIndex',
        'compliance': 'Compliance',
        'create_note_hyperlinks': 'CreateNoteHyperlinks',
        'custom_properties_export': 'CustomPropertiesExport',
        'digital_signature_details': 'DigitalSignatureDetails',
        'display_doc_title': 'DisplayDocTitle',
        'downsample_options': 'DownsampleOptions',
        'embed_full_fonts': 'EmbedFullFonts',
        'encryption_details': 'EncryptionDetails',
        'export_document_structure': 'ExportDocumentStructure',
        'export_language_to_span_tag': 'ExportLanguageToSpanTag',
        'font_embedding_mode': 'FontEmbeddingMode',
        'header_footer_bookmarks_export_mode': 'HeaderFooterBookmarksExportMode',
        'image_color_space_export_mode': 'ImageColorSpaceExportMode',
        'image_compression': 'ImageCompression',
        'interpolate_images': 'InterpolateImages',
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

    def __init__(self, allow_embedding_post_script_fonts=None, custom_time_zone_info_data=None, dml3_d_effects_rendering_mode=None, dml_effects_rendering_mode=None, dml_rendering_mode=None, file_name=None, flat_opc_xml_mapping_only=None, iml_rendering_mode=None, save_format=None, update_created_time_property=None, update_fields=None, update_last_printed_property=None, update_last_saved_time_property=None, update_sdt_content=None, zip_output=None, color_mode=None, jpeg_quality=None, metafile_rendering_options=None, numeral_format=None, optimize_output=None, page_count=None, page_index=None, compliance=None, create_note_hyperlinks=None, custom_properties_export=None, digital_signature_details=None, display_doc_title=None, downsample_options=None, embed_full_fonts=None, encryption_details=None, export_document_structure=None, export_language_to_span_tag=None, font_embedding_mode=None, header_footer_bookmarks_export_mode=None, image_color_space_export_mode=None, image_compression=None, interpolate_images=None, open_hyperlinks_in_new_window=None, outline_options=None, page_mode=None, preblend_images=None, preserve_form_fields=None, text_compression=None, use_book_fold_printing_settings=None, use_core_fonts=None, zoom_behavior=None, zoom_factor=None):  # noqa: E501
        """PdfSaveOptionsData - a model defined in Swagger"""  # noqa: E501

        self._allow_embedding_post_script_fonts = None
        self._custom_time_zone_info_data = None
        self._dml3_d_effects_rendering_mode = None
        self._dml_effects_rendering_mode = None
        self._dml_rendering_mode = None
        self._file_name = None
        self._flat_opc_xml_mapping_only = None
        self._iml_rendering_mode = None
        self._save_format = None
        self._update_created_time_property = None
        self._update_fields = None
        self._update_last_printed_property = None
        self._update_last_saved_time_property = None
        self._update_sdt_content = None
        self._zip_output = None
        self._color_mode = None
        self._jpeg_quality = None
        self._metafile_rendering_options = None
        self._numeral_format = None
        self._optimize_output = None
        self._page_count = None
        self._page_index = None
        self._compliance = None
        self._create_note_hyperlinks = None
        self._custom_properties_export = None
        self._digital_signature_details = None
        self._display_doc_title = None
        self._downsample_options = None
        self._embed_full_fonts = None
        self._encryption_details = None
        self._export_document_structure = None
        self._export_language_to_span_tag = None
        self._font_embedding_mode = None
        self._header_footer_bookmarks_export_mode = None
        self._image_color_space_export_mode = None
        self._image_compression = None
        self._interpolate_images = None
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

        if allow_embedding_post_script_fonts is not None:
            self.allow_embedding_post_script_fonts = allow_embedding_post_script_fonts
        if custom_time_zone_info_data is not None:
            self.custom_time_zone_info_data = custom_time_zone_info_data
        if dml3_d_effects_rendering_mode is not None:
            self.dml3_d_effects_rendering_mode = dml3_d_effects_rendering_mode
        if dml_effects_rendering_mode is not None:
            self.dml_effects_rendering_mode = dml_effects_rendering_mode
        if dml_rendering_mode is not None:
            self.dml_rendering_mode = dml_rendering_mode
        if file_name is not None:
            self.file_name = file_name
        if flat_opc_xml_mapping_only is not None:
            self.flat_opc_xml_mapping_only = flat_opc_xml_mapping_only
        if iml_rendering_mode is not None:
            self.iml_rendering_mode = iml_rendering_mode
        if save_format is not None:
            self.save_format = save_format
        if update_created_time_property is not None:
            self.update_created_time_property = update_created_time_property
        if update_fields is not None:
            self.update_fields = update_fields
        if update_last_printed_property is not None:
            self.update_last_printed_property = update_last_printed_property
        if update_last_saved_time_property is not None:
            self.update_last_saved_time_property = update_last_saved_time_property
        if update_sdt_content is not None:
            self.update_sdt_content = update_sdt_content
        if zip_output is not None:
            self.zip_output = zip_output
        if color_mode is not None:
            self.color_mode = color_mode
        if jpeg_quality is not None:
            self.jpeg_quality = jpeg_quality
        if metafile_rendering_options is not None:
            self.metafile_rendering_options = metafile_rendering_options
        if numeral_format is not None:
            self.numeral_format = numeral_format
        if optimize_output is not None:
            self.optimize_output = optimize_output
        if page_count is not None:
            self.page_count = page_count
        if page_index is not None:
            self.page_index = page_index
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
        if export_language_to_span_tag is not None:
            self.export_language_to_span_tag = export_language_to_span_tag
        if font_embedding_mode is not None:
            self.font_embedding_mode = font_embedding_mode
        if header_footer_bookmarks_export_mode is not None:
            self.header_footer_bookmarks_export_mode = header_footer_bookmarks_export_mode
        if image_color_space_export_mode is not None:
            self.image_color_space_export_mode = image_color_space_export_mode
        if image_compression is not None:
            self.image_compression = image_compression
        if interpolate_images is not None:
            self.interpolate_images = interpolate_images
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
    def allow_embedding_post_script_fonts(self):
        """Gets the allow_embedding_post_script_fonts of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets a boolean value indicating whether to allow embedding fonts with PostScript outlines when embedding TrueType fonts in a document upon it is saved. The default value is false..  # noqa: E501

        :return: The allow_embedding_post_script_fonts of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._allow_embedding_post_script_fonts

    @allow_embedding_post_script_fonts.setter
    def allow_embedding_post_script_fonts(self, allow_embedding_post_script_fonts):
        """Sets the allow_embedding_post_script_fonts of this PdfSaveOptionsData.

        Gets or sets a boolean value indicating whether to allow embedding fonts with PostScript outlines when embedding TrueType fonts in a document upon it is saved. The default value is false..  # noqa: E501

        :param allow_embedding_post_script_fonts: The allow_embedding_post_script_fonts of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._allow_embedding_post_script_fonts = allow_embedding_post_script_fonts

    @property
    def custom_time_zone_info_data(self):
        """Gets the custom_time_zone_info_data of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets CustomTimeZoneInfo.  # noqa: E501

        :return: The custom_time_zone_info_data of this PdfSaveOptionsData.  # noqa: E501
        :rtype: TimeZoneInfoData
        """
        return self._custom_time_zone_info_data

    @custom_time_zone_info_data.setter
    def custom_time_zone_info_data(self, custom_time_zone_info_data):
        """Sets the custom_time_zone_info_data of this PdfSaveOptionsData.

        Gets or sets CustomTimeZoneInfo.  # noqa: E501

        :param custom_time_zone_info_data: The custom_time_zone_info_data of this PdfSaveOptionsData.  # noqa: E501
        :type: TimeZoneInfoData
        """
        self._custom_time_zone_info_data = custom_time_zone_info_data

    @property
    def dml3_d_effects_rendering_mode(self):
        """Gets the dml3_d_effects_rendering_mode of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how 3D effects are rendered.  # noqa: E501

        :return: The dml3_d_effects_rendering_mode of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml3_d_effects_rendering_mode

    @dml3_d_effects_rendering_mode.setter
    def dml3_d_effects_rendering_mode(self, dml3_d_effects_rendering_mode):
        """Sets the dml3_d_effects_rendering_mode of this PdfSaveOptionsData.

        Gets or sets the value determining how 3D effects are rendered.  # noqa: E501

        :param dml3_d_effects_rendering_mode: The dml3_d_effects_rendering_mode of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Basic", "Advanced"]  # noqa: E501
        if not dml3_d_effects_rendering_mode.isdigit():
            if dml3_d_effects_rendering_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `dml3_d_effects_rendering_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(dml3_d_effects_rendering_mode, allowed_values))
            self._dml3_d_effects_rendering_mode = dml3_d_effects_rendering_mode
        else:
            self._dml3_d_effects_rendering_mode = allowed_values[int(dml3_d_effects_rendering_mode) if six.PY3 else long(dml3_d_effects_rendering_mode)]

    @property
    def dml_effects_rendering_mode(self):
        """Gets the dml_effects_rendering_mode of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how DrawingML effects are rendered. { Simplified | None | Fine }.  # noqa: E501

        :return: The dml_effects_rendering_mode of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_effects_rendering_mode

    @dml_effects_rendering_mode.setter
    def dml_effects_rendering_mode(self, dml_effects_rendering_mode):
        """Sets the dml_effects_rendering_mode of this PdfSaveOptionsData.

        Gets or sets the value determining how DrawingML effects are rendered. { Simplified | None | Fine }.  # noqa: E501

        :param dml_effects_rendering_mode: The dml_effects_rendering_mode of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._dml_effects_rendering_mode = dml_effects_rendering_mode

    @property
    def dml_rendering_mode(self):
        """Gets the dml_rendering_mode of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the option that controls how DrawingML shapes are rendered.  # noqa: E501

        :return: The dml_rendering_mode of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_rendering_mode

    @dml_rendering_mode.setter
    def dml_rendering_mode(self, dml_rendering_mode):
        """Sets the dml_rendering_mode of this PdfSaveOptionsData.

        Gets or sets the option that controls how DrawingML shapes are rendered.  # noqa: E501

        :param dml_rendering_mode: The dml_rendering_mode of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._dml_rendering_mode = dml_rendering_mode

    @property
    def file_name(self):
        """Gets the file_name of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the name of destination file.  # noqa: E501

        :return: The file_name of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this PdfSaveOptionsData.

        Gets or sets the name of destination file.  # noqa: E501

        :param file_name: The file_name of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._file_name = file_name

    @property
    def flat_opc_xml_mapping_only(self):
        """Gets the flat_opc_xml_mapping_only of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets value determining which document formats are allowed to be mapped by Aspose.Words.Markup.StructuredDocumentTag.XmlMapping. By default only Aspose.Words.LoadFormat.FlatOpc document format is allowed to be mapped.  # noqa: E501

        :return: The flat_opc_xml_mapping_only of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._flat_opc_xml_mapping_only

    @flat_opc_xml_mapping_only.setter
    def flat_opc_xml_mapping_only(self, flat_opc_xml_mapping_only):
        """Sets the flat_opc_xml_mapping_only of this PdfSaveOptionsData.

        Gets or sets value determining which document formats are allowed to be mapped by Aspose.Words.Markup.StructuredDocumentTag.XmlMapping. By default only Aspose.Words.LoadFormat.FlatOpc document format is allowed to be mapped.  # noqa: E501

        :param flat_opc_xml_mapping_only: The flat_opc_xml_mapping_only of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._flat_opc_xml_mapping_only = flat_opc_xml_mapping_only

    @property
    def iml_rendering_mode(self):
        """Gets the iml_rendering_mode of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how ink (InkML) objects are rendered.  # noqa: E501

        :return: The iml_rendering_mode of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._iml_rendering_mode

    @iml_rendering_mode.setter
    def iml_rendering_mode(self, iml_rendering_mode):
        """Sets the iml_rendering_mode of this PdfSaveOptionsData.

        Gets or sets the value determining how ink (InkML) objects are rendered.  # noqa: E501

        :param iml_rendering_mode: The iml_rendering_mode of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._iml_rendering_mode = iml_rendering_mode

    @property
    def save_format(self):
        """Gets the save_format of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the format of save.  # noqa: E501

        :return: The save_format of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._save_format

    @save_format.setter
    def save_format(self, save_format):
        """Sets the save_format of this PdfSaveOptionsData.

        Gets or sets the format of save.  # noqa: E501

        :param save_format: The save_format of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._save_format = save_format

    @property
    def update_created_time_property(self):
        """Gets the update_created_time_property of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.CreatedTime property is updated before saving. Default value is false.  # noqa: E501

        :return: The update_created_time_property of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_created_time_property

    @update_created_time_property.setter
    def update_created_time_property(self, update_created_time_property):
        """Sets the update_created_time_property of this PdfSaveOptionsData.

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.CreatedTime property is updated before saving. Default value is false.  # noqa: E501

        :param update_created_time_property: The update_created_time_property of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_created_time_property = update_created_time_property

    @property
    def update_fields(self):
        """Gets the update_fields of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether fields should be updated before saving the document to a fixed page format. The default value is true.  # noqa: E501

        :return: The update_fields of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_fields

    @update_fields.setter
    def update_fields(self, update_fields):
        """Sets the update_fields of this PdfSaveOptionsData.

        Gets or sets a value indicating whether fields should be updated before saving the document to a fixed page format. The default value is true.  # noqa: E501

        :param update_fields: The update_fields of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_fields = update_fields

    @property
    def update_last_printed_property(self):
        """Gets the update_last_printed_property of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastPrinted property is updated before saving.  # noqa: E501

        :return: The update_last_printed_property of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_last_printed_property

    @update_last_printed_property.setter
    def update_last_printed_property(self, update_last_printed_property):
        """Sets the update_last_printed_property of this PdfSaveOptionsData.

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastPrinted property is updated before saving.  # noqa: E501

        :param update_last_printed_property: The update_last_printed_property of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_last_printed_property = update_last_printed_property

    @property
    def update_last_saved_time_property(self):
        """Gets the update_last_saved_time_property of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving.  # noqa: E501

        :return: The update_last_saved_time_property of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_last_saved_time_property

    @update_last_saved_time_property.setter
    def update_last_saved_time_property(self, update_last_saved_time_property):
        """Sets the update_last_saved_time_property of this PdfSaveOptionsData.

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving.  # noqa: E501

        :param update_last_saved_time_property: The update_last_saved_time_property of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_last_saved_time_property = update_last_saved_time_property

    @property
    def update_sdt_content(self):
        """Gets the update_sdt_content of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether content of StructuredDocumentTag is updated before saving.  # noqa: E501

        :return: The update_sdt_content of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_sdt_content

    @update_sdt_content.setter
    def update_sdt_content(self, update_sdt_content):
        """Sets the update_sdt_content of this PdfSaveOptionsData.

        Gets or sets a value indicating whether content of StructuredDocumentTag is updated before saving.  # noqa: E501

        :param update_sdt_content: The update_sdt_content of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_sdt_content = update_sdt_content

    @property
    def zip_output(self):
        """Gets the zip_output of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to zip output or not. The default value is false.  # noqa: E501

        :return: The zip_output of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._zip_output

    @zip_output.setter
    def zip_output(self, zip_output):
        """Sets the zip_output of this PdfSaveOptionsData.

        Gets or sets a value indicating whether to zip output or not. The default value is false.  # noqa: E501

        :param zip_output: The zip_output of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._zip_output = zip_output

    @property
    def color_mode(self):
        """Gets the color_mode of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how colors are rendered. { Normal | Grayscale}.  # noqa: E501

        :return: The color_mode of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._color_mode

    @color_mode.setter
    def color_mode(self, color_mode):
        """Sets the color_mode of this PdfSaveOptionsData.

        Gets or sets the value determining how colors are rendered. { Normal | Grayscale}.  # noqa: E501

        :param color_mode: The color_mode of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._color_mode = color_mode

    @property
    def jpeg_quality(self):
        """Gets the jpeg_quality of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the quality of the JPEG images inside PDF document.  # noqa: E501

        :return: The jpeg_quality of this PdfSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._jpeg_quality

    @jpeg_quality.setter
    def jpeg_quality(self, jpeg_quality):
        """Sets the jpeg_quality of this PdfSaveOptionsData.

        Gets or sets the quality of the JPEG images inside PDF document.  # noqa: E501

        :param jpeg_quality: The jpeg_quality of this PdfSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._jpeg_quality = jpeg_quality

    @property
    def metafile_rendering_options(self):
        """Gets the metafile_rendering_options of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the metafile rendering options.  # noqa: E501

        :return: The metafile_rendering_options of this PdfSaveOptionsData.  # noqa: E501
        :rtype: MetafileRenderingOptionsData
        """
        return self._metafile_rendering_options

    @metafile_rendering_options.setter
    def metafile_rendering_options(self, metafile_rendering_options):
        """Sets the metafile_rendering_options of this PdfSaveOptionsData.

        Gets or sets the metafile rendering options.  # noqa: E501

        :param metafile_rendering_options: The metafile_rendering_options of this PdfSaveOptionsData.  # noqa: E501
        :type: MetafileRenderingOptionsData
        """
        self._metafile_rendering_options = metafile_rendering_options

    @property
    def numeral_format(self):
        """Gets the numeral_format of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the symbol set, that is used to represent numbers while rendering to fixed page formats.  # noqa: E501

        :return: The numeral_format of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._numeral_format

    @numeral_format.setter
    def numeral_format(self, numeral_format):
        """Sets the numeral_format of this PdfSaveOptionsData.

        Gets or sets the symbol set, that is used to represent numbers while rendering to fixed page formats.  # noqa: E501

        :param numeral_format: The numeral_format of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._numeral_format = numeral_format

    @property
    def optimize_output(self):
        """Gets the optimize_output of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether it is required to optimize output of XPS. If this flag is set redundant nested canvases and empty canvases are removed, also neighbor glyphs with the same formatting are concatenated. Note: The accuracy of the content display may be affected if this property is set to true.. The default value is false.  # noqa: E501

        :return: The optimize_output of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._optimize_output

    @optimize_output.setter
    def optimize_output(self, optimize_output):
        """Sets the optimize_output of this PdfSaveOptionsData.

        Gets or sets a value indicating whether it is required to optimize output of XPS. If this flag is set redundant nested canvases and empty canvases are removed, also neighbor glyphs with the same formatting are concatenated. Note: The accuracy of the content display may be affected if this property is set to true.. The default value is false.  # noqa: E501

        :param optimize_output: The optimize_output of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._optimize_output = optimize_output

    @property
    def page_count(self):
        """Gets the page_count of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the number of pages to render.  # noqa: E501

        :return: The page_count of this PdfSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this PdfSaveOptionsData.

        Gets or sets the number of pages to render.  # noqa: E501

        :param page_count: The page_count of this PdfSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._page_count = page_count

    @property
    def page_index(self):
        """Gets the page_index of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the 0-based index of the first page to render.  # noqa: E501

        :return: The page_index of this PdfSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """Sets the page_index of this PdfSaveOptionsData.

        Gets or sets the 0-based index of the first page to render.  # noqa: E501

        :param page_index: The page_index of this PdfSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._page_index = page_index

    @property
    def compliance(self):
        """Gets the compliance of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the PDF standards compliance level for output documents.  # noqa: E501

        :return: The compliance of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._compliance

    @compliance.setter
    def compliance(self, compliance):
        """Sets the compliance of this PdfSaveOptionsData.

        Gets or sets the PDF standards compliance level for output documents.  # noqa: E501

        :param compliance: The compliance of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._compliance = compliance

    @property
    def create_note_hyperlinks(self):
        """Gets the create_note_hyperlinks of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to convert footnote/endnote references in main text story into active hyperlinks. When clicked the hyperlink will lead to the corresponding footnote/endnote. The default value is false.  # noqa: E501

        :return: The create_note_hyperlinks of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._create_note_hyperlinks

    @create_note_hyperlinks.setter
    def create_note_hyperlinks(self, create_note_hyperlinks):
        """Sets the create_note_hyperlinks of this PdfSaveOptionsData.

        Gets or sets a value indicating whether to convert footnote/endnote references in main text story into active hyperlinks. When clicked the hyperlink will lead to the corresponding footnote/endnote. The default value is false.  # noqa: E501

        :param create_note_hyperlinks: The create_note_hyperlinks of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._create_note_hyperlinks = create_note_hyperlinks

    @property
    def custom_properties_export(self):
        """Gets the custom_properties_export of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the option that controls the way CustomDocumentProperties are exported to PDF file. The default value is None.  # noqa: E501

        :return: The custom_properties_export of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._custom_properties_export

    @custom_properties_export.setter
    def custom_properties_export(self, custom_properties_export):
        """Sets the custom_properties_export of this PdfSaveOptionsData.

        Gets or sets the option that controls the way CustomDocumentProperties are exported to PDF file. The default value is None.  # noqa: E501

        :param custom_properties_export: The custom_properties_export of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._custom_properties_export = custom_properties_export

    @property
    def digital_signature_details(self):
        """Gets the digital_signature_details of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the details for signing the output PDF document.  # noqa: E501

        :return: The digital_signature_details of this PdfSaveOptionsData.  # noqa: E501
        :rtype: PdfDigitalSignatureDetailsData
        """
        return self._digital_signature_details

    @digital_signature_details.setter
    def digital_signature_details(self, digital_signature_details):
        """Sets the digital_signature_details of this PdfSaveOptionsData.

        Gets or sets the details for signing the output PDF document.  # noqa: E501

        :param digital_signature_details: The digital_signature_details of this PdfSaveOptionsData.  # noqa: E501
        :type: PdfDigitalSignatureDetailsData
        """
        self._digital_signature_details = digital_signature_details

    @property
    def display_doc_title(self):
        """Gets the display_doc_title of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the window’s title bar should display the document title taken from the Title entry of the document information dictionary.  # noqa: E501

        :return: The display_doc_title of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._display_doc_title

    @display_doc_title.setter
    def display_doc_title(self, display_doc_title):
        """Sets the display_doc_title of this PdfSaveOptionsData.

        Gets or sets a value indicating whether the window’s title bar should display the document title taken from the Title entry of the document information dictionary.  # noqa: E501

        :param display_doc_title: The display_doc_title of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._display_doc_title = display_doc_title

    @property
    def downsample_options(self):
        """Gets the downsample_options of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the downsample options.  # noqa: E501

        :return: The downsample_options of this PdfSaveOptionsData.  # noqa: E501
        :rtype: DownsampleOptionsData
        """
        return self._downsample_options

    @downsample_options.setter
    def downsample_options(self, downsample_options):
        """Sets the downsample_options of this PdfSaveOptionsData.

        Gets or sets the downsample options.  # noqa: E501

        :param downsample_options: The downsample_options of this PdfSaveOptionsData.  # noqa: E501
        :type: DownsampleOptionsData
        """
        self._downsample_options = downsample_options

    @property
    def embed_full_fonts(self):
        """Gets the embed_full_fonts of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether fonts are embedded into the resulting PDF documents.  # noqa: E501

        :return: The embed_full_fonts of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._embed_full_fonts

    @embed_full_fonts.setter
    def embed_full_fonts(self, embed_full_fonts):
        """Sets the embed_full_fonts of this PdfSaveOptionsData.

        Gets or sets a value indicating whether fonts are embedded into the resulting PDF documents.  # noqa: E501

        :param embed_full_fonts: The embed_full_fonts of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._embed_full_fonts = embed_full_fonts

    @property
    def encryption_details(self):
        """Gets the encryption_details of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the details for encrypting the output PDF document.  # noqa: E501

        :return: The encryption_details of this PdfSaveOptionsData.  # noqa: E501
        :rtype: PdfEncryptionDetailsData
        """
        return self._encryption_details

    @encryption_details.setter
    def encryption_details(self, encryption_details):
        """Sets the encryption_details of this PdfSaveOptionsData.

        Gets or sets the details for encrypting the output PDF document.  # noqa: E501

        :param encryption_details: The encryption_details of this PdfSaveOptionsData.  # noqa: E501
        :type: PdfEncryptionDetailsData
        """
        self._encryption_details = encryption_details

    @property
    def export_document_structure(self):
        """Gets the export_document_structure of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to export document structure.  # noqa: E501

        :return: The export_document_structure of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_document_structure

    @export_document_structure.setter
    def export_document_structure(self, export_document_structure):
        """Sets the export_document_structure of this PdfSaveOptionsData.

        Gets or sets a value indicating whether to export document structure.  # noqa: E501

        :param export_document_structure: The export_document_structure of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_document_structure = export_document_structure

    @property
    def export_language_to_span_tag(self):
        """Gets the export_language_to_span_tag of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets a value determining whether or not to create a "Span" tag in the document structure to export the text language.  # noqa: E501

        :return: The export_language_to_span_tag of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_language_to_span_tag

    @export_language_to_span_tag.setter
    def export_language_to_span_tag(self, export_language_to_span_tag):
        """Sets the export_language_to_span_tag of this PdfSaveOptionsData.

        Gets or sets a value determining whether or not to create a "Span" tag in the document structure to export the text language.  # noqa: E501

        :param export_language_to_span_tag: The export_language_to_span_tag of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_language_to_span_tag = export_language_to_span_tag

    @property
    def font_embedding_mode(self):
        """Gets the font_embedding_mode of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the font embedding mode.  # noqa: E501

        :return: The font_embedding_mode of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._font_embedding_mode

    @font_embedding_mode.setter
    def font_embedding_mode(self, font_embedding_mode):
        """Sets the font_embedding_mode of this PdfSaveOptionsData.

        Gets or sets the font embedding mode.  # noqa: E501

        :param font_embedding_mode: The font_embedding_mode of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._font_embedding_mode = font_embedding_mode

    @property
    def header_footer_bookmarks_export_mode(self):
        """Gets the header_footer_bookmarks_export_mode of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the option that controls how bookmarks in headers/footers are exported. The default value is Aspose.Words.Saving.HeaderFooterBookmarksExportMode.All.  # noqa: E501

        :return: The header_footer_bookmarks_export_mode of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._header_footer_bookmarks_export_mode

    @header_footer_bookmarks_export_mode.setter
    def header_footer_bookmarks_export_mode(self, header_footer_bookmarks_export_mode):
        """Sets the header_footer_bookmarks_export_mode of this PdfSaveOptionsData.

        Gets or sets the option that controls how bookmarks in headers/footers are exported. The default value is Aspose.Words.Saving.HeaderFooterBookmarksExportMode.All.  # noqa: E501

        :param header_footer_bookmarks_export_mode: The header_footer_bookmarks_export_mode of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "First", "All"]  # noqa: E501
        if not header_footer_bookmarks_export_mode.isdigit():
            if header_footer_bookmarks_export_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `header_footer_bookmarks_export_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(header_footer_bookmarks_export_mode, allowed_values))
            self._header_footer_bookmarks_export_mode = header_footer_bookmarks_export_mode
        else:
            self._header_footer_bookmarks_export_mode = allowed_values[int(header_footer_bookmarks_export_mode) if six.PY3 else long(header_footer_bookmarks_export_mode)]

    @property
    def image_color_space_export_mode(self):
        """Gets the image_color_space_export_mode of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the option that controls how the color space will be selected for the images in PDF document.  # noqa: E501

        :return: The image_color_space_export_mode of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._image_color_space_export_mode

    @image_color_space_export_mode.setter
    def image_color_space_export_mode(self, image_color_space_export_mode):
        """Sets the image_color_space_export_mode of this PdfSaveOptionsData.

        Gets or sets the option that controls how the color space will be selected for the images in PDF document.  # noqa: E501

        :param image_color_space_export_mode: The image_color_space_export_mode of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._image_color_space_export_mode = image_color_space_export_mode

    @property
    def image_compression(self):
        """Gets the image_compression of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the compression type to be used for all images in the document.  # noqa: E501

        :return: The image_compression of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._image_compression

    @image_compression.setter
    def image_compression(self, image_compression):
        """Sets the image_compression of this PdfSaveOptionsData.

        Gets or sets the compression type to be used for all images in the document.  # noqa: E501

        :param image_compression: The image_compression of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._image_compression = image_compression

    @property
    def interpolate_images(self):
        """Gets the interpolate_images of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether image interpolation shall be performed by a conforming reader. When false is specified, the flag is not written to the output document and the default behavior of reader is used instead.  # noqa: E501

        :return: The interpolate_images of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._interpolate_images

    @interpolate_images.setter
    def interpolate_images(self, interpolate_images):
        """Sets the interpolate_images of this PdfSaveOptionsData.

        Gets or sets a value indicating whether image interpolation shall be performed by a conforming reader. When false is specified, the flag is not written to the output document and the default behavior of reader is used instead.  # noqa: E501

        :param interpolate_images: The interpolate_images of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._interpolate_images = interpolate_images

    @property
    def open_hyperlinks_in_new_window(self):
        """Gets the open_hyperlinks_in_new_window of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether hyperlinks in the output Pdf document are forced to be opened in a new window (or tab) of a browser.  # noqa: E501

        :return: The open_hyperlinks_in_new_window of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._open_hyperlinks_in_new_window

    @open_hyperlinks_in_new_window.setter
    def open_hyperlinks_in_new_window(self, open_hyperlinks_in_new_window):
        """Sets the open_hyperlinks_in_new_window of this PdfSaveOptionsData.

        Gets or sets a value indicating whether hyperlinks in the output Pdf document are forced to be opened in a new window (or tab) of a browser.  # noqa: E501

        :param open_hyperlinks_in_new_window: The open_hyperlinks_in_new_window of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._open_hyperlinks_in_new_window = open_hyperlinks_in_new_window

    @property
    def outline_options(self):
        """Gets the outline_options of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the outline options.  # noqa: E501

        :return: The outline_options of this PdfSaveOptionsData.  # noqa: E501
        :rtype: OutlineOptionsData
        """
        return self._outline_options

    @outline_options.setter
    def outline_options(self, outline_options):
        """Sets the outline_options of this PdfSaveOptionsData.

        Gets or sets the outline options.  # noqa: E501

        :param outline_options: The outline_options of this PdfSaveOptionsData.  # noqa: E501
        :type: OutlineOptionsData
        """
        self._outline_options = outline_options

    @property
    def page_mode(self):
        """Gets the page_mode of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the option that controls how the PDF document should be displayed when opened in the PDF reader.  # noqa: E501

        :return: The page_mode of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._page_mode

    @page_mode.setter
    def page_mode(self, page_mode):
        """Sets the page_mode of this PdfSaveOptionsData.

        Gets or sets the option that controls how the PDF document should be displayed when opened in the PDF reader.  # noqa: E501

        :param page_mode: The page_mode of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._page_mode = page_mode

    @property
    def preblend_images(self):
        """Gets the preblend_images of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to preblend transparent images with black background color.  # noqa: E501

        :return: The preblend_images of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._preblend_images

    @preblend_images.setter
    def preblend_images(self, preblend_images):
        """Sets the preblend_images of this PdfSaveOptionsData.

        Gets or sets a value indicating whether to preblend transparent images with black background color.  # noqa: E501

        :param preblend_images: The preblend_images of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._preblend_images = preblend_images

    @property
    def preserve_form_fields(self):
        """Gets the preserve_form_fields of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to preserve Microsoft Word form fields as form fields in PDF or convert them to text.  # noqa: E501

        :return: The preserve_form_fields of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._preserve_form_fields

    @preserve_form_fields.setter
    def preserve_form_fields(self, preserve_form_fields):
        """Sets the preserve_form_fields of this PdfSaveOptionsData.

        Gets or sets a value indicating whether to preserve Microsoft Word form fields as form fields in PDF or convert them to text.  # noqa: E501

        :param preserve_form_fields: The preserve_form_fields of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._preserve_form_fields = preserve_form_fields

    @property
    def text_compression(self):
        """Gets the text_compression of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the compression type to be used for all textual content in the document.  # noqa: E501

        :return: The text_compression of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._text_compression

    @text_compression.setter
    def text_compression(self, text_compression):
        """Sets the text_compression of this PdfSaveOptionsData.

        Gets or sets the compression type to be used for all textual content in the document.  # noqa: E501

        :param text_compression: The text_compression of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._text_compression = text_compression

    @property
    def use_book_fold_printing_settings(self):
        """Gets the use_book_fold_printing_settings of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the document should be saved using a booklet printing layout.  # noqa: E501

        :return: The use_book_fold_printing_settings of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._use_book_fold_printing_settings

    @use_book_fold_printing_settings.setter
    def use_book_fold_printing_settings(self, use_book_fold_printing_settings):
        """Sets the use_book_fold_printing_settings of this PdfSaveOptionsData.

        Gets or sets a value indicating whether the document should be saved using a booklet printing layout.  # noqa: E501

        :param use_book_fold_printing_settings: The use_book_fold_printing_settings of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._use_book_fold_printing_settings = use_book_fold_printing_settings

    @property
    def use_core_fonts(self):
        """Gets the use_core_fonts of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to substitute TrueType fonts Arial, Times New Roman, Courier New and Symbol with core PDF Type 1 fonts.  # noqa: E501

        :return: The use_core_fonts of this PdfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._use_core_fonts

    @use_core_fonts.setter
    def use_core_fonts(self, use_core_fonts):
        """Sets the use_core_fonts of this PdfSaveOptionsData.

        Gets or sets a value indicating whether to substitute TrueType fonts Arial, Times New Roman, Courier New and Symbol with core PDF Type 1 fonts.  # noqa: E501

        :param use_core_fonts: The use_core_fonts of this PdfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._use_core_fonts = use_core_fonts

    @property
    def zoom_behavior(self):
        """Gets the zoom_behavior of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the option that controls what type of zoom should be applied when a document is opened with a PDF viewer.  # noqa: E501

        :return: The zoom_behavior of this PdfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._zoom_behavior

    @zoom_behavior.setter
    def zoom_behavior(self, zoom_behavior):
        """Sets the zoom_behavior of this PdfSaveOptionsData.

        Gets or sets the option that controls what type of zoom should be applied when a document is opened with a PDF viewer.  # noqa: E501

        :param zoom_behavior: The zoom_behavior of this PdfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._zoom_behavior = zoom_behavior

    @property
    def zoom_factor(self):
        """Gets the zoom_factor of this PdfSaveOptionsData.  # noqa: E501

        Gets or sets the zoom factor (in percentages) for a document.  # noqa: E501

        :return: The zoom_factor of this PdfSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._zoom_factor

    @zoom_factor.setter
    def zoom_factor(self, zoom_factor):
        """Sets the zoom_factor of this PdfSaveOptionsData.

        Gets or sets the zoom factor (in percentages) for a document.  # noqa: E501

        :param zoom_factor: The zoom_factor of this PdfSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._zoom_factor = zoom_factor


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
        if not isinstance(other, PdfSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other