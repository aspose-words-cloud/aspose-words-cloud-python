# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="build_report_online_request.py">
#   Copyright (c) 2020 Aspose.Words for Cloud
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

class BuildReportOnlineRequest(object):
    """
    Request model for build_report_online operation.
    Initializes a new instance.
    :param template File with template.
    :param data A string providing a data to populate the specified template. The string must be of one of the following types: xml, json, csv.
    :param report_engine_settings An object providing a settings of report engine.
    :param document_file_name This file name will be used when resulting document has dynamic field for document file name {filename}. If it is not set, "template" will be used instead.
    """

    def __init__(self, template, data, report_engine_settings, document_file_name=None):
        self.template = template
        self.data = data
        self.report_engine_settings = report_engine_settings
        self.document_file_name = document_file_name
