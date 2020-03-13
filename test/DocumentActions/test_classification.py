#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_classification.py">
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


class TestClassification(BaseTestContext):
    test_folder = 'Common'

    #
    # Test for raw text classification
    #
    def test_classify(self):
        request = asposewordscloud.models.requests.ClassifyRequest('Try text classification', '3')
        result = self.words_api.classify(request)
        self.assertTrue(True)

    #
    # Test for document classification
    #
    def test_classify_document(self):
        filename = "test_multi_pages.docx"
        remote_name = "Source.docx"
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.ClassifyDocumentRequest(remote_name,
                                                                           os.path.join(self.remote_test_folder,
                                                                                        self.test_folder))
        result = self.words_api.classify_document(request)
        self.assertTrue(True)

    #
    # Test for document classification with taxonomy "documents"
    #
    def test_classify_taxonomy_documents(self):
        filename = "test_multi_pages.docx"
        remote_name = "Source.docx"
        taxonomy = "documents"
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.ClassifyDocumentRequest(remote_name,
                                                                           os.path.join(self.remote_test_folder,
                                                                                        self.test_folder),
                                                                           taxonomy=taxonomy)
        result = self.words_api.classify_document(request)
        self.assertTrue(True)
