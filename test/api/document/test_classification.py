# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_classification.py">
#   Copyright (c) 2023 Aspose.Words for Cloud
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
import dateutil.parser
import asposewordscloud.models.requests
from test.base_test_context import BaseTestContext

#
# Example of how to classify text.
#
class TestClassification(BaseTestContext):
    #
    # Test for raw text classification.
    #
    def test_classify(self):
        request = asposewordscloud.models.requests.ClassifyRequest(text='Try text classification', best_classes_count='3')

        result = self.words_api.classify(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertEqual('Science', result.best_class_name)
        self.assertIsNotNone(result.best_results, 'Validate Classify response')
        self.assertEqual(3, len(result.best_results))

    #
    # Test for document classification.
    #
    def test_classify_document(self):
        remote_data_folder = self.remote_test_folder + '/Common'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestClassifyDocument.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.ClassifyDocumentRequest(name=remote_file_name, folder=remote_data_folder, best_classes_count='3')

        result = self.words_api.classify_document(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertEqual('Hobbies_&_Interests', result.best_class_name)
        self.assertIsNotNone(result.best_results, 'Validate ClassifyDocument response')
        self.assertEqual(3, len(result.best_results))

    #
    # Test for document classification online.
    #
    def test_classify_document_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.ClassifyDocumentOnlineRequest(document=request_document, best_classes_count='3')

        result = self.words_api.classify_document_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

