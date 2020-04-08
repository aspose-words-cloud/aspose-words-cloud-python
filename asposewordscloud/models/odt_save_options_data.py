# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="OdtSaveOptionsData.py">
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


class OdtSaveOptionsData(object):
    """container class for odt/ott save options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'save_format': 'str',
        'file_name': 'str',
        'dml_rendering_mode': 'str',
        'dml_effects_rendering_mode': 'str',
        'zip_output': 'bool',
        'update_last_saved_time_property': 'bool',
        'update_sdt_content': 'bool',
        'update_fields': 'bool',
        'is_strict_schema11': 'bool',
        'measure_unit': 'str',
        'pretty_format': 'bool'
    }

    attribute_map = {
        'save_format': 'SaveFormat',
        'file_name': 'FileName',
        'dml_rendering_mode': 'DmlRenderingMode',
        'dml_effects_rendering_mode': 'DmlEffectsRenderingMode',
        'zip_output': 'ZipOutput',
        'update_last_saved_time_property': 'UpdateLastSavedTimeProperty',
        'update_sdt_content': 'UpdateSdtContent',
        'update_fields': 'UpdateFields',
        'is_strict_schema11': 'IsStrictSchema11',
        'measure_unit': 'MeasureUnit',
        'pretty_format': 'PrettyFormat'
    }

    def __init__(self, save_format=None, file_name=None, dml_rendering_mode=None, dml_effects_rendering_mode=None, zip_output=None, update_last_saved_time_property=None, update_sdt_content=None, update_fields=None, is_strict_schema11=None, measure_unit=None, pretty_format=None):  # noqa: E501
        """OdtSaveOptionsData - a model defined in Swagger"""  # noqa: E501

        self._save_format = None
        self._file_name = None
        self._dml_rendering_mode = None
        self._dml_effects_rendering_mode = None
        self._zip_output = None
        self._update_last_saved_time_property = None
        self._update_sdt_content = None
        self._update_fields = None
        self._is_strict_schema11 = None
        self._measure_unit = None
        self._pretty_format = None
        self.discriminator = None

        if save_format is not None:
            self.save_format = save_format
        if file_name is not None:
            self.file_name = file_name
        if dml_rendering_mode is not None:
            self.dml_rendering_mode = dml_rendering_mode
        if dml_effects_rendering_mode is not None:
            self.dml_effects_rendering_mode = dml_effects_rendering_mode
        if zip_output is not None:
            self.zip_output = zip_output
        if update_last_saved_time_property is not None:
            self.update_last_saved_time_property = update_last_saved_time_property
        if update_sdt_content is not None:
            self.update_sdt_content = update_sdt_content
        if update_fields is not None:
            self.update_fields = update_fields
        if is_strict_schema11 is not None:
            self.is_strict_schema11 = is_strict_schema11
        if measure_unit is not None:
            self.measure_unit = measure_unit
        if pretty_format is not None:
            self.pretty_format = pretty_format

    @property
    def save_format(self):
        """Gets the save_format of this OdtSaveOptionsData.  # noqa: E501

        Gets or sets format of save.  # noqa: E501

        :return: The save_format of this OdtSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._save_format

    @save_format.setter
    def save_format(self, save_format):
        """Sets the save_format of this OdtSaveOptionsData.

        Gets or sets format of save.  # noqa: E501

        :param save_format: The save_format of this OdtSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._save_format = save_format
    @property
    def file_name(self):
        """Gets the file_name of this OdtSaveOptionsData.  # noqa: E501

        Gets or sets name of destination file.  # noqa: E501

        :return: The file_name of this OdtSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this OdtSaveOptionsData.

        Gets or sets name of destination file.  # noqa: E501

        :param file_name: The file_name of this OdtSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._file_name = file_name
    @property
    def dml_rendering_mode(self):
        """Gets the dml_rendering_mode of this OdtSaveOptionsData.  # noqa: E501

        Gets or sets a value determining how DrawingML shapes are rendered. { Fallback | DrawingML }.  # noqa: E501

        :return: The dml_rendering_mode of this OdtSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_rendering_mode

    @dml_rendering_mode.setter
    def dml_rendering_mode(self, dml_rendering_mode):
        """Sets the dml_rendering_mode of this OdtSaveOptionsData.

        Gets or sets a value determining how DrawingML shapes are rendered. { Fallback | DrawingML }.  # noqa: E501

        :param dml_rendering_mode: The dml_rendering_mode of this OdtSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._dml_rendering_mode = dml_rendering_mode
    @property
    def dml_effects_rendering_mode(self):
        """Gets the dml_effects_rendering_mode of this OdtSaveOptionsData.  # noqa: E501

        Gets or sets a value determining how DrawingML effects are rendered. { Simplified | None | Fine }.  # noqa: E501

        :return: The dml_effects_rendering_mode of this OdtSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_effects_rendering_mode

    @dml_effects_rendering_mode.setter
    def dml_effects_rendering_mode(self, dml_effects_rendering_mode):
        """Sets the dml_effects_rendering_mode of this OdtSaveOptionsData.

        Gets or sets a value determining how DrawingML effects are rendered. { Simplified | None | Fine }.  # noqa: E501

        :param dml_effects_rendering_mode: The dml_effects_rendering_mode of this OdtSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._dml_effects_rendering_mode = dml_effects_rendering_mode
    @property
    def zip_output(self):
        """Gets the zip_output of this OdtSaveOptionsData.  # noqa: E501

        Gets or sets controls zip output or not. Default value is false.  # noqa: E501

        :return: The zip_output of this OdtSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._zip_output

    @zip_output.setter
    def zip_output(self, zip_output):
        """Sets the zip_output of this OdtSaveOptionsData.

        Gets or sets controls zip output or not. Default value is false.  # noqa: E501

        :param zip_output: The zip_output of this OdtSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._zip_output = zip_output
    @property
    def update_last_saved_time_property(self):
        """Gets the update_last_saved_time_property of this OdtSaveOptionsData.  # noqa: E501

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving.  # noqa: E501

        :return: The update_last_saved_time_property of this OdtSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_last_saved_time_property

    @update_last_saved_time_property.setter
    def update_last_saved_time_property(self, update_last_saved_time_property):
        """Sets the update_last_saved_time_property of this OdtSaveOptionsData.

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving.  # noqa: E501

        :param update_last_saved_time_property: The update_last_saved_time_property of this OdtSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_last_saved_time_property = update_last_saved_time_property
    @property
    def update_sdt_content(self):
        """Gets the update_sdt_content of this OdtSaveOptionsData.  # noqa: E501

        Gets or sets value determining whether content of StructuredDocumentTag is updated before saving.  # noqa: E501

        :return: The update_sdt_content of this OdtSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_sdt_content

    @update_sdt_content.setter
    def update_sdt_content(self, update_sdt_content):
        """Sets the update_sdt_content of this OdtSaveOptionsData.

        Gets or sets value determining whether content of StructuredDocumentTag is updated before saving.  # noqa: E501

        :param update_sdt_content: The update_sdt_content of this OdtSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_sdt_content = update_sdt_content
    @property
    def update_fields(self):
        """Gets the update_fields of this OdtSaveOptionsData.  # noqa: E501

        Gets or sets a value determining if fields should be updated before saving the document to a fixed page format. Default value for this property is. true  # noqa: E501

        :return: The update_fields of this OdtSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_fields

    @update_fields.setter
    def update_fields(self, update_fields):
        """Sets the update_fields of this OdtSaveOptionsData.

        Gets or sets a value determining if fields should be updated before saving the document to a fixed page format. Default value for this property is. true  # noqa: E501

        :param update_fields: The update_fields of this OdtSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_fields = update_fields
    @property
    def is_strict_schema11(self):
        """Gets the is_strict_schema11 of this OdtSaveOptionsData.  # noqa: E501

        Gets or sets specifies whether export should correspond to ODT specification 1.1 strictly.  # noqa: E501

        :return: The is_strict_schema11 of this OdtSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._is_strict_schema11

    @is_strict_schema11.setter
    def is_strict_schema11(self, is_strict_schema11):
        """Sets the is_strict_schema11 of this OdtSaveOptionsData.

        Gets or sets specifies whether export should correspond to ODT specification 1.1 strictly.  # noqa: E501

        :param is_strict_schema11: The is_strict_schema11 of this OdtSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._is_strict_schema11 = is_strict_schema11
    @property
    def measure_unit(self):
        """Gets the measure_unit of this OdtSaveOptionsData.  # noqa: E501

        Gets or sets allows to specify units of measure to apply to document content. The default value is Aspose.Words.Saving.OdtSaveMeasureUnit.Centimeters.  Open Office uses centimeters when specifying lengths, widths and other measurable formatting and content properties in documents whereas MS Office uses inches.  # noqa: E501

        :return: The measure_unit of this OdtSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._measure_unit

    @measure_unit.setter
    def measure_unit(self, measure_unit):
        """Sets the measure_unit of this OdtSaveOptionsData.

        Gets or sets allows to specify units of measure to apply to document content. The default value is Aspose.Words.Saving.OdtSaveMeasureUnit.Centimeters.  Open Office uses centimeters when specifying lengths, widths and other measurable formatting and content properties in documents whereas MS Office uses inches.  # noqa: E501

        :param measure_unit: The measure_unit of this OdtSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Centimeters", "Inches"]  # noqa: E501
        if not measure_unit.isdigit():	
            if measure_unit not in allowed_values:
                raise ValueError(
                    "Invalid value for `measure_unit` ({0}), must be one of {1}"  # noqa: E501
                    .format(measure_unit, allowed_values))
            self._measure_unit = measure_unit
        else:
            self._measure_unit = allowed_values[int(measure_unit) if six.PY3 else long(measure_unit)]
    @property
    def pretty_format(self):
        """Gets the pretty_format of this OdtSaveOptionsData.  # noqa: E501

        Gets or sets specifies whether or not use pretty formats output.  # noqa: E501

        :return: The pretty_format of this OdtSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._pretty_format

    @pretty_format.setter
    def pretty_format(self, pretty_format):
        """Sets the pretty_format of this OdtSaveOptionsData.

        Gets or sets specifies whether or not use pretty formats output.  # noqa: E501

        :param pretty_format: The pretty_format of this OdtSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._pretty_format = pretty_format
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
        if not isinstance(other, OdtSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
