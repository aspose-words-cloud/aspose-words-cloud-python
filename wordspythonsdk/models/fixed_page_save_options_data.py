# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="FixedPageSaveOptionsData.py">
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


class FixedPageSaveOptionsData(object):
    """Contains common options that can be specified when saving a document into fixed page formats (PDF, XPS, images etc).
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'jpeg_quality': 'int',
        'metafile_rendering_options': 'MetafileRenderingOptionsData',
        'numeral_format': 'str',
        'optimize_output': 'bool',
        'page_count': 'int',
        'page_index': 'int'
    }

    attribute_map = {
        'jpeg_quality': 'JpegQuality',
        'metafile_rendering_options': 'MetafileRenderingOptions',
        'numeral_format': 'NumeralFormat',
        'optimize_output': 'OptimizeOutput',
        'page_count': 'PageCount',
        'page_index': 'PageIndex'
    }

    def __init__(self, jpeg_quality=None, metafile_rendering_options=None, numeral_format=None, optimize_output=None, page_count=None, page_index=None):  # noqa: E501
        """FixedPageSaveOptionsData - a model defined in Swagger"""  # noqa: E501

        self._jpeg_quality = None
        self._metafile_rendering_options = None
        self._numeral_format = None
        self._optimize_output = None
        self._page_count = None
        self._page_index = None
        self.discriminator = None

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

    @property
    def jpeg_quality(self):
        """Gets the jpeg_quality of this FixedPageSaveOptionsData.  # noqa: E501

        Determines the quality of the JPEG images inside PDF document.  # noqa: E501

        :return: The jpeg_quality of this FixedPageSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._jpeg_quality

    @jpeg_quality.setter
    def jpeg_quality(self, jpeg_quality):
        """Sets the jpeg_quality of this FixedPageSaveOptionsData.

        Determines the quality of the JPEG images inside PDF document.  # noqa: E501

        :param jpeg_quality: The jpeg_quality of this FixedPageSaveOptionsData.  # noqa: E501
        :type: int
        """

        self._jpeg_quality = jpeg_quality

    @property
    def metafile_rendering_options(self):
        """Gets the metafile_rendering_options of this FixedPageSaveOptionsData.  # noqa: E501

        Allows to specify metafile rendering options.  # noqa: E501

        :return: The metafile_rendering_options of this FixedPageSaveOptionsData.  # noqa: E501
        :rtype: MetafileRenderingOptionsData
        """
        return self._metafile_rendering_options

    @metafile_rendering_options.setter
    def metafile_rendering_options(self, metafile_rendering_options):
        """Sets the metafile_rendering_options of this FixedPageSaveOptionsData.

        Allows to specify metafile rendering options.  # noqa: E501

        :param metafile_rendering_options: The metafile_rendering_options of this FixedPageSaveOptionsData.  # noqa: E501
        :type: MetafileRenderingOptionsData
        """

        self._metafile_rendering_options = metafile_rendering_options

    @property
    def numeral_format(self):
        """Gets the numeral_format of this FixedPageSaveOptionsData.  # noqa: E501

        Indicates the symbol set that is used to represent numbers while rendering to fixed page formats  # noqa: E501

        :return: The numeral_format of this FixedPageSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._numeral_format

    @numeral_format.setter
    def numeral_format(self, numeral_format):
        """Sets the numeral_format of this FixedPageSaveOptionsData.

        Indicates the symbol set that is used to represent numbers while rendering to fixed page formats  # noqa: E501

        :param numeral_format: The numeral_format of this FixedPageSaveOptionsData.  # noqa: E501
        :type: str
        """

        self._numeral_format = numeral_format

    @property
    def optimize_output(self):
        """Gets the optimize_output of this FixedPageSaveOptionsData.  # noqa: E501

        Flag indicates whether it is required to optimize output of XPS.  If this flag is set redundant nested canvases and empty canvases are removed, also neighbor glyphs with the same formatting are concatenated.  Note: The accuracy of the content display may be affected if this property is set to true.  Default is false.  # noqa: E501

        :return: The optimize_output of this FixedPageSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._optimize_output

    @optimize_output.setter
    def optimize_output(self, optimize_output):
        """Sets the optimize_output of this FixedPageSaveOptionsData.

        Flag indicates whether it is required to optimize output of XPS.  If this flag is set redundant nested canvases and empty canvases are removed, also neighbor glyphs with the same formatting are concatenated.  Note: The accuracy of the content display may be affected if this property is set to true.  Default is false.  # noqa: E501

        :param optimize_output: The optimize_output of this FixedPageSaveOptionsData.  # noqa: E501
        :type: bool
        """

        self._optimize_output = optimize_output

    @property
    def page_count(self):
        """Gets the page_count of this FixedPageSaveOptionsData.  # noqa: E501

        Determines number of pages to render  # noqa: E501

        :return: The page_count of this FixedPageSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this FixedPageSaveOptionsData.

        Determines number of pages to render  # noqa: E501

        :param page_count: The page_count of this FixedPageSaveOptionsData.  # noqa: E501
        :type: int
        """

        self._page_count = page_count

    @property
    def page_index(self):
        """Gets the page_index of this FixedPageSaveOptionsData.  # noqa: E501

        Determines 0-based index of the first page to render  # noqa: E501

        :return: The page_index of this FixedPageSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """Sets the page_index of this FixedPageSaveOptionsData.

        Determines 0-based index of the first page to render  # noqa: E501

        :param page_index: The page_index of this FixedPageSaveOptionsData.  # noqa: E501
        :type: int
        """

        self._page_index = page_index

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
        if not isinstance(other, FixedPageSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
