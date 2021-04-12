# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_batch.py">
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

import os
import asposewordscloud.models.requests
from test.base_test_context import BaseTestContext


class TestBatch(BaseTestContext):

    test_folder = 'DocumentElements/Bookmarks'

    #
    # Test for batch request
    #
    def test_batch(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestBatchParagraphs.docx'
        file = open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb')
        remote_path = os.path.join(self.remote_test_folder, self.test_folder, remote_name)
        remote_folder = os.path.join(self.remote_test_folder, self.test_folder)
        paragraph = asposewordscloud.models.ParagraphInsert(text="This is a new paragraph for your document")
        request0 = asposewordscloud.models.requests.UploadFileRequest(file, remote_path)
        request1 = asposewordscloud.models.requests.GetParagraphsRequest(name=remote_name, node_path="sections/0", folder=remote_folder)
        request2 = asposewordscloud.models.requests.GetParagraphRequest(name=remote_name, index=0, node_path="sections/0", folder=remote_folder)
        request3 = asposewordscloud.models.requests.InsertParagraphRequest(name=remote_name, paragraph=paragraph, node_path="sections/0", folder=remote_folder)
        request4 = asposewordscloud.models.requests.DeleteParagraphRequest(name=remote_name, index=0, node_path="", folder=remote_folder)

        reportingFolder = 'DocumentActions/Reporting'
        localDocumentFile = 'ReportTemplate.docx'
        localDataFile = open(os.path.join(self.local_test_folder, reportingFolder + '/ReportData.json')).read()
        requestReportEngineSettings = asposewordscloud.ReportEngineSettings(data_source_type='Json', data_source_name='persons')
        request5 = asposewordscloud.models.requests.BuildReportOnlineRequest(
            template=open(os.path.join(self.local_test_folder, reportingFolder + '/' + localDocumentFile), 'rb'),
            data=localDataFile, report_engine_settings=requestReportEngineSettings)

        self.words_api.upload_file(request0)
        result = self.words_api.batch(request1, request2, request3, request4, request5)
        self.assertEqual(len(result), 5)
        self.assertIsInstance(result[0], asposewordscloud.ParagraphLinkCollectionResponse)
        self.assertIsInstance(result[1], asposewordscloud.ParagraphResponse)
        self.assertIsInstance(result[2], asposewordscloud.ParagraphResponse)
        self.assertIsNone(result[3])
        self.assertIsInstance(result[4], str)
