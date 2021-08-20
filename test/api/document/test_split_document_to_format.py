# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_split_document_to_format.py">
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
import dateutil.parser
import asposewordscloud.models.requests
from test.base_test_context import BaseTestContext

#
# Example of how to split document and return result with specified format and page range.
#
class TestSplitDocumentToFormat(BaseTestContext):
    #
    # Test for document splitting.
    #
    def test_split_document(self):
        remote_data_folder = self.remote_test_folder + '/DocumentActions/SplitDocument'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestSplitDocument.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.SplitDocumentRequest(name=remote_file_name, format='text', folder=remote_data_folder, dest_file_name=self.remote_test_out + '/TestSplitDocument.text', _from=1, to=2)

        result = self.words_api.split_document(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.split_result, 'Validate SplitDocument response')
        self.assertIsNotNone(result.split_result.pages, 'Validate SplitDocument response')
        self.assertEqual(2, len(result.split_result.pages))

    #
    # Test for document splitting online.
    #
    def test_split_document_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.SplitDocumentOnlineRequest(document=request_document, format='text', dest_file_name=self.remote_test_out + '/TestSplitDocument.text', _from=1, to=2)

        result = self.words_api.split_document_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

