# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_folder.py">
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
# Example of how to work with folders.
#
class TestFolder(BaseTestContext):
    #
    # Test for create folder.
    #
    def test_create_folder(self):
        remoteDataFolder = self.remote_test_folder + '/Storage'

        request = asposewordscloud.models.requests.CreateFolderRequest(path=remoteDataFolder + '/TestCreateFolder')

        self.words_api.create_folder(request)


    #
    # Test for delete folder.
    #
    def test_delete_folder(self):
        remoteDataFolder = self.remote_test_folder + '/Storage'
        localFile = 'Common/test_multi_pages.docx'
        testDeleteFolder = remoteDataFolder + '/TestDeleteFolder'

        self.upload_file(testDeleteFolder + '/TestDeleteFolder.docx', open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteFolderRequest(path=testDeleteFolder)

        self.words_api.delete_folder(request)


    #
    # Test for get file list of folder.
    #
    def test_get_files_list(self):
        remoteDataFolder = self.remote_test_folder + '/Storage'

        request = asposewordscloud.models.requests.GetFilesListRequest(path=remoteDataFolder)

        result = self.words_api.get_files_list(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for copy folder.
    #
    def test_copy_folder(self):
        remoteDataFolder = self.remote_test_folder + '/Storage'
        localFile = 'Common/test_multi_pages.docx'
        folderToCopy = remoteDataFolder + '/TestCopyFolder'

        self.upload_file(folderToCopy + 'Src/TestCopyFolderSrc.docx', open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.CopyFolderRequest(dest_path=folderToCopy + 'Dest', src_path=folderToCopy + 'Src')

        self.words_api.copy_folder(request)


    #
    # Test for move folder.
    #
    def test_move_folder(self):
        remoteDataFolder = self.remote_test_folder + '/Storage'
        localFile = 'Common/test_multi_pages.docx'

        self.upload_file(remoteDataFolder + '/TestMoveFolderSrc/TestMoveFolderSrc.docx', open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.MoveFolderRequest(dest_path=self.remote_test_out + '/TestMoveFolderDest_' + self.create_random_guid(), src_path=remoteDataFolder + '/TestMoveFolderSrc')

        self.words_api.move_folder(request)

