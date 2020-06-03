# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="CompareOptions.py">
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


class CompareOptions(object):
    """Container class for compare documents options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ignore_case_changes': 'bool',
        'ignore_tables': 'bool',
        'ignore_fields': 'bool',
        'ignore_footnotes': 'bool',
        'ignore_comments': 'bool',
        'ignore_textboxes': 'bool',
        'ignore_formatting': 'bool',
        'ignore_headers_and_footers': 'bool',
        'target': 'str'
    }

    attribute_map = {
        'ignore_case_changes': 'IgnoreCaseChanges',
        'ignore_tables': 'IgnoreTables',
        'ignore_fields': 'IgnoreFields',
        'ignore_footnotes': 'IgnoreFootnotes',
        'ignore_comments': 'IgnoreComments',
        'ignore_textboxes': 'IgnoreTextboxes',
        'ignore_formatting': 'IgnoreFormatting',
        'ignore_headers_and_footers': 'IgnoreHeadersAndFooters',
        'target': 'Target'
    }

    def __init__(self, ignore_case_changes=None, ignore_tables=None, ignore_fields=None, ignore_footnotes=None, ignore_comments=None, ignore_textboxes=None, ignore_formatting=None, ignore_headers_and_footers=None, target=None):  # noqa: E501
        """CompareOptions - a model defined in Swagger"""  # noqa: E501

        self._ignore_case_changes = None
        self._ignore_tables = None
        self._ignore_fields = None
        self._ignore_footnotes = None
        self._ignore_comments = None
        self._ignore_textboxes = None
        self._ignore_formatting = None
        self._ignore_headers_and_footers = None
        self._target = None
        self.discriminator = None

        if ignore_case_changes is not None:
            self.ignore_case_changes = ignore_case_changes
        if ignore_tables is not None:
            self.ignore_tables = ignore_tables
        if ignore_fields is not None:
            self.ignore_fields = ignore_fields
        if ignore_footnotes is not None:
            self.ignore_footnotes = ignore_footnotes
        if ignore_comments is not None:
            self.ignore_comments = ignore_comments
        if ignore_textboxes is not None:
            self.ignore_textboxes = ignore_textboxes
        if ignore_formatting is not None:
            self.ignore_formatting = ignore_formatting
        if ignore_headers_and_footers is not None:
            self.ignore_headers_and_footers = ignore_headers_and_footers
        if target is not None:
            self.target = target

    @property
    def ignore_case_changes(self):
        """Gets the ignore_case_changes of this CompareOptions.  # noqa: E501

        Gets or sets a value indicating whether true indicates that documents comparison is case insensitive. By default comparison is case sensitive.               # noqa: E501

        :return: The ignore_case_changes of this CompareOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_case_changes

    @ignore_case_changes.setter
    def ignore_case_changes(self, ignore_case_changes):
        """Sets the ignore_case_changes of this CompareOptions.

        Gets or sets a value indicating whether true indicates that documents comparison is case insensitive. By default comparison is case sensitive.               # noqa: E501

        :param ignore_case_changes: The ignore_case_changes of this CompareOptions.  # noqa: E501
        :type: bool
        """
        self._ignore_case_changes = ignore_case_changes
    @property
    def ignore_tables(self):
        """Gets the ignore_tables of this CompareOptions.  # noqa: E501

        Gets or sets a value indicating whether specifies whether to compare the differences in data contained in tables. By default tables are not ignored.               # noqa: E501

        :return: The ignore_tables of this CompareOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_tables

    @ignore_tables.setter
    def ignore_tables(self, ignore_tables):
        """Sets the ignore_tables of this CompareOptions.

        Gets or sets a value indicating whether specifies whether to compare the differences in data contained in tables. By default tables are not ignored.               # noqa: E501

        :param ignore_tables: The ignore_tables of this CompareOptions.  # noqa: E501
        :type: bool
        """
        self._ignore_tables = ignore_tables
    @property
    def ignore_fields(self):
        """Gets the ignore_fields of this CompareOptions.  # noqa: E501

        Gets or sets a value indicating whether specifies whether to compare differences in fields. By default fields are not ignored.               # noqa: E501

        :return: The ignore_fields of this CompareOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_fields

    @ignore_fields.setter
    def ignore_fields(self, ignore_fields):
        """Sets the ignore_fields of this CompareOptions.

        Gets or sets a value indicating whether specifies whether to compare differences in fields. By default fields are not ignored.               # noqa: E501

        :param ignore_fields: The ignore_fields of this CompareOptions.  # noqa: E501
        :type: bool
        """
        self._ignore_fields = ignore_fields
    @property
    def ignore_footnotes(self):
        """Gets the ignore_footnotes of this CompareOptions.  # noqa: E501

        Gets or sets a value indicating whether specifies whether to compare differences in footnotes and endnotes. By default footnotes are not ignored.               # noqa: E501

        :return: The ignore_footnotes of this CompareOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_footnotes

    @ignore_footnotes.setter
    def ignore_footnotes(self, ignore_footnotes):
        """Sets the ignore_footnotes of this CompareOptions.

        Gets or sets a value indicating whether specifies whether to compare differences in footnotes and endnotes. By default footnotes are not ignored.               # noqa: E501

        :param ignore_footnotes: The ignore_footnotes of this CompareOptions.  # noqa: E501
        :type: bool
        """
        self._ignore_footnotes = ignore_footnotes
    @property
    def ignore_comments(self):
        """Gets the ignore_comments of this CompareOptions.  # noqa: E501

        Gets or sets a value indicating whether specifies whether to compare differences in comments. By default comments are not ignored.               # noqa: E501

        :return: The ignore_comments of this CompareOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_comments

    @ignore_comments.setter
    def ignore_comments(self, ignore_comments):
        """Sets the ignore_comments of this CompareOptions.

        Gets or sets a value indicating whether specifies whether to compare differences in comments. By default comments are not ignored.               # noqa: E501

        :param ignore_comments: The ignore_comments of this CompareOptions.  # noqa: E501
        :type: bool
        """
        self._ignore_comments = ignore_comments
    @property
    def ignore_textboxes(self):
        """Gets the ignore_textboxes of this CompareOptions.  # noqa: E501

        Gets or sets a value indicating whether specifies whether to compare differences in the data contained within text boxes. By default textboxes are not ignored.               # noqa: E501

        :return: The ignore_textboxes of this CompareOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_textboxes

    @ignore_textboxes.setter
    def ignore_textboxes(self, ignore_textboxes):
        """Sets the ignore_textboxes of this CompareOptions.

        Gets or sets a value indicating whether specifies whether to compare differences in the data contained within text boxes. By default textboxes are not ignored.               # noqa: E501

        :param ignore_textboxes: The ignore_textboxes of this CompareOptions.  # noqa: E501
        :type: bool
        """
        self._ignore_textboxes = ignore_textboxes
    @property
    def ignore_formatting(self):
        """Gets the ignore_formatting of this CompareOptions.  # noqa: E501

        Gets or sets a value indicating whether true indicates that formatting is ignored. By default document formatting is not ignored.               # noqa: E501

        :return: The ignore_formatting of this CompareOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_formatting

    @ignore_formatting.setter
    def ignore_formatting(self, ignore_formatting):
        """Sets the ignore_formatting of this CompareOptions.

        Gets or sets a value indicating whether true indicates that formatting is ignored. By default document formatting is not ignored.               # noqa: E501

        :param ignore_formatting: The ignore_formatting of this CompareOptions.  # noqa: E501
        :type: bool
        """
        self._ignore_formatting = ignore_formatting
    @property
    def ignore_headers_and_footers(self):
        """Gets the ignore_headers_and_footers of this CompareOptions.  # noqa: E501

        Gets or sets a value indicating whether true indicates that headers and footers content is ignored. By default headers and footers are not ignored.               # noqa: E501

        :return: The ignore_headers_and_footers of this CompareOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_headers_and_footers

    @ignore_headers_and_footers.setter
    def ignore_headers_and_footers(self, ignore_headers_and_footers):
        """Sets the ignore_headers_and_footers of this CompareOptions.

        Gets or sets a value indicating whether true indicates that headers and footers content is ignored. By default headers and footers are not ignored.               # noqa: E501

        :param ignore_headers_and_footers: The ignore_headers_and_footers of this CompareOptions.  # noqa: E501
        :type: bool
        """
        self._ignore_headers_and_footers = ignore_headers_and_footers
    @property
    def target(self):
        """Gets the target of this CompareOptions.  # noqa: E501

        Gets or sets specifies which document shall be used as a target during comparison.               # noqa: E501

        :return: The target of this CompareOptions.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this CompareOptions.

        Gets or sets specifies which document shall be used as a target during comparison.               # noqa: E501

        :param target: The target of this CompareOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["Current", "New"]  # noqa: E501
        if not target.isdigit():	
            if target not in allowed_values:
                raise ValueError(
                    "Invalid value for `target` ({0}), must be one of {1}"  # noqa: E501
                    .format(target, allowed_values))
            self._target = target
        else:
            self._target = allowed_values[int(target) if six.PY3 else long(target)]
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
        if not isinstance(other, CompareOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
