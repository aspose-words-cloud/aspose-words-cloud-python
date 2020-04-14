#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_reporting.py">
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
# --------------------------------------------------------------------------------------------------------------------
#

import os
import asposewordscloud.models.requests
from test.base_test_context import BaseTestContext


class TestReporting(BaseTestContext):
    test_folder = 'DocumentActions/Reporting'

    #
    # Test for saving document with specified format
    #
    def test_build_report_online(self):
        template = open(os.path.join(self.local_test_folder, self.test_folder, 'ReportTemplate.docx'), 'rb')
        with open(os.path.join(self.local_test_folder, self.test_folder, 'ReportData.json')) as fp:
            dataJson = fp.read()
            settings = '{DataSourceType: "Json", DataSourceName: "persons"}'
            request = asposewordscloud.models.requests.BuildReportOnlineRequest(template, dataJson, settings)
            result = self.words_api.build_report_online(request)
            self.assertTrue(len(result) > 0)

    #
    # Test for saving document with specified format
    #
    def test_build_report(self):
        remote_name = 'TestBuildReport.docx'
        dataJson = open(os.path.join(self.local_test_folder, self.test_folder, 'ReportData.json'), 'r').read()

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, 'ReportTemplate.docx'), 'rb'))

        settings = '{DataSourceType: "Json", ReportBuildOptions: ["AllowMissingMembers", "RemoveEmptyParagraphs"]}'
        request = asposewordscloud.models.requests.BuildReportRequest(remote_name, dataJson, settings, os.path.join(self.remote_test_folder, self.test_folder))
        self.words_api.build_report(request)
