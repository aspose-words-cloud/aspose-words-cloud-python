# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_range.py">
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
# Example of how to work with ranges.
#
class TestRange(BaseTestContext):
    #
    # Test for getting the text from range.
    #
    def test_get_range_text(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Range'
        localFile = 'DocumentElements/Range/RangeGet.doc'
        remoteFileName = 'TestGetRangeText.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetRangeTextRequest(name=remoteFileName, range_start_identifier='id0.0.0', range_end_identifier='id0.0.1', folder=remoteDataFolder)

        result = self.words_api.get_range_text(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for removing the text for range.
    #
    def test_remove_range(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Range'
        localFile = 'DocumentElements/Range/RangeGet.doc'
        remoteFileName = 'TestRemoveRange.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.RemoveRangeRequest(name=remoteFileName, range_start_identifier='id0.0.0', range_end_identifier='id0.0.1', folder=remoteDataFolder)

        result = self.words_api.remove_range(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for saving a range as a new document.
    #
    def test_save_as_range(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Range'
        localFile = 'DocumentElements/Range/RangeGet.doc'
        remoteFileName = 'TestSaveAsRange.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestDocumentParameters = asposewordscloud.RangeDocument(document_name=remoteDataFolder + '/NewDoc.docx')
        request = asposewordscloud.models.requests.SaveAsRangeRequest(name=remoteFileName, range_start_identifier='id0.0.0', document_parameters=requestDocumentParameters, range_end_identifier='id0.0.1', folder=remoteDataFolder)

        result = self.words_api.save_as_range(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for replacing text in range.
    #
    def test_replace_with_text(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Range'
        localFile = 'DocumentElements/Range/RangeGet.doc'
        remoteFileName = 'TestReplaceWithText.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestRangeText = asposewordscloud.ReplaceRange(text='Replaced header')
        request = asposewordscloud.models.requests.ReplaceWithTextRequest(name=remoteFileName, range_start_identifier='id0.0.0', range_text=requestRangeText, range_end_identifier='id0.0.1', folder=remoteDataFolder)

        result = self.words_api.replace_with_text(request)
        self.assertIsNotNone(result, 'Error has occurred.')

