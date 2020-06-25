# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_build_report.py">
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

import os
import datetime
import asposewordscloud.models.requests
from test.base_test_context import BaseTestContext

#
# Example of how to perform mail merge.
#
class TestBuildReport(BaseTestContext):
    #
    # Test for build report online.
    #
    def test_build_report_online(self):
        reportingFolder = 'DocumentActions/Reporting'
        localDocumentFile = 'ReportTemplate.docx'
        localDataFile = open(os.path.join(self.local_test_folder, reportingFolder + '/ReportData.json')).read()

        requestReportEngineSettings = asposewordscloud.ReportEngineSettings(data_source_type='Json', data_source_name='persons')
        request = asposewordscloud.models.requests.BuildReportOnlineRequest(template=open(os.path.join(self.local_test_folder, reportingFolder + '/' + localDocumentFile), 'rb'), data=localDataFile, report_engine_settings=requestReportEngineSettings)

        result = self.words_api.build_report_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for build report.
    #
    def test_build_report(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentActions/Reporting'
        reportingFolder = 'DocumentActions/Reporting'
        localDocumentFile = 'ReportTemplate.docx'
        remoteFileName = 'TestBuildReport.docx'
        localDataFile = open(os.path.join(self.local_test_folder, reportingFolder + '/ReportData.json')).read()

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, reportingFolder + '/' + localDocumentFile), 'rb'))

        requestReportEngineSettingsReportBuildOptions = ['AllowMissingMembers', 'RemoveEmptyParagraphs']
        requestReportEngineSettings = asposewordscloud.ReportEngineSettings(data_source_type='Json', report_build_options=requestReportEngineSettingsReportBuildOptions)
        request = asposewordscloud.models.requests.BuildReportRequest(name=remoteFileName, data=localDataFile, report_engine_settings=requestReportEngineSettings, folder=remoteDataFolder)

        result = self.words_api.build_report(request)
        self.assertIsNotNone(result, 'Error has occurred.')
