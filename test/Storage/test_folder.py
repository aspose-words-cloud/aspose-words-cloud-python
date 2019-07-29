import uuid
import asposewordscloud.models.requests
from test.base_test_context import BaseTestContext
from asposewordscloud.rest import ApiException

class TestFolder(BaseTestContext):
    test_folder = "Temp/SdkTests/TestData/Storage"

    def test_create_folder(self): 
        folder_uuid = str(uuid.uuid4())
        folder_path = '{self.test_folder}/TestCreateFolder{folder_uuid}'
        request = asposewordscloud.models.requests.CreateFolderRequest(folder_path)
        response = self.words_api.create_folder(request)
        self.assertIsNotNone(response, "Folder has not been created")

    def test_delete_folder(self):
        folder_uuid = str(uuid.uuid4())
        folder_path = '{self.test_folder}/TestCreateFolder{folder_uuid}'
        request = asposewordscloud.models.requests.CreateFolderRequest(folder_path)
        self.words_api.create_folder(request)
        request = asposewordscloud.models.requests.DeleteFolderRequest(folder_path)
        response = self.words_api.delete_folder(request)
        self.assertIsNotNone(response, "Folder has not been created")

    def test_get_files_list(self):
        request = asposewordscloud.models.requests.GetFilesListRequest(self.test_folder)
        response = self.words_api.get_files_list(request)
        self.assertTrue(True)

    def test_copy_folder(self):
        folder_uuid = str(uuid.uuid4())
        folder_path_src = '/{self.test_folder}/TestCopyFolderSrc{folder_uuid}/'
        folder_path_dst = '/{self.test_folder}/TestCopyFolderDst{folder_uuid}/'
        self.words_api.create_folder(asposewordscloud.models.requests.CreateFolderRequest(folder_path_src))

        request = asposewordscloud.models.requests.CopyFolderRequest(folder_path_dst, folder_path_src)
        self.words_api.copy_folder(request)

        response = self.words_api.get_files_list(asposewordscloud.models.requests.GetFilesListRequest(self.test_folder))
        self.assertIsNotNone(response)

    def test_move_folder(self):
        folder_uuid = str(uuid.uuid4())
        folder_path_src = '/{self.test_folder}/TestCopyFolderSrc{folder_uuid}/'
        folder_path_dst = '/{self.test_folder}/TestCopyFolderDst{folder_uuid}/'
        self.words_api.create_folder(asposewordscloud.models.requests.CreateFolderRequest(folder_path_src))

        request = asposewordscloud.models.requests.MoveFolderRequest(folder_path_dst, folder_path_src)
        self.words_api.move_folder(request)

        response = self.words_api.get_files_list(asposewordscloud.models.requests.GetFilesListRequest(self.test_folder))