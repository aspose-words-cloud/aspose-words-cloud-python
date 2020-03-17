#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_execute_mail_merge.py">
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


class TestExecuteMailMerge(BaseTestContext):
    test_folder = 'DocumentActions/MailMerge'

    #
    # Test for mail merge execution
    #
    def test_execute_mail_merge(self):
        filename = 'SampleMailMergeTemplate.docx'
        remote_name = 'TestPostDocumentExecuteMailMerge.docx'
        dest_name = os.path.join(self.remote_test_out, remote_name)
        with open(os.path.join(self.local_test_folder, self.test_folder, 'SampleMailMergeTemplateData.txt')) as f:
            data = f.read()
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, 'SampleMailMergeTemplateData.txt'), 'rb'))
        request = asposewordscloud.models.requests.ExecuteMailMergeRequest(remote_name, data,
                                                                                     os.path.join(
                                                                                         self.remote_test_folder,
                                                                                         self.test_folder),
                                                                                     dest_file_name=dest_name)
        result = self.words_api.execute_mail_merge(request)
        self.assertIsNotNone(result, 'Error has occurred while execute mail merge')

    #
    # Test for executing mail merge online
    #
    def test_execute_mail_merge_online(self):
        filename = 'SampleMailMergeTemplate.docx'
        file = open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb')
        data = open(os.path.join(self.local_test_folder, self.test_folder, 'SampleMailMergeTemplateData.txt'), 'rb')
        request = asposewordscloud.models.requests.ExecuteMailMergeOnlineRequest(file, data)
        result = self.words_api.execute_mail_merge_online(request)
        self.assertTrue(len(result) > 0, 'Error has occurred while execute mail merge')
