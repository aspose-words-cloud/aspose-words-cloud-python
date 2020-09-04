# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_run.py">
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
# Example of how to work with runs.
#
class TestRun(BaseTestContext):
    #
    # Test for updating run.
    #
    def test_update_run(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Runs'
        localFile = 'DocumentElements/Runs/Run.doc'
        remoteFileName = 'TestUpdateRun.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestRun = asposewordscloud.RunUpdate(text='run with text')
        request = asposewordscloud.models.requests.UpdateRunRequest(name=remoteFileName, run=requestRun, paragraph_path='paragraphs/1', index=0, folder=remoteDataFolder)

        result = self.words_api.update_run(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for adding run.
    #
    def test_insert_run(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Runs'
        localFile = 'DocumentElements/Runs/Run.doc'
        remoteFileName = 'TestInsertRun.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestRun = asposewordscloud.RunInsert(text='run with text')
        request = asposewordscloud.models.requests.InsertRunRequest(name=remoteFileName, paragraph_path='paragraphs/1', run=requestRun, folder=remoteDataFolder)

        result = self.words_api.insert_run(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting run.
    #
    def test_delete_run(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Runs'
        localFile = 'DocumentElements/Runs/Run.doc'
        remoteFileName = 'TestDeleteRun.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteRunRequest(name=remoteFileName, paragraph_path='paragraphs/1', index=0, folder=remoteDataFolder)

        self.words_api.delete_run(request)

