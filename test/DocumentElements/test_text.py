#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_text.py">
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


class TestText(BaseTestContext):
    test_folder = 'DocumentElements/Text'

    #
    #  Test for replacing text
    #
    def test_replace_text(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPostReplaceText.docx'
        dest_name = os.path.join(self.remote_test_out, remote_name)
        body = asposewordscloud.ReplaceTextParameters('aspose', 'aspose new')

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.ReplaceTextRequest(remote_name, body,
                                                                        os.path.join(
                                                                            self.remote_test_folder,
                                                                            self.test_folder),
                                                                        dest_file_name=dest_name)
        result = self.words_api.replace_text(request)
        self.assertIsNotNone(result, 'Error has occurred while post replace text')

    #
    #  Test for searching text
    #
    def test_search(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestSearch.docx'
        pattern = 'aspose'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.SearchRequest(remote_name, pattern,
                                                                 os.path.join(
                                                                     self.remote_test_folder,
                                                                     self.test_folder))
        result = self.words_api.search(request)
        self.assertIsNotNone(result, 'Error has occurred while search text')
