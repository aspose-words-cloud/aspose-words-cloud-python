# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_compare_document.py">
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
import dateutil.parser
import asposewordscloud.models.requests
from test.base_test_context import BaseTestContext

#
# Example of document comparison.
#
class TestCompareDocument(BaseTestContext):
    #
    # Test for document comparison.
    #
    def test_compare_document(self):
        remoteFolder = self.remote_test_folder + '/DocumentActions/CompareDocument'
        localFolder = 'DocumentActions/CompareDocument'
        localName1 = 'compareTestDoc1.doc'
        localName2 = 'compareTestDoc2.doc'
        remoteName1 = 'TestCompareDocument1.doc'
        remoteName2 = 'TestCompareDocument2.doc'

        self.upload_file(remoteFolder + '/' + remoteName1, open(os.path.join(self.local_test_folder, localFolder + '/' + localName1), 'rb'))
        self.upload_file(remoteFolder + '/' + remoteName2, open(os.path.join(self.local_test_folder, localFolder + '/' + localName2), 'rb'))

        requestCompareData = asposewordscloud.CompareData(author='author', comparing_with_document=remoteFolder + '/' + remoteName2, date_time=dateutil.parser.isoparse('2015-10-26T00:00:00.0000000Z'))
        request = asposewordscloud.models.requests.CompareDocumentRequest(name=remoteName1, compare_data=requestCompareData, folder=remoteFolder, dest_file_name=self.remote_test_out + '/TestCompareDocumentOut.doc')

        result = self.words_api.compare_document(request)
        self.assertIsNotNone(result, 'Error has occurred.')
