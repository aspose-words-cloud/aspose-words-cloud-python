# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="PdfDigitalSignatureDetailsData.py">
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


class PdfDigitalSignatureDetailsData(object):
    """container class for details of digital signature.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'certificate_filename': 'str',
        'hash_algorithm': 'str',
        'location': 'str',
        'reason': 'str',
        'signature_date': 'datetime'
    }

    attribute_map = {
        'certificate_filename': 'CertificateFilename',
        'hash_algorithm': 'HashAlgorithm',
        'location': 'Location',
        'reason': 'Reason',
        'signature_date': 'SignatureDate'
    }

    def __init__(self, certificate_filename=None, hash_algorithm=None, location=None, reason=None, signature_date=None):  # noqa: E501
        """PdfDigitalSignatureDetailsData - a model defined in Swagger"""  # noqa: E501

        self._certificate_filename = None
        self._hash_algorithm = None
        self._location = None
        self._reason = None
        self._signature_date = None
        self.discriminator = None

        if certificate_filename is not None:
            self.certificate_filename = certificate_filename
        if hash_algorithm is not None:
            self.hash_algorithm = hash_algorithm
        if location is not None:
            self.location = location
        if reason is not None:
            self.reason = reason
        if signature_date is not None:
            self.signature_date = signature_date

    @property
    def certificate_filename(self):
        """Gets the certificate_filename of this PdfDigitalSignatureDetailsData.  # noqa: E501

        Gets or sets certificate's filename using for signing.  # noqa: E501

        :return: The certificate_filename of this PdfDigitalSignatureDetailsData.  # noqa: E501
        :rtype: str
        """
        return self._certificate_filename

    @certificate_filename.setter
    def certificate_filename(self, certificate_filename):
        """Sets the certificate_filename of this PdfDigitalSignatureDetailsData.

        Gets or sets certificate's filename using for signing.  # noqa: E501

        :param certificate_filename: The certificate_filename of this PdfDigitalSignatureDetailsData.  # noqa: E501
        :type: str
        """
        self._certificate_filename = certificate_filename
    @property
    def hash_algorithm(self):
        """Gets the hash_algorithm of this PdfDigitalSignatureDetailsData.  # noqa: E501

        Gets or sets hash algorithm.  # noqa: E501

        :return: The hash_algorithm of this PdfDigitalSignatureDetailsData.  # noqa: E501
        :rtype: str
        """
        return self._hash_algorithm

    @hash_algorithm.setter
    def hash_algorithm(self, hash_algorithm):
        """Sets the hash_algorithm of this PdfDigitalSignatureDetailsData.

        Gets or sets hash algorithm.  # noqa: E501

        :param hash_algorithm: The hash_algorithm of this PdfDigitalSignatureDetailsData.  # noqa: E501
        :type: str
        """
        self._hash_algorithm = hash_algorithm
    @property
    def location(self):
        """Gets the location of this PdfDigitalSignatureDetailsData.  # noqa: E501

        Gets or sets location of the signing.  # noqa: E501

        :return: The location of this PdfDigitalSignatureDetailsData.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this PdfDigitalSignatureDetailsData.

        Gets or sets location of the signing.  # noqa: E501

        :param location: The location of this PdfDigitalSignatureDetailsData.  # noqa: E501
        :type: str
        """
        self._location = location
    @property
    def reason(self):
        """Gets the reason of this PdfDigitalSignatureDetailsData.  # noqa: E501

        Gets or sets reason for the signing.  # noqa: E501

        :return: The reason of this PdfDigitalSignatureDetailsData.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this PdfDigitalSignatureDetailsData.

        Gets or sets reason for the signing.  # noqa: E501

        :param reason: The reason of this PdfDigitalSignatureDetailsData.  # noqa: E501
        :type: str
        """
        self._reason = reason
    @property
    def signature_date(self):
        """Gets the signature_date of this PdfDigitalSignatureDetailsData.  # noqa: E501

        Gets or sets date of the signing.  # noqa: E501

        :return: The signature_date of this PdfDigitalSignatureDetailsData.  # noqa: E501
        :rtype: datetime
        """
        return self._signature_date

    @signature_date.setter
    def signature_date(self, signature_date):
        """Sets the signature_date of this PdfDigitalSignatureDetailsData.

        Gets or sets date of the signing.  # noqa: E501

        :param signature_date: The signature_date of this PdfDigitalSignatureDetailsData.  # noqa: E501
        :type: datetime
        """
        self._signature_date = signature_date
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
        if not isinstance(other, PdfDigitalSignatureDetailsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
