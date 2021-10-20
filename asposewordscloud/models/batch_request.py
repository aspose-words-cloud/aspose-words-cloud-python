# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="batch_request.py">
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
import uuid
import io

class BatchRequest():
    """
    Request wrapper for batch operation.
    Initializes a new instance.
    :param request The request to wrap.
    """
    def __init__(self, request):
        self.request = request
        self.id = str(uuid.uuid4())
        self.parent_id = None 

    def dependsOn(self, parent_request):
        self.parent_id = parent_request.id

    def create_http_request(self, api_client):
        http_request = self.request.create_http_request(api_client)
        http_request["header_params"]["RequestId"] = self.id

        if self.parent_id != None:
            http_request["header_params"]["DependsOn"] = self.parent_id

        return http_request

    def get_response_type(self):
        return self.request.get_response_type()

    def deserialize_response(self, api_client, response):
        return self.request.deserialize_response(api_client, response)

    def use_as_source(self):
        data = io.StringIO()
        data.write('"resultOf(' + self.id + ')')
        return data