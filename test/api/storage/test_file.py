# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_file.py">
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
# Example of how to work with files.
#
class TestFile(BaseTestContext):
    #
    # Test for uploading file.
    #
    def test_upload_file(self):
        remoteDataFolder = self.remote_test_folder + '/Storage'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestUploadFile.docx'

        request = asposewordscloud.models.requests.UploadFileRequest(file_content=open(os.path.join(self.local_test_folder, localFile), 'rb'), path=remoteDataFolder + '/' + remoteFileName)

        result = self.words_api.upload_file(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.uploaded, 'Validate UploadFile response')
        self.assertEqual(1, len(result.uploaded))
        self.assertEqual('TestUploadFile.docx', result.uploaded[0])

    #
    # Test for copy file.
    #
    def test_copy_file(self):
        remoteDataFolder = self.remote_test_folder + '/Storage'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestCopyFileSrc.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.CopyFileRequest(dest_path=remoteDataFolder + '/TestCopyFileDest.docx', src_path=remoteDataFolder + '/' + remoteFileName)

        self.words_api.copy_file(request)


    #
    # Test for move file.
    #
    def test_move_file(self):
        remoteDataFolder = self.remote_test_folder + '/Storage'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestMoveFileSrc.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.MoveFileRequest(dest_path=self.remote_test_out + '/TestMoveFileDest_' + self.create_random_guid() + '.docx', src_path=remoteDataFolder + '/' + remoteFileName)

        self.words_api.move_file(request)


    #
    # Test for delete file.
    #
    def test_delete_file(self):
        remoteDataFolder = self.remote_test_folder + '/Storage'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestDeleteFile.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteFileRequest(path=remoteDataFolder + '/' + remoteFileName)

        self.words_api.delete_file(request)


    #
    # Test for download file.
    #
    def test_download_file(self):
        remoteDataFolder = self.remote_test_folder + '/Storage'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestDownloadFile.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DownloadFileRequest(path=remoteDataFolder + '/' + remoteFileName)

        result = self.words_api.download_file(request)
        self.assertIsNotNone(result, 'Error has occurred.')

