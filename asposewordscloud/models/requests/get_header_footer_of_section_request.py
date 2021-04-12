# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="get_header_footer_of_section_request.py">
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

class GetHeaderFooterOfSectionRequest(BaseRequestObject):
    """
    Request model for get_header_footer_of_section operation.
    Initializes a new instance.
    :param name The filename of the input document.
    :param header_footer_index The index of the HeaderFooter object.
    :param section_index The index of the section.
    :param folder Original document folder.
    :param storage Original document storage.
    :param load_encoding Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
    :param password Password for opening an encrypted document.
    :param filter_by_type The list of HeaderFooter types.
    """

    def __init__(self, name, header_footer_index, section_index, folder=None, storage=None, load_encoding=None, password=None, filter_by_type=None):
        self.name = name
        self.header_footer_index = header_footer_index
        self.section_index = section_index
        self.folder = folder
        self.storage = storage
        self.load_encoding = load_encoding
        self.password = password
        self.filter_by_type = filter_by_type

    def create_http_request(self, api_client):
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_header_footer_of_section`")  # noqa: E501
        # verify the required parameter 'header_footer_index' is set
        if self.header_footer_index is None:
            raise ValueError("Missing the required parameter `header_footer_index` when calling `get_header_footer_of_section`")  # noqa: E501
        # verify the required parameter 'section_index' is set
        if self.section_index is None:
            raise ValueError("Missing the required parameter `section_index` when calling `get_header_footer_of_section`")  # noqa: E501

        path = '/v4.0/words/{name}/sections/{sectionIndex}/headersfooters/{headerFooterIndex}'
        path_params = {}
        if self.name is not None:
            path_params['name'] = self.name  # noqa: E501
        else:
            path_params['name'] = ''  # noqa: E501
        if self.header_footer_index is not None:
            path_params['headerFooterIndex'] = self.header_footer_index  # noqa: E501
        else:
            path_params['headerFooterIndex'] = ''  # noqa: E501
        if self.section_index is not None:
            path_params['sectionIndex'] = self.section_index  # noqa: E501
        else:
            path_params['sectionIndex'] = ''  # noqa: E501

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
        if self.folder is not None:
                query_params.append(('folder', self.folder))  # noqa: E501
        if self.storage is not None:
                query_params.append(('storage', self.storage))  # noqa: E501
        if self.load_encoding is not None:
                query_params.append(('loadEncoding', self.load_encoding))  # noqa: E501
        if self.password is not None:
                query_params.append(('password', self.password))  # noqa: E501
        if self.filter_by_type is not None:
                query_params.append(('filterByType', self.filter_by_type))  # noqa: E501

        header_params = {}

        form_params = []

        body_params = None
        return {
            "method": "GET",
            "path": path,
            "query_params": query_params,
            "header_params": header_params,
            "form_params": form_params,
            "body": body_params,
            "collection_formats": collection_formats,
            "response_type": 'HeaderFooterResponse'  # noqa: E501
        }

    def get_response_type(self):
        return 'HeaderFooterResponse'  # noqa: E501

    def deserialize_response(self, api_client, response):
        return self.deserialize(response, HeaderFooterResponse, api_client)
