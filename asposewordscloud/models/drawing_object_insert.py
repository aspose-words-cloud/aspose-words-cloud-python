# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="drawing_object_insert.py">
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

class DrawingObjectInsert(object):
    """Drawing object element for insert.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'height': 'float',
        'left': 'float',
        'position': 'DocumentPosition',
        'relative_horizontal_position': 'str',
        'relative_vertical_position': 'str',
        'top': 'float',
        'width': 'float',
        'wrap_type': 'str'
    }

    attribute_map = {
        'height': 'Height',
        'left': 'Left',
        'position': 'Position',
        'relative_horizontal_position': 'RelativeHorizontalPosition',
        'relative_vertical_position': 'RelativeVerticalPosition',
        'top': 'Top',
        'width': 'Width',
        'wrap_type': 'WrapType'
    }

    def __init__(self, height=None, left=None, position=None, relative_horizontal_position=None, relative_vertical_position=None, top=None, width=None, wrap_type=None):  # noqa: E501
        """DrawingObjectInsert - a model defined in Swagger"""  # noqa: E501

        self._height = None
        self._left = None
        self._position = None
        self._relative_horizontal_position = None
        self._relative_vertical_position = None
        self._top = None
        self._width = None
        self._wrap_type = None
        self.discriminator = None

        if height is not None:
            self.height = height
        if left is not None:
            self.left = left
        if position is not None:
            self.position = position
        if relative_horizontal_position is not None:
            self.relative_horizontal_position = relative_horizontal_position
        if relative_vertical_position is not None:
            self.relative_vertical_position = relative_vertical_position
        if top is not None:
            self.top = top
        if width is not None:
            self.width = width
        if wrap_type is not None:
            self.wrap_type = wrap_type

    @property
    def height(self):
        """Gets the height of this DrawingObjectInsert.  # noqa: E501

        Gets or sets the height of the DrawingObject in points.  # noqa: E501

        :return: The height of this DrawingObjectInsert.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this DrawingObjectInsert.

        Gets or sets the height of the DrawingObject in points.  # noqa: E501

        :param height: The height of this DrawingObjectInsert.  # noqa: E501
        :type: float
        """
        self._height = height

    @property
    def left(self):
        """Gets the left of this DrawingObjectInsert.  # noqa: E501

        Gets or sets the distance in points from the origin to the left side of the image.  # noqa: E501

        :return: The left of this DrawingObjectInsert.  # noqa: E501
        :rtype: float
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this DrawingObjectInsert.

        Gets or sets the distance in points from the origin to the left side of the image.  # noqa: E501

        :param left: The left of this DrawingObjectInsert.  # noqa: E501
        :type: float
        """
        self._left = left

    @property
    def position(self):
        """Gets the position of this DrawingObjectInsert.  # noqa: E501

        Gets or sets the position, before which the DrawingObject will be inserted.  # noqa: E501

        :return: The position of this DrawingObjectInsert.  # noqa: E501
        :rtype: DocumentPosition
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this DrawingObjectInsert.

        Gets or sets the position, before which the DrawingObject will be inserted.  # noqa: E501

        :param position: The position of this DrawingObjectInsert.  # noqa: E501
        :type: DocumentPosition
        """
        self._position = position

    @property
    def relative_horizontal_position(self):
        """Gets the relative_horizontal_position of this DrawingObjectInsert.  # noqa: E501

        Gets or sets the relative horizontal position, from which the distance to the image is measured.  # noqa: E501

        :return: The relative_horizontal_position of this DrawingObjectInsert.  # noqa: E501
        :rtype: str
        """
        return self._relative_horizontal_position

    @relative_horizontal_position.setter
    def relative_horizontal_position(self, relative_horizontal_position):
        """Sets the relative_horizontal_position of this DrawingObjectInsert.

        Gets or sets the relative horizontal position, from which the distance to the image is measured.  # noqa: E501

        :param relative_horizontal_position: The relative_horizontal_position of this DrawingObjectInsert.  # noqa: E501
        :type: str
        """
        allowed_values = ["Margin", "Page", "Column", "Default", "Character", "LeftMargin", "RightMargin", "InsideMargin", "OutsideMargin"]  # noqa: E501
        if not relative_horizontal_position.isdigit():
            if relative_horizontal_position not in allowed_values:
                raise ValueError(
                    "Invalid value for `relative_horizontal_position` ({0}), must be one of {1}"  # noqa: E501
                    .format(relative_horizontal_position, allowed_values))
            self._relative_horizontal_position = relative_horizontal_position
        else:
            self._relative_horizontal_position = allowed_values[int(relative_horizontal_position) if six.PY3 else long(relative_horizontal_position)]

    @property
    def relative_vertical_position(self):
        """Gets the relative_vertical_position of this DrawingObjectInsert.  # noqa: E501

        Gets or sets the relative vertical position, from which the distance to the image is measured.  # noqa: E501

        :return: The relative_vertical_position of this DrawingObjectInsert.  # noqa: E501
        :rtype: str
        """
        return self._relative_vertical_position

    @relative_vertical_position.setter
    def relative_vertical_position(self, relative_vertical_position):
        """Sets the relative_vertical_position of this DrawingObjectInsert.

        Gets or sets the relative vertical position, from which the distance to the image is measured.  # noqa: E501

        :param relative_vertical_position: The relative_vertical_position of this DrawingObjectInsert.  # noqa: E501
        :type: str
        """
        allowed_values = ["Margin", "TableDefault", "Page", "Paragraph", "TextFrameDefault", "Line", "TopMargin", "BottomMargin", "InsideMargin", "OutsideMargin"]  # noqa: E501
        if not relative_vertical_position.isdigit():
            if relative_vertical_position not in allowed_values:
                raise ValueError(
                    "Invalid value for `relative_vertical_position` ({0}), must be one of {1}"  # noqa: E501
                    .format(relative_vertical_position, allowed_values))
            self._relative_vertical_position = relative_vertical_position
        else:
            self._relative_vertical_position = allowed_values[int(relative_vertical_position) if six.PY3 else long(relative_vertical_position)]

    @property
    def top(self):
        """Gets the top of this DrawingObjectInsert.  # noqa: E501

        Gets or sets the distance in points from the origin to the top side of the image.  # noqa: E501

        :return: The top of this DrawingObjectInsert.  # noqa: E501
        :rtype: float
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this DrawingObjectInsert.

        Gets or sets the distance in points from the origin to the top side of the image.  # noqa: E501

        :param top: The top of this DrawingObjectInsert.  # noqa: E501
        :type: float
        """
        self._top = top

    @property
    def width(self):
        """Gets the width of this DrawingObjectInsert.  # noqa: E501

        Gets or sets the width of the DrawingObjects in points.  # noqa: E501

        :return: The width of this DrawingObjectInsert.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this DrawingObjectInsert.

        Gets or sets the width of the DrawingObjects in points.  # noqa: E501

        :param width: The width of this DrawingObjectInsert.  # noqa: E501
        :type: float
        """
        self._width = width

    @property
    def wrap_type(self):
        """Gets the wrap_type of this DrawingObjectInsert.  # noqa: E501

        Gets or sets the option indicating how to wrap text around the image.  # noqa: E501

        :return: The wrap_type of this DrawingObjectInsert.  # noqa: E501
        :rtype: str
        """
        return self._wrap_type

    @wrap_type.setter
    def wrap_type(self, wrap_type):
        """Sets the wrap_type of this DrawingObjectInsert.

        Gets or sets the option indicating how to wrap text around the image.  # noqa: E501

        :param wrap_type: The wrap_type of this DrawingObjectInsert.  # noqa: E501
        :type: str
        """
        allowed_values = ["Inline", "TopBottom", "Square", "None", "Tight", "Through"]  # noqa: E501
        if not wrap_type.isdigit():
            if wrap_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `wrap_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(wrap_type, allowed_values))
            self._wrap_type = wrap_type
        else:
            self._wrap_type = allowed_values[int(wrap_type) if six.PY3 else long(wrap_type)]


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
        if not isinstance(other, DrawingObjectInsert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other