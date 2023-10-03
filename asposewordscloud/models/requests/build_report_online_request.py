# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="build_report_online_request.py">
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

class BuildReportOnlineRequest(BaseRequestObject):
    """
    Request model for build_report_online operation.
    Initializes a new instance.
    :param template File with template.
    :param data A string providing a data to populate the specified template. The string must be of one of the following types: xml, json, csv.
    :param report_engine_settings An object providing a settings of report engine.
    :param document_file_name The filename of the output document, that will be used when the resulting document has a dynamic field {filename}. If it is not set, the "template" will be used instead.
    """

    def __init__(self, template, data, report_engine_settings, document_file_name=None):
        self.template = template
        self.data = data
        self.report_engine_settings = report_engine_settings
        self.document_file_name = document_file_name

    def create_http_request(self, api_client):
        # verify the required parameter 'template' is set
        if self.template is None:
            raise ValueError("Missing the required parameter `template` when calling `build_report_online`")  # noqa: E501
        # verify the required parameter 'data' is set
        if self.data is None:
            raise ValueError("Missing the required parameter `data` when calling `build_report_online`")  # noqa: E501
        # verify the required parameter 'report_engine_settings' is set
        if self.report_engine_settings is None:
            raise ValueError("Missing the required parameter `report_engine_settings` when calling `build_report_online`")  # noqa: E501

        path = '/v4.0/words/buildReport'
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
        if self.document_file_name is not None:
                query_params.append(('documentFileName', self.document_file_name))  # noqa: E501

        header_params = {}
        # HTTP header `Content-Type`
        header_params['Content-Type'] = api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        file_content_params = []
        form_params = []
        if self.template is not None:
            form_params.append(['template', self.template, 'file'])  # noqa: E501
        if self.data is not None:
            form_params.append(['data', self.data, 'string'])  # noqa: E501
        if self.report_engine_settings is not None:
            form_params.append(['reportEngineSettings', self.report_engine_settings, 'json'])  # noqa: E501

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
            "response_type": 'file'  # noqa: E501
        }

    def get_response_type(self):
        return 'file'  # noqa: E501

    def deserialize_response(self, api_client, response):
        return api_client.deserialize_file(response.data, response.getheaders())
