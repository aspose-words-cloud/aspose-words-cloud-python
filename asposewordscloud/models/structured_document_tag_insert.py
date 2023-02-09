# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="structured_document_tag_insert.py">
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

class StructuredDocumentTagInsert(object):
    """DTO container with a StructuredDocumentTag.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'link': 'WordsApiLink',
        'node_id': 'str',
        'appearance': 'str',
        'building_block_category': 'str',
        'building_block_gallery': 'str',
        'calendar_type': 'str',
        'checked': 'bool',
        'color': 'str',
        'date_display_format': 'str',
        'date_display_locale': 'int',
        'date_storage_format': 'str',
        'full_date': 'datetime',
        'id': 'int',
        'is_showing_placeholder_text': 'bool',
        'is_temporary': 'bool',
        'level': 'str',
        'list_items': 'list[StructuredDocumentTagListItem]',
        'lock_content_control': 'bool',
        'lock_contents': 'bool',
        'multiline': 'bool',
        'placeholder_name': 'str',
        'sdt_type': 'str',
        'style_name': 'str',
        'tag': 'str',
        'title': 'str',
        'word_open_xml': 'str'
    }

    attribute_map = {
        'link': 'Link',
        'node_id': 'NodeId',
        'appearance': 'Appearance',
        'building_block_category': 'BuildingBlockCategory',
        'building_block_gallery': 'BuildingBlockGallery',
        'calendar_type': 'CalendarType',
        'checked': 'Checked',
        'color': 'Color',
        'date_display_format': 'DateDisplayFormat',
        'date_display_locale': 'DateDisplayLocale',
        'date_storage_format': 'DateStorageFormat',
        'full_date': 'FullDate',
        'id': 'Id',
        'is_showing_placeholder_text': 'IsShowingPlaceholderText',
        'is_temporary': 'IsTemporary',
        'level': 'Level',
        'list_items': 'ListItems',
        'lock_content_control': 'LockContentControl',
        'lock_contents': 'LockContents',
        'multiline': 'Multiline',
        'placeholder_name': 'PlaceholderName',
        'sdt_type': 'SdtType',
        'style_name': 'StyleName',
        'tag': 'Tag',
        'title': 'Title',
        'word_open_xml': 'WordOpenXML'
    }

    def __init__(self, link=None, node_id=None, appearance=None, building_block_category=None, building_block_gallery=None, calendar_type=None, checked=None, color=None, date_display_format=None, date_display_locale=None, date_storage_format=None, full_date=None, id=None, is_showing_placeholder_text=None, is_temporary=None, level=None, list_items=None, lock_content_control=None, lock_contents=None, multiline=None, placeholder_name=None, sdt_type=None, style_name=None, tag=None, title=None, word_open_xml=None):  # noqa: E501
        """StructuredDocumentTagInsert - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._node_id = None
        self._appearance = None
        self._building_block_category = None
        self._building_block_gallery = None
        self._calendar_type = None
        self._checked = None
        self._color = None
        self._date_display_format = None
        self._date_display_locale = None
        self._date_storage_format = None
        self._full_date = None
        self._id = None
        self._is_showing_placeholder_text = None
        self._is_temporary = None
        self._level = None
        self._list_items = None
        self._lock_content_control = None
        self._lock_contents = None
        self._multiline = None
        self._placeholder_name = None
        self._sdt_type = None
        self._style_name = None
        self._tag = None
        self._title = None
        self._word_open_xml = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if node_id is not None:
            self.node_id = node_id
        if appearance is not None:
            self.appearance = appearance
        if building_block_category is not None:
            self.building_block_category = building_block_category
        if building_block_gallery is not None:
            self.building_block_gallery = building_block_gallery
        if calendar_type is not None:
            self.calendar_type = calendar_type
        if checked is not None:
            self.checked = checked
        if color is not None:
            self.color = color
        if date_display_format is not None:
            self.date_display_format = date_display_format
        if date_display_locale is not None:
            self.date_display_locale = date_display_locale
        if date_storage_format is not None:
            self.date_storage_format = date_storage_format
        if full_date is not None:
            self.full_date = full_date
        if id is not None:
            self.id = id
        if is_showing_placeholder_text is not None:
            self.is_showing_placeholder_text = is_showing_placeholder_text
        if is_temporary is not None:
            self.is_temporary = is_temporary
        if level is not None:
            self.level = level
        if list_items is not None:
            self.list_items = list_items
        if lock_content_control is not None:
            self.lock_content_control = lock_content_control
        if lock_contents is not None:
            self.lock_contents = lock_contents
        if multiline is not None:
            self.multiline = multiline
        if placeholder_name is not None:
            self.placeholder_name = placeholder_name
        if sdt_type is not None:
            self.sdt_type = sdt_type
        if style_name is not None:
            self.style_name = style_name
        if tag is not None:
            self.tag = tag
        if title is not None:
            self.title = title
        if word_open_xml is not None:
            self.word_open_xml = word_open_xml

    @property
    def link(self):
        """Gets the link of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The link of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this StructuredDocumentTagInsert.

        Gets or sets the link to the document.  # noqa: E501

        :param link: The link of this StructuredDocumentTagInsert.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link

    @property
    def node_id(self):
        """Gets the node_id of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets the node id.  # noqa: E501

        :return: The node_id of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this StructuredDocumentTagInsert.

        Gets or sets the node id.  # noqa: E501

        :param node_id: The node_id of this StructuredDocumentTagInsert.  # noqa: E501
        :type: str
        """
        self._node_id = node_id

    @property
    def appearance(self):
        """Gets the appearance of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets the appearance of a structured document tag.  # noqa: E501

        :return: The appearance of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: str
        """
        return self._appearance

    @appearance.setter
    def appearance(self, appearance):
        """Sets the appearance of this StructuredDocumentTagInsert.

        Gets or sets the appearance of a structured document tag.  # noqa: E501

        :param appearance: The appearance of this StructuredDocumentTagInsert.  # noqa: E501
        :type: str
        """
        allowed_values = ["Default", "BoundingBox", "Tags", "Hidden"]  # noqa: E501
        if not appearance.isdigit():
            if appearance not in allowed_values:
                raise ValueError(
                    "Invalid value for `appearance` ({0}), must be one of {1}"  # noqa: E501
                    .format(appearance, allowed_values))
            self._appearance = appearance
        else:
            self._appearance = allowed_values[int(appearance) if six.PY3 else long(appearance)]

    @property
    def building_block_category(self):
        """Gets the building_block_category of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets category of building block for this SDT node. Can not be null.  # noqa: E501

        :return: The building_block_category of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: str
        """
        return self._building_block_category

    @building_block_category.setter
    def building_block_category(self, building_block_category):
        """Sets the building_block_category of this StructuredDocumentTagInsert.

        Gets or sets category of building block for this SDT node. Can not be null.  # noqa: E501

        :param building_block_category: The building_block_category of this StructuredDocumentTagInsert.  # noqa: E501
        :type: str
        """
        self._building_block_category = building_block_category

    @property
    def building_block_gallery(self):
        """Gets the building_block_gallery of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets type of building block for this SDT. Can not be null.  # noqa: E501

        :return: The building_block_gallery of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: str
        """
        return self._building_block_gallery

    @building_block_gallery.setter
    def building_block_gallery(self, building_block_gallery):
        """Sets the building_block_gallery of this StructuredDocumentTagInsert.

        Gets or sets type of building block for this SDT. Can not be null.  # noqa: E501

        :param building_block_gallery: The building_block_gallery of this StructuredDocumentTagInsert.  # noqa: E501
        :type: str
        """
        self._building_block_gallery = building_block_gallery

    @property
    def calendar_type(self):
        """Gets the calendar_type of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets the type of calendar for this SDT. Default is Aspose.Words.Markup.SdtCalendarType.Default.  # noqa: E501

        :return: The calendar_type of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: str
        """
        return self._calendar_type

    @calendar_type.setter
    def calendar_type(self, calendar_type):
        """Sets the calendar_type of this StructuredDocumentTagInsert.

        Gets or sets the type of calendar for this SDT. Default is Aspose.Words.Markup.SdtCalendarType.Default.  # noqa: E501

        :param calendar_type: The calendar_type of this StructuredDocumentTagInsert.  # noqa: E501
        :type: str
        """
        allowed_values = ["Default", "Gregorian", "GregorianArabic", "GregorianMeFrench", "GregorianUs", "GregorianXlitEnglish", "GregorianXlitFrench", "Hebrew", "Hijri", "Japan", "Korea", "None", "Saka", "Taiwan", "Thai"]  # noqa: E501
        if not calendar_type.isdigit():
            if calendar_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `calendar_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(calendar_type, allowed_values))
            self._calendar_type = calendar_type
        else:
            self._calendar_type = allowed_values[int(calendar_type) if six.PY3 else long(calendar_type)]

    @property
    def checked(self):
        """Gets the checked of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets a value indicating whether current state of the Checkbox SDT. Default value for this property.  # noqa: E501

        :return: The checked of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: bool
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        """Sets the checked of this StructuredDocumentTagInsert.

        Gets or sets a value indicating whether current state of the Checkbox SDT. Default value for this property.  # noqa: E501

        :param checked: The checked of this StructuredDocumentTagInsert.  # noqa: E501
        :type: bool
        """
        self._checked = checked

    @property
    def color(self):
        """Gets the color of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets the color of the structured document tag.  # noqa: E501

        :return: The color of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this StructuredDocumentTagInsert.

        Gets or sets the color of the structured document tag.  # noqa: E501

        :param color: The color of this StructuredDocumentTagInsert.  # noqa: E501
        :type: str
        """
        self._color = color

    @property
    def date_display_format(self):
        """Gets the date_display_format of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets String that represents the format in which dates are displayed. Can not be null. The dates for English (U.S.) is "mm/dd/yyyy".  # noqa: E501

        :return: The date_display_format of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: str
        """
        return self._date_display_format

    @date_display_format.setter
    def date_display_format(self, date_display_format):
        """Sets the date_display_format of this StructuredDocumentTagInsert.

        Gets or sets String that represents the format in which dates are displayed. Can not be null. The dates for English (U.S.) is "mm/dd/yyyy".  # noqa: E501

        :param date_display_format: The date_display_format of this StructuredDocumentTagInsert.  # noqa: E501
        :type: str
        """
        self._date_display_format = date_display_format

    @property
    def date_display_locale(self):
        """Gets the date_display_locale of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets the language format for the date displayed in this SDT.  # noqa: E501

        :return: The date_display_locale of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: int
        """
        return self._date_display_locale

    @date_display_locale.setter
    def date_display_locale(self, date_display_locale):
        """Sets the date_display_locale of this StructuredDocumentTagInsert.

        Gets or sets the language format for the date displayed in this SDT.  # noqa: E501

        :param date_display_locale: The date_display_locale of this StructuredDocumentTagInsert.  # noqa: E501
        :type: int
        """
        self._date_display_locale = date_display_locale

    @property
    def date_storage_format(self):
        """Gets the date_storage_format of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets format in which the date for a date SDT is stored when the SDT is bound to an XML node in the document's data store. Default value is Aspose.Words.Markup.SdtDateStorageFormat.DateTime.  # noqa: E501

        :return: The date_storage_format of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: str
        """
        return self._date_storage_format

    @date_storage_format.setter
    def date_storage_format(self, date_storage_format):
        """Sets the date_storage_format of this StructuredDocumentTagInsert.

        Gets or sets format in which the date for a date SDT is stored when the SDT is bound to an XML node in the document's data store. Default value is Aspose.Words.Markup.SdtDateStorageFormat.DateTime.  # noqa: E501

        :param date_storage_format: The date_storage_format of this StructuredDocumentTagInsert.  # noqa: E501
        :type: str
        """
        allowed_values = ["Date", "DateTime", "Default", "Text"]  # noqa: E501
        if not date_storage_format.isdigit():
            if date_storage_format not in allowed_values:
                raise ValueError(
                    "Invalid value for `date_storage_format` ({0}), must be one of {1}"  # noqa: E501
                    .format(date_storage_format, allowed_values))
            self._date_storage_format = date_storage_format
        else:
            self._date_storage_format = allowed_values[int(date_storage_format) if six.PY3 else long(date_storage_format)]

    @property
    def full_date(self):
        """Gets the full_date of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets the full date and time last entered into this SDT.  # noqa: E501

        :return: The full_date of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: datetime
        """
        return self._full_date

    @full_date.setter
    def full_date(self, full_date):
        """Sets the full_date of this StructuredDocumentTagInsert.

        Gets or sets the full date and time last entered into this SDT.  # noqa: E501

        :param full_date: The full_date of this StructuredDocumentTagInsert.  # noqa: E501
        :type: datetime
        """
        self._full_date = full_date

    @property
    def id(self):
        """Gets the id of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets a unique read-only persistent numerical Id for this SDT.  # noqa: E501

        :return: The id of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StructuredDocumentTagInsert.

        Gets or sets a unique read-only persistent numerical Id for this SDT.  # noqa: E501

        :param id: The id of this StructuredDocumentTagInsert.  # noqa: E501
        :type: int
        """
        self._id = id

    @property
    def is_showing_placeholder_text(self):
        """Gets the is_showing_placeholder_text of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets a value indicating whether the content of this SDT shall be interpreted to contain placeholder text (as opposed to regular text contents within the SDT). If set to true, this state shall be resumed (showing placeholder text) upon opening his document.  # noqa: E501

        :return: The is_showing_placeholder_text of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: bool
        """
        return self._is_showing_placeholder_text

    @is_showing_placeholder_text.setter
    def is_showing_placeholder_text(self, is_showing_placeholder_text):
        """Sets the is_showing_placeholder_text of this StructuredDocumentTagInsert.

        Gets or sets a value indicating whether the content of this SDT shall be interpreted to contain placeholder text (as opposed to regular text contents within the SDT). If set to true, this state shall be resumed (showing placeholder text) upon opening his document.  # noqa: E501

        :param is_showing_placeholder_text: The is_showing_placeholder_text of this StructuredDocumentTagInsert.  # noqa: E501
        :type: bool
        """
        self._is_showing_placeholder_text = is_showing_placeholder_text

    @property
    def is_temporary(self):
        """Gets the is_temporary of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets a value indicating whether this SDT shall be removed from the WordProcessingML document when its contents are modified.  # noqa: E501

        :return: The is_temporary of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: bool
        """
        return self._is_temporary

    @is_temporary.setter
    def is_temporary(self, is_temporary):
        """Sets the is_temporary of this StructuredDocumentTagInsert.

        Gets or sets a value indicating whether this SDT shall be removed from the WordProcessingML document when its contents are modified.  # noqa: E501

        :param is_temporary: The is_temporary of this StructuredDocumentTagInsert.  # noqa: E501
        :type: bool
        """
        self._is_temporary = is_temporary

    @property
    def level(self):
        """Gets the level of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets the level at which this SDT occurs in the document tree.  # noqa: E501

        :return: The level of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this StructuredDocumentTagInsert.

        Gets or sets the level at which this SDT occurs in the document tree.  # noqa: E501

        :param level: The level of this StructuredDocumentTagInsert.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unknown", "Inline", "Block", "Row", "Cell"]  # noqa: E501
        if not level.isdigit():
            if level not in allowed_values:
                raise ValueError(
                    "Invalid value for `level` ({0}), must be one of {1}"  # noqa: E501
                    .format(level, allowed_values))
            self._level = level
        else:
            self._level = allowed_values[int(level) if six.PY3 else long(level)]

    @property
    def list_items(self):
        """Gets the list_items of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets Aspose.Words.Markup.SdtListItemCollection associated with this SDT.  # noqa: E501

        :return: The list_items of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: list[StructuredDocumentTagListItem]
        """
        return self._list_items

    @list_items.setter
    def list_items(self, list_items):
        """Sets the list_items of this StructuredDocumentTagInsert.

        Gets or sets Aspose.Words.Markup.SdtListItemCollection associated with this SDT.  # noqa: E501

        :param list_items: The list_items of this StructuredDocumentTagInsert.  # noqa: E501
        :type: list[StructuredDocumentTagListItem]
        """
        self._list_items = list_items

    @property
    def lock_content_control(self):
        """Gets the lock_content_control of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets a value indicating whether, this property will prohibit a user from deleting this SDT.  # noqa: E501

        :return: The lock_content_control of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: bool
        """
        return self._lock_content_control

    @lock_content_control.setter
    def lock_content_control(self, lock_content_control):
        """Sets the lock_content_control of this StructuredDocumentTagInsert.

        Gets or sets a value indicating whether, this property will prohibit a user from deleting this SDT.  # noqa: E501

        :param lock_content_control: The lock_content_control of this StructuredDocumentTagInsert.  # noqa: E501
        :type: bool
        """
        self._lock_content_control = lock_content_control

    @property
    def lock_contents(self):
        """Gets the lock_contents of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets a value indicating whether, this property will prohibit a user from editing the contents of this SDT.  # noqa: E501

        :return: The lock_contents of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: bool
        """
        return self._lock_contents

    @lock_contents.setter
    def lock_contents(self, lock_contents):
        """Sets the lock_contents of this StructuredDocumentTagInsert.

        Gets or sets a value indicating whether, this property will prohibit a user from editing the contents of this SDT.  # noqa: E501

        :param lock_contents: The lock_contents of this StructuredDocumentTagInsert.  # noqa: E501
        :type: bool
        """
        self._lock_contents = lock_contents

    @property
    def multiline(self):
        """Gets the multiline of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets a value indicating whether this SDT allows multiple lines of text.  # noqa: E501

        :return: The multiline of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: bool
        """
        return self._multiline

    @multiline.setter
    def multiline(self, multiline):
        """Sets the multiline of this StructuredDocumentTagInsert.

        Gets or sets a value indicating whether this SDT allows multiple lines of text.  # noqa: E501

        :param multiline: The multiline of this StructuredDocumentTagInsert.  # noqa: E501
        :type: bool
        """
        self._multiline = multiline

    @property
    def placeholder_name(self):
        """Gets the placeholder_name of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets Name of the Aspose.Words.BuildingBlocks.BuildingBlock containing placeholder text. Aspose.Words.BuildingBlocks.BuildingBlock with this name Aspose.Words.BuildingBlocks.BuildingBlock.Name has to be present in the Aspose.Words.Document.GlossaryDocument otherwise System.InvalidOperationException will occur.  # noqa: E501

        :return: The placeholder_name of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: str
        """
        return self._placeholder_name

    @placeholder_name.setter
    def placeholder_name(self, placeholder_name):
        """Sets the placeholder_name of this StructuredDocumentTagInsert.

        Gets or sets Name of the Aspose.Words.BuildingBlocks.BuildingBlock containing placeholder text. Aspose.Words.BuildingBlocks.BuildingBlock with this name Aspose.Words.BuildingBlocks.BuildingBlock.Name has to be present in the Aspose.Words.Document.GlossaryDocument otherwise System.InvalidOperationException will occur.  # noqa: E501

        :param placeholder_name: The placeholder_name of this StructuredDocumentTagInsert.  # noqa: E501
        :type: str
        """
        self._placeholder_name = placeholder_name

    @property
    def sdt_type(self):
        """Gets the sdt_type of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets type of this Structured document tag.  # noqa: E501

        :return: The sdt_type of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: str
        """
        return self._sdt_type

    @sdt_type.setter
    def sdt_type(self, sdt_type):
        """Sets the sdt_type of this StructuredDocumentTagInsert.

        Gets or sets type of this Structured document tag.  # noqa: E501

        :param sdt_type: The sdt_type of this StructuredDocumentTagInsert.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Bibliography", "Citation", "Equation", "DropDownList", "ComboBox", "Date", "BuildingBlockGallery", "DocPartObj", "Group", "Picture", "RichText", "PlainText", "Checkbox", "RepeatingSection", "RepeatingSectionItem", "EntityPicker"]  # noqa: E501
        if not sdt_type.isdigit():
            if sdt_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `sdt_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(sdt_type, allowed_values))
            self._sdt_type = sdt_type
        else:
            self._sdt_type = allowed_values[int(sdt_type) if six.PY3 else long(sdt_type)]

    @property
    def style_name(self):
        """Gets the style_name of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets the name of the style applied to the structured document tag.  # noqa: E501

        :return: The style_name of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: str
        """
        return self._style_name

    @style_name.setter
    def style_name(self, style_name):
        """Sets the style_name of this StructuredDocumentTagInsert.

        Gets or sets the name of the style applied to the structured document tag.  # noqa: E501

        :param style_name: The style_name of this StructuredDocumentTagInsert.  # noqa: E501
        :type: str
        """
        self._style_name = style_name

    @property
    def tag(self):
        """Gets the tag of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets a tag associated with the current SDT node. Can not be null.  # noqa: E501

        :return: The tag of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this StructuredDocumentTagInsert.

        Gets or sets a tag associated with the current SDT node. Can not be null.  # noqa: E501

        :param tag: The tag of this StructuredDocumentTagInsert.  # noqa: E501
        :type: str
        """
        self._tag = tag

    @property
    def title(self):
        """Gets the title of this StructuredDocumentTagInsert.  # noqa: E501

        Gets or sets the friendly name associated with this SDT. Can not be null.  # noqa: E501

        :return: The title of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this StructuredDocumentTagInsert.

        Gets or sets the friendly name associated with this SDT. Can not be null.  # noqa: E501

        :param title: The title of this StructuredDocumentTagInsert.  # noqa: E501
        :type: str
        """
        self._title = title

    @property
    def word_open_xml(self):
        """Gets the word_open_xml of this StructuredDocumentTagInsert.  # noqa: E501

        Gets a string that represents the XML contained within the node in the Aspose.Words.SaveFormat.FlatOpc format.  # noqa: E501

        :return: The word_open_xml of this StructuredDocumentTagInsert.  # noqa: E501
        :rtype: str
        """
        return self._word_open_xml

    @word_open_xml.setter
    def word_open_xml(self, word_open_xml):
        """Sets the word_open_xml of this StructuredDocumentTagInsert.

        Gets a string that represents the XML contained within the node in the Aspose.Words.SaveFormat.FlatOpc format.  # noqa: E501

        :param word_open_xml: The word_open_xml of this StructuredDocumentTagInsert.  # noqa: E501
        :type: str
        """
        self._word_open_xml = word_open_xml


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
        if not isinstance(other, StructuredDocumentTagInsert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other