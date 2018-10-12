# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="CommentsResponse.py">
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


class CommentsResponse(object):
    """This response should be returned by the service when handling: GET http://api.aspose.com/v1.1/words/Test.doc/comments 
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'int',
        'status': 'str',
        'comments': 'CommentsCollection'
    }

    attribute_map = {
        'code': 'Code',
        'status': 'Status',
        'comments': 'Comments'
    }

    def __init__(self, code=None, status=None, comments=None):  # noqa: E501
        """CommentsResponse - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._status = None
        self._comments = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if status is not None:
            self.status = status
        if comments is not None:
            self.comments = comments

    @property
    def code(self):
        """Gets the code of this CommentsResponse.  # noqa: E501

        Response status code.  # noqa: E501

        :return: The code of this CommentsResponse.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CommentsResponse.

        Response status code.  # noqa: E501

        :param code: The code of this CommentsResponse.  # noqa: E501
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        self._code = code
    @property
    def status(self):
        """Gets the status of this CommentsResponse.  # noqa: E501

        Response status.  # noqa: E501

        :return: The status of this CommentsResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CommentsResponse.

        Response status.  # noqa: E501

        :param status: The status of this CommentsResponse.  # noqa: E501
        :type: str
        """
        self._status = status
    @property
    def comments(self):
        """Gets the comments of this CommentsResponse.  # noqa: E501

        Collection of comments.  # noqa: E501

        :return: The comments of this CommentsResponse.  # noqa: E501
        :rtype: CommentsCollection
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this CommentsResponse.

        Collection of comments.  # noqa: E501

        :param comments: The comments of this CommentsResponse.  # noqa: E501
        :type: CommentsCollection
        """
        self._comments = comments
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
        if not isinstance(other, CommentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
