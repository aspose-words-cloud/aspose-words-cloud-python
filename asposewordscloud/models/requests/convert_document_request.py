# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="convert_document_request.py">
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

class ConvertDocumentRequest(BaseRequestObject):
    """
    Request model for convert_document operation.
    Initializes a new instance.
    :param document Converting document.
    :param format The format to convert.
    :param out_path The path to the output document on a local storage.
    :param file_name_field_value The filename of the output document, that will be used when the resulting document has a dynamic field {filename}. If it is not set, the "sourceFilename" will be used instead.
    :param storage Original document storage.
    :param fonts_location Folder in filestorage with custom fonts.
    """

    def __init__(self, document, format, out_path=None, file_name_field_value=None, storage=None, fonts_location=None):
        self.document = document
        self.format = format
        self.out_path = out_path
        self.file_name_field_value = file_name_field_value
        self.storage = storage
        self.fonts_location = fonts_location

    def create_http_request(self, api_client):
        # verify the required parameter 'document' is set
        if self.document is None:
            raise ValueError("Missing the required parameter `document` when calling `convert_document`")  # noqa: E501
        # verify the required parameter 'format' is set
        if self.format is None:
            raise ValueError("Missing the required parameter `format` when calling `convert_document`")  # noqa: E501

        path = '/v4.0/words/convert'
        path_params = {}

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
        if self.format is not None:
                query_params.append(('format', self.format))  # noqa: E501
        if self.out_path is not None:
                query_params.append(('outPath', self.out_path))  # noqa: E501
        if self.file_name_field_value is not None:
                query_params.append(('fileNameFieldValue', self.file_name_field_value))  # noqa: E501
        if self.storage is not None:
                query_params.append(('storage', self.storage))  # noqa: E501
        if self.fonts_location is not None:
                query_params.append(('fontsLocation', self.fonts_location))  # noqa: E501

        header_params = {}
        # HTTP header `Content-Type`
        header_params['Content-Type'] = api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        form_params = []
        if self.document is not None:
            form_params.append(['document', self.document, 'file'])  # noqa: E501

        body_params = None
        return {
            "method": "PUT",
            "path": path,
            "query_params": query_params,
            "header_params": header_params,
            "form_params": form_params,
            "body": body_params,
            "collection_formats": collection_formats,
            "response_type": 'file'  # noqa: E501
        }

    def get_response_type(self):
        return 'file'  # noqa: E501

    def deserialize_response(self, api_client, response):
        return self.deserialize_file(response.data, response.getheaders(), api_client)
