#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_execute_template.py">
#   Copyright (c) 2018 Aspose.Words for Cloud
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


class TestExecuteTemplate(BaseTestContext):
    test_folder = 'DocumentActions/MailMerge'

    #
    # Test for executing template
    #
    def test_post_execute_template(self):
        filename = 'TestExecuteTemplate.doc'
        remote_name = 'TestPostExecuteTemplate.docx'
        dest_name = os.path.join(self.remote_test_out, remote_name)
        with open(os.path.join(self.local_test_folder, self.test_folder, 'TestExecuteTemplateData.txt')) as f:
            data = f.read()
        with open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.PostExecuteTemplateRequest(remote_name, data,
                                                                            os.path.join(
                                                                                self.remote_test_folder,
                                                                                self.test_folder),
                                                                            dest_file_name=dest_name)
        result = self.words_api.post_execute_template(request)
        self.assertTrue(result.code == 200, 'Error has occurred while execute template')

    #
    # Test for executing template online
    #
    def test_put_execute_template_online(self):
        filename = 'SampleExecuteTemplate.docx'
        file = os.path.join(self.local_test_folder, self.test_folder, filename)
        data = os.path.join(self.local_test_folder, self.test_folder, 'SampleExecuteTemplateData.txt')
        request = asposewordscloud.models.requests.PutExecuteTemplateOnlineRequest(file, data)
        result = self.words_api.put_execute_template_online(request)
        self.assertTrue(len(result) > 0, 'Error has occurred while execute template')
