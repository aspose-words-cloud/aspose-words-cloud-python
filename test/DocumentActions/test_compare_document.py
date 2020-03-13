#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_compare_document.py">
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
import datetime
import asposewordscloud.models.requests
from test.base_test_context import BaseTestContext


class TestCompareDocument(BaseTestContext):
    test_folder = 'DocumentActions/CompareDocument'

    #
    # Test for document comparison
    #
    def test_compare_document(self):
        local_name1 = "compareTestDoc1.doc"
        local_name2 = "compareTestDoc2.doc"
        remote_name1 = "TestPostCompareDocument1.doc"
        remote_name2 = "TestPostCompareDocument2.doc"
        dest_name = os.path.join(self.remote_test_out, 'TestCompareOut.doc')
        compare_data = asposewordscloud.CompareData(os.path.join(self.remote_test_folder, self.test_folder, remote_name2),
                                                  'author', datetime.datetime.now())
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name1), open(os.path.join(self.local_test_folder, self.test_folder, local_name1), 'rb'))
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name2), open(os.path.join(self.local_test_folder, self.test_folder, local_name2), 'rb'))

        request = asposewordscloud.models.requests.CompareDocumentRequest(remote_name1, compare_data,
                                                                            os.path.join(self.remote_test_folder,
                                                                                         self.test_folder),
                                                                            dest_file_name=dest_name)
        result = self.words_api.compare_document(request)
        self.assertTrue(result.document is not None, 'Error has occurred while compare document')
