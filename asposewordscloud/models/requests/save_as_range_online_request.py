# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="save_as_range_online_request.py">
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
import json

from six.moves.urllib.parse import quote
from asposewordscloud import *
from asposewordscloud.models.requests import *
from asposewordscloud.models.responses import *

class SaveAsRangeOnlineRequest(BaseRequestObject):
    """
    Request model for save_as_range_online operation.
    Initializes a new instance.
    :param document The document.
    :param range_start_identifier The range start identifier.
    :param document_parameters Parameters of a new document.
    :param range_end_identifier The range end identifier.
    :param load_encoding Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
    :param password Password for opening an encrypted document.
    """

    def __init__(self, document, range_start_identifier, document_parameters, range_end_identifier=None, load_encoding=None, password=None):
        self.document = document
        self.range_start_identifier = range_start_identifier
        self.document_parameters = document_parameters
        self.range_end_identifier = range_end_identifier
        self.load_encoding = load_encoding
        self.password = password

    def create_http_request(self, api_client):
        # verify the required parameter 'document' is set
        if self.document is None:
            raise ValueError("Missing the required parameter `document` when calling `save_as_range_online`")  # noqa: E501
        # verify the required parameter 'range_start_identifier' is set
        if self.range_start_identifier is None:
            raise ValueError("Missing the required parameter `range_start_identifier` when calling `save_as_range_online`")  # noqa: E501
        # verify the required parameter 'document_parameters' is set
        if self.document_parameters is None:
            raise ValueError("Missing the required parameter `document_parameters` when calling `save_as_range_online`")  # noqa: E501

        path = '/v4.0/words/online/post/range/{rangeStartIdentifier}/{rangeEndIdentifier}/SaveAs'
        path_params = {}
        if self.range_start_identifier is not None:
            path_params['rangeStartIdentifier'] = self.range_start_identifier  # noqa: E501
        else:
            path_params['rangeStartIdentifier'] = ''  # noqa: E501
        if self.range_end_identifier is not None:
            path_params['rangeEndIdentifier'] = self.range_end_identifier  # noqa: E501
        else:
            path_params['rangeEndIdentifier'] = ''  # noqa: E501

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

        header_params = {}
        # HTTP header `Content-Type`
        header_params['Content-Type'] = api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        form_params = []
        if self.document is not None:
            form_params.append(['document', self.document, 'file'])  # noqa: E501
        if self.document_parameters is not None:
            form_params.append(['documentParameters', self.document_parameters.to_json(), 'string'])  # noqa: E501

        body_params = None
        return {
            "method": "PUT",
            "path": path,
            "query_params": query_params,
            "header_params": header_params,
            "form_params": form_params,
            "body": body_params,
            "collection_formats": collection_formats,
            "response_type": 'SaveAsRangeOnlineResponse'  # noqa: E501
        }

    def get_response_type(self):
        return 'SaveAsRangeOnlineResponse'  # noqa: E501

    def deserialize_response(self, api_client, response):
        multipart = self.getparts(response)
        return SaveAsRangeOnlineResponse(
          self.deserialize(json.loads(multipart[0].text), DocumentResponse, api_client),
          self.deserialize_file(multipart[1].content, multipart[1].headers, api_client))
