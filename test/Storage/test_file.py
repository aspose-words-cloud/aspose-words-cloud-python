import os
import uuid
import asposewordscloud.models.requests
from test.base_test_context import BaseTestContext
from asposewordscloud.rest import ApiException

class TestFile(BaseTestContext):
    test_folder = "Temp/SdkTests/TestData"

    def test_upload_file(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestUploadFile.docx'

        request = asposewordscloud.models.requests.UploadFileRequest(open(os.path.join(self.local_common_folder, filename), 'rb'), os.path.join(self.test_folder, remote_name))
        result = self.words_api.upload_file(request)
        self.assertTrue(len(result._uploaded) == 1 , 'Error has occurred while delete document macros')

    def test_copy_file(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestCopyFileSrc.docx'
        remote_name_dst = 'TestCopyFileDst' + str(uuid.uuid4()) + '.docx'
        remote_path_src = os.path.join(self.remote_test_folder, self.test_folder, remote_name)
        remote_path_dst = os.path.join(self.remote_test_folder, self.test_folder, remote_name_dst)
       
        request = asposewordscloud.models.requests.UploadFileRequest(open(os.path.join(self.local_common_folder, filename), 'rb'), remote_path_src)
        self.words_api.upload_file(request)

        request = asposewordscloud.models.requests.CopyFileRequest(remote_path_dst, remote_path_src)
        response = self.words_api.copy_file(request)

        self.assertIsNotNone(response, 'Error has occurred while delete document macros')
        
    def test_move_file(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestMoveFileSrc.docx'
        remote_name_dst = 'TestMoveFileDst' + str(uuid.uuid4()) + '.docx'
        remote_path_src = os.path.join(self.remote_test_folder, self.test_folder, remote_name)
        remote_path_dst = os.path.join(self.remote_test_folder, self.test_folder, remote_name_dst)

        request = asposewordscloud.models.requests.UploadFileRequest(open(os.path.join(self.local_common_folder, filename), 'rb'), remote_path_src)
        result = self.words_api.upload_file(request)

        request = asposewordscloud.models.requests.MoveFileRequest(remote_path_dst, remote_path_src)
        result = self.words_api.move_file(request)
        download_dst = self.words_api.download_file(asposewordscloud.models.requests.DownloadFileRequest(request.dest_path))
        self.assertTrue(len(download_dst) > 0)

        try:
            download_src = self.words_api.download_file(asposewordscloud.models.requests.DownloadFileRequest(remote_path_src))
            self.assertRaises(ApiException)
        except ApiException as e:
            self.assertEqual(404, e.status, "Status has to be 404")

    def test_delete_file(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestDeleteFile.docx'
        path = os.path.join(self.local_common_folder, filename)
        request = asposewordscloud.models.requests.UploadFileRequest(open(os.path.join(self.local_common_folder, filename), 'rb'), os.path.join(self.remote_test_folder, self.test_folder, remote_name))
        self.words_api.upload_file(request)

        result = self.words_api.delete_file(asposewordscloud.models.requests.DeleteFileRequest(path))
        self.assertIsNotNone(result, "Error while deleting file")

    def test_download_file(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestDownloadFile.docx'
        remote_path = os.path.join(self.remote_test_folder, self.test_folder, remote_name)
        path = os.path.join(self.local_common_folder, filename)
        self.upload_file(remote_path, open(os.path.join(self.local_common_folder, filename), 'rb'))

        request = asposewordscloud.models.requests.DownloadFileRequest(remote_path)
        response = self.words_api.download_file(request)
        self.assertTrue(len(response) > 0, 'Error while downloading file')
