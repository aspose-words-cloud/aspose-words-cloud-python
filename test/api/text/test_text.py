# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_text.py">
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
import datetime
import asposewordscloud.models.requests
from test.base_test_context import BaseTestContext

#
# Example of how to work with macros.
#
class TestText(BaseTestContext):
    #
    # Test for replacing text.
    #
    def test_replace_text(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Text'
        remoteFileName = 'TestReplaceText.docx'
        localFile = 'Common/test_multi_pages.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestReplaceText = asposewordscloud.ReplaceTextParameters(old_value='aspose', new_value='aspose new')
        request = asposewordscloud.models.requests.ReplaceTextRequest(name=remoteFileName, replace_text=requestReplaceText, folder=remoteDataFolder, dest_file_name=self.remote_test_out + '/' + remoteFileName)

        result = self.words_api.replace_text(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for searching.
    #
    def test_search(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Text'
        remoteFileName = 'TestSearch.docx'
        localFile = 'DocumentElements/Text/SampleWordDocument.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.SearchRequest(name=remoteFileName, pattern='aspose', folder=remoteDataFolder)

        result = self.words_api.search(request)
        self.assertIsNotNone(result, 'Error has occurred.')
