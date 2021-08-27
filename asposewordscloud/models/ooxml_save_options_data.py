# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="ooxml_save_options_data.py">
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


class OoxmlSaveOptionsData(object):
    """Container class for docx/docm/dotx/dotm/flatopc save options.
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
        'compliance': 'str',
        'compression_level': 'str',
        'password': 'str',
        'pretty_format': 'bool'
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
        'compliance': 'Compliance',
        'compression_level': 'CompressionLevel',
        'password': 'Password',
        'pretty_format': 'PrettyFormat'
    }

    def __init__(self, allow_embedding_post_script_fonts=None, custom_time_zone_info_data=None, dml3_d_effects_rendering_mode=None, dml_effects_rendering_mode=None, dml_rendering_mode=None, file_name=None, flat_opc_xml_mapping_only=None, iml_rendering_mode=None, save_format=None, update_created_time_property=None, update_fields=None, update_last_printed_property=None, update_last_saved_time_property=None, update_sdt_content=None, zip_output=None, compliance=None, compression_level=None, password=None, pretty_format=None):  # noqa: E501
        """OoxmlSaveOptionsData - a model defined in Swagger"""  # noqa: E501

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
        self._compliance = None
        self._compression_level = None
        self._password = None
        self._pretty_format = None
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
        if compliance is not None:
            self.compliance = compliance
        if compression_level is not None:
            self.compression_level = compression_level
        if password is not None:
            self.password = password
        if pretty_format is not None:
            self.pretty_format = pretty_format

    @property
    def allow_embedding_post_script_fonts(self):
        """Gets the allow_embedding_post_script_fonts of this OoxmlSaveOptionsData.  # noqa: E501

        Gets or sets a boolean value indicating whether to allow embedding fonts with PostScript outlines when embedding TrueType fonts in a document upon it is saved. The default value is false..  # noqa: E501

        :return: The allow_embedding_post_script_fonts of this OoxmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._allow_embedding_post_script_fonts

    @allow_embedding_post_script_fonts.setter
    def allow_embedding_post_script_fonts(self, allow_embedding_post_script_fonts):
        """Sets the allow_embedding_post_script_fonts of this OoxmlSaveOptionsData.

        Gets or sets a boolean value indicating whether to allow embedding fonts with PostScript outlines when embedding TrueType fonts in a document upon it is saved. The default value is false..  # noqa: E501

        :param allow_embedding_post_script_fonts: The allow_embedding_post_script_fonts of this OoxmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._allow_embedding_post_script_fonts = allow_embedding_post_script_fonts

    @property
    def custom_time_zone_info_data(self):
        """Gets the custom_time_zone_info_data of this OoxmlSaveOptionsData.  # noqa: E501

        Gets or sets CustomTimeZoneInfo.  # noqa: E501

        :return: The custom_time_zone_info_data of this OoxmlSaveOptionsData.  # noqa: E501
        :rtype: TimeZoneInfoData
        """
        return self._custom_time_zone_info_data

    @custom_time_zone_info_data.setter
    def custom_time_zone_info_data(self, custom_time_zone_info_data):
        """Sets the custom_time_zone_info_data of this OoxmlSaveOptionsData.

        Gets or sets CustomTimeZoneInfo.  # noqa: E501

        :param custom_time_zone_info_data: The custom_time_zone_info_data of this OoxmlSaveOptionsData.  # noqa: E501
        :type: TimeZoneInfoData
        """
        self._custom_time_zone_info_data = custom_time_zone_info_data

    @property
    def dml3_d_effects_rendering_mode(self):
        """Gets the dml3_d_effects_rendering_mode of this OoxmlSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how 3D effects are rendered.  # noqa: E501

        :return: The dml3_d_effects_rendering_mode of this OoxmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml3_d_effects_rendering_mode

    @dml3_d_effects_rendering_mode.setter
    def dml3_d_effects_rendering_mode(self, dml3_d_effects_rendering_mode):
        """Sets the dml3_d_effects_rendering_mode of this OoxmlSaveOptionsData.

        Gets or sets the value determining how 3D effects are rendered.  # noqa: E501

        :param dml3_d_effects_rendering_mode: The dml3_d_effects_rendering_mode of this OoxmlSaveOptionsData.  # noqa: E501
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
        """Gets the dml_effects_rendering_mode of this OoxmlSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how DrawingML effects are rendered. { Simplified | None | Fine }.  # noqa: E501

        :return: The dml_effects_rendering_mode of this OoxmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_effects_rendering_mode

    @dml_effects_rendering_mode.setter
    def dml_effects_rendering_mode(self, dml_effects_rendering_mode):
        """Sets the dml_effects_rendering_mode of this OoxmlSaveOptionsData.

        Gets or sets the value determining how DrawingML effects are rendered. { Simplified | None | Fine }.  # noqa: E501

        :param dml_effects_rendering_mode: The dml_effects_rendering_mode of this OoxmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._dml_effects_rendering_mode = dml_effects_rendering_mode

    @property
    def dml_rendering_mode(self):
        """Gets the dml_rendering_mode of this OoxmlSaveOptionsData.  # noqa: E501

        Gets or sets the option that controls how DrawingML shapes are rendered.  # noqa: E501

        :return: The dml_rendering_mode of this OoxmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_rendering_mode

    @dml_rendering_mode.setter
    def dml_rendering_mode(self, dml_rendering_mode):
        """Sets the dml_rendering_mode of this OoxmlSaveOptionsData.

        Gets or sets the option that controls how DrawingML shapes are rendered.  # noqa: E501

        :param dml_rendering_mode: The dml_rendering_mode of this OoxmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._dml_rendering_mode = dml_rendering_mode

    @property
    def file_name(self):
        """Gets the file_name of this OoxmlSaveOptionsData.  # noqa: E501

        Gets or sets the name of destination file.  # noqa: E501

        :return: The file_name of this OoxmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this OoxmlSaveOptionsData.

        Gets or sets the name of destination file.  # noqa: E501

        :param file_name: The file_name of this OoxmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._file_name = file_name

    @property
    def flat_opc_xml_mapping_only(self):
        """Gets the flat_opc_xml_mapping_only of this OoxmlSaveOptionsData.  # noqa: E501

        Gets or sets value determining which document formats are allowed to be mapped by Aspose.Words.Markup.StructuredDocumentTag.XmlMapping. By default only Aspose.Words.LoadFormat.FlatOpc document format is allowed to be mapped.  # noqa: E501

        :return: The flat_opc_xml_mapping_only of this OoxmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._flat_opc_xml_mapping_only

    @flat_opc_xml_mapping_only.setter
    def flat_opc_xml_mapping_only(self, flat_opc_xml_mapping_only):
        """Sets the flat_opc_xml_mapping_only of this OoxmlSaveOptionsData.

        Gets or sets value determining which document formats are allowed to be mapped by Aspose.Words.Markup.StructuredDocumentTag.XmlMapping. By default only Aspose.Words.LoadFormat.FlatOpc document format is allowed to be mapped.  # noqa: E501

        :param flat_opc_xml_mapping_only: The flat_opc_xml_mapping_only of this OoxmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._flat_opc_xml_mapping_only = flat_opc_xml_mapping_only

    @property
    def iml_rendering_mode(self):
        """Gets the iml_rendering_mode of this OoxmlSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how ink (InkML) objects are rendered.  # noqa: E501

        :return: The iml_rendering_mode of this OoxmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._iml_rendering_mode

    @iml_rendering_mode.setter
    def iml_rendering_mode(self, iml_rendering_mode):
        """Sets the iml_rendering_mode of this OoxmlSaveOptionsData.

        Gets or sets the value determining how ink (InkML) objects are rendered.  # noqa: E501

        :param iml_rendering_mode: The iml_rendering_mode of this OoxmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._iml_rendering_mode = iml_rendering_mode

    @property
    def save_format(self):
        """Gets the save_format of this OoxmlSaveOptionsData.  # noqa: E501

        Gets or sets the format of save.  # noqa: E501

        :return: The save_format of this OoxmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._save_format

    @save_format.setter
    def save_format(self, save_format):
        """Sets the save_format of this OoxmlSaveOptionsData.

        Gets or sets the format of save.  # noqa: E501

        :param save_format: The save_format of this OoxmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._save_format = save_format

    @property
    def update_created_time_property(self):
        """Gets the update_created_time_property of this OoxmlSaveOptionsData.  # noqa: E501

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.CreatedTime property is updated before saving. Default value is false.  # noqa: E501

        :return: The update_created_time_property of this OoxmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_created_time_property

    @update_created_time_property.setter
    def update_created_time_property(self, update_created_time_property):
        """Sets the update_created_time_property of this OoxmlSaveOptionsData.

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.CreatedTime property is updated before saving. Default value is false.  # noqa: E501

        :param update_created_time_property: The update_created_time_property of this OoxmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_created_time_property = update_created_time_property

    @property
    def update_fields(self):
        """Gets the update_fields of this OoxmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether fields should be updated before saving the document to a fixed page format. The default value is true.  # noqa: E501

        :return: The update_fields of this OoxmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_fields

    @update_fields.setter
    def update_fields(self, update_fields):
        """Sets the update_fields of this OoxmlSaveOptionsData.

        Gets or sets a value indicating whether fields should be updated before saving the document to a fixed page format. The default value is true.  # noqa: E501

        :param update_fields: The update_fields of this OoxmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_fields = update_fields

    @property
    def update_last_printed_property(self):
        """Gets the update_last_printed_property of this OoxmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastPrinted property is updated before saving.  # noqa: E501

        :return: The update_last_printed_property of this OoxmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_last_printed_property

    @update_last_printed_property.setter
    def update_last_printed_property(self, update_last_printed_property):
        """Sets the update_last_printed_property of this OoxmlSaveOptionsData.

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastPrinted property is updated before saving.  # noqa: E501

        :param update_last_printed_property: The update_last_printed_property of this OoxmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_last_printed_property = update_last_printed_property

    @property
    def update_last_saved_time_property(self):
        """Gets the update_last_saved_time_property of this OoxmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving.  # noqa: E501

        :return: The update_last_saved_time_property of this OoxmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_last_saved_time_property

    @update_last_saved_time_property.setter
    def update_last_saved_time_property(self, update_last_saved_time_property):
        """Sets the update_last_saved_time_property of this OoxmlSaveOptionsData.

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving.  # noqa: E501

        :param update_last_saved_time_property: The update_last_saved_time_property of this OoxmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_last_saved_time_property = update_last_saved_time_property

    @property
    def update_sdt_content(self):
        """Gets the update_sdt_content of this OoxmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether content of StructuredDocumentTag is updated before saving.  # noqa: E501

        :return: The update_sdt_content of this OoxmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_sdt_content

    @update_sdt_content.setter
    def update_sdt_content(self, update_sdt_content):
        """Sets the update_sdt_content of this OoxmlSaveOptionsData.

        Gets or sets a value indicating whether content of StructuredDocumentTag is updated before saving.  # noqa: E501

        :param update_sdt_content: The update_sdt_content of this OoxmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_sdt_content = update_sdt_content

    @property
    def zip_output(self):
        """Gets the zip_output of this OoxmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to zip output or not. The default value is false.  # noqa: E501

        :return: The zip_output of this OoxmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._zip_output

    @zip_output.setter
    def zip_output(self, zip_output):
        """Sets the zip_output of this OoxmlSaveOptionsData.

        Gets or sets a value indicating whether to zip output or not. The default value is false.  # noqa: E501

        :param zip_output: The zip_output of this OoxmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._zip_output = zip_output

    @property
    def compliance(self):
        """Gets the compliance of this OoxmlSaveOptionsData.  # noqa: E501

        Gets or sets the oOXML version for the output document.  # noqa: E501

        :return: The compliance of this OoxmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._compliance

    @compliance.setter
    def compliance(self, compliance):
        """Sets the compliance of this OoxmlSaveOptionsData.

        Gets or sets the oOXML version for the output document.  # noqa: E501

        :param compliance: The compliance of this OoxmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._compliance = compliance

    @property
    def compression_level(self):
        """Gets the compression_level of this OoxmlSaveOptionsData.  # noqa: E501

        Gets or sets the compression level.  # noqa: E501

        :return: The compression_level of this OoxmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._compression_level

    @compression_level.setter
    def compression_level(self, compression_level):
        """Sets the compression_level of this OoxmlSaveOptionsData.

        Gets or sets the compression level.  # noqa: E501

        :param compression_level: The compression_level of this OoxmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Normal", "Maximum", "Fast", "SuperFast"]  # noqa: E501
        if not compression_level.isdigit():
            if compression_level not in allowed_values:
                raise ValueError(
                    "Invalid value for `compression_level` ({0}), must be one of {1}"  # noqa: E501
                    .format(compression_level, allowed_values))
            self._compression_level = compression_level
        else:
            self._compression_level = allowed_values[int(compression_level) if six.PY3 else long(compression_level)]

    @property
    def password(self):
        """Gets the password of this OoxmlSaveOptionsData.  # noqa: E501

        Gets or sets the password to encrypt document using ECMA376 Standard encryption algorithm.  # noqa: E501

        :return: The password of this OoxmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this OoxmlSaveOptionsData.

        Gets or sets the password to encrypt document using ECMA376 Standard encryption algorithm.  # noqa: E501

        :param password: The password of this OoxmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._password = password

    @property
    def pretty_format(self):
        """Gets the pretty_format of this OoxmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to use pretty formats output.  # noqa: E501

        :return: The pretty_format of this OoxmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._pretty_format

    @pretty_format.setter
    def pretty_format(self, pretty_format):
        """Sets the pretty_format of this OoxmlSaveOptionsData.

        Gets or sets a value indicating whether to use pretty formats output.  # noqa: E501

        :param pretty_format: The pretty_format of this OoxmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._pretty_format = pretty_format


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
        if not isinstance(other, OoxmlSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other