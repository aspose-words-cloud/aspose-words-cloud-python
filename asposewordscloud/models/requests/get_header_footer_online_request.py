# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="get_header_footer_online_request.py">
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
import json

from six.moves.urllib.parse import quote
from asposewordscloud import *
from asposewordscloud.models import *
from asposewordscloud.models.requests import *
from asposewordscloud.models.responses import *

class GetHeaderFooterOnlineRequest(BaseRequestObject):
    """
    Request model for get_header_footer_online operation.
    Initializes a new instance.
    :param document The document.
    :param header_footer_index The index of the HeaderFooter object.
    :param load_encoding Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
    :param password Password of protected Word document. Use the parameter to pass a password via SDK. SDK encrypts it automatically. We don't recommend to use the parameter to pass a plain password for direct call of API.
    :param encrypted_password Password of protected Word document. Use the parameter to pass an encrypted password for direct calls of API. See SDK code for encyption details.
    :param filter_by_type The list of HeaderFooter types.
    """

    def __init__(self, document, header_footer_index, load_encoding=None, password=None, encrypted_password=None, filter_by_type=None):
        self.document = document
        self.header_footer_index = header_footer_index
        self.load_encoding = load_encoding
        self.password = password
        self.encrypted_password = encrypted_password
        self.filter_by_type = filter_by_type

    def create_http_request(self, api_client):
        # verify the required parameter 'document' is set
        if self.document is None:
            raise ValueError("Missing the required parameter `document` when calling `get_header_footer_online`")  # noqa: E501
        # verify the required parameter 'header_footer_index' is set
        if self.header_footer_index is None:
            raise ValueError("Missing the required parameter `header_footer_index` when calling `get_header_footer_online`")  # noqa: E501

        path = '/v4.0/words/online/get/headersfooters/{headerFooterIndex}'
        path_params = {}
        if self.header_footer_index is not None:
            path_params['headerFooterIndex'] = self.header_footer_index  # noqa: E501
        else:
            path_params['headerFooterIndex'] = ''  # noqa: E501

        # path parameters
        collection_formats = {}
        if path_params:
            path_params = api_client.sanitize_for_serialization(path_params)
            path_params = api_client.parameters_to_tuples(path_params, collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                path = path.replace(
                    '{%s}' % k,
                    quote(str(v), safe=api_client.configuration.safe_chars_for_path_param)
                )

        # remove optional path parameters
        path = path.replace('//', '/')

        query_params = []
        if self.load_encoding is not None:
                query_params.append(('loadEncoding', self.load_encoding))  # noqa: E501
        if self.password is not None:
                query_params.append(('password', self.password))  # noqa: E501
        if self.encrypted_password is not None:
                query_params.append(('encryptedPassword', self.encrypted_password))  # noqa: E501
        if self.filter_by_type is not None:
                query_params.append(('filterByType', self.filter_by_type))  # noqa: E501

        header_params = {}
        # HTTP header `Content-Type`
        header_params['Content-Type'] = api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        file_content_params = []
        form_params = []
        if self.document is not None:
            form_params.append(['document', self.document, 'file'])  # noqa: E501

        for file_content_value in file_content_params:
            form_params.append([file_content_value.reference, file_content_value.content, 'file'])  # noqa: E501

        return {
            "method": "PUT",
            "path": path,
            "body": None,
            "query_params": query_params,
            "header_params": header_params,
            "form_params": form_params,
            "collection_formats": collection_formats,
            "response_type": 'HeaderFooterResponse'  # noqa: E501
        }

    def get_response_type(self):
        return 'HeaderFooterResponse'  # noqa: E501

    def deserialize_response(self, api_client, response):
        return api_client.deserialize(response.data, response.getheaders(), HeaderFooterResponse)
