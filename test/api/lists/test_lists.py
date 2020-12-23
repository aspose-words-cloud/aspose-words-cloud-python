# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_lists.py">
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
# Example of how to work with lists.
#
class TestLists(BaseTestContext):
    #
    # Test for getting lists from document.
    #
    def test_get_lists(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Lists'
        localFile = 'DocumentElements/Lists/ListsGet.doc'
        remoteFileName = 'TestGetLists.doc'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetListsRequest(name=remoteFileName, folder=remoteDataFolder)

        result = self.words_api.get_lists(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.lists, 'Validate GetLists response')
        self.assertIsNotNone(result.lists.list_info, 'Validate GetLists response')
        self.assertEqual(2, len(result.lists.list_info))
        self.assertEqual(1, result.lists.list_info[0].list_id)

    #
    # Test for getting lists from document online.
    #
    def test_get_lists_online(self):
        localFile = 'DocumentElements/Lists/ListsGet.doc'

        request = asposewordscloud.models.requests.GetListsOnlineRequest(document=open(os.path.join(self.local_test_folder, localFile), 'rb'))

        result = self.words_api.get_lists_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting list from document.
    #
    def test_get_list(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Lists'
        localFile = 'DocumentElements/Lists/ListsGet.doc'
        remoteFileName = 'TestGetList.doc'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetListRequest(name=remoteFileName, list_id=1, folder=remoteDataFolder)

        result = self.words_api.get_list(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.list, 'Validate GetList response')
        self.assertEqual(1, result.list.list_id)

    #
    # Test for getting list from document online.
    #
    def test_get_list_online(self):
        localFile = 'DocumentElements/Lists/ListsGet.doc'

        request = asposewordscloud.models.requests.GetListOnlineRequest(document=open(os.path.join(self.local_test_folder, localFile), 'rb'), list_id=1)

        result = self.words_api.get_list_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating list from document.
    #
    def test_update_list(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Lists'
        localFile = 'DocumentElements/Lists/ListsGet.doc'
        remoteFileName = 'TestUpdateList.doc'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestListUpdate = asposewordscloud.ListUpdate(is_restart_at_each_section=True)
        request = asposewordscloud.models.requests.UpdateListRequest(name=remoteFileName, list_id=1, list_update=requestListUpdate, folder=remoteDataFolder)

        result = self.words_api.update_list(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating list from document online.
    #
    def test_update_list_online(self):
        localFile = 'DocumentElements/Lists/ListsGet.doc'

        requestListUpdate = asposewordscloud.ListUpdate(is_restart_at_each_section=True)
        request = asposewordscloud.models.requests.UpdateListOnlineRequest(document=open(os.path.join(self.local_test_folder, localFile), 'rb'), list_id=1, list_update=requestListUpdate)

        result = self.words_api.update_list_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.model.list, 'Validate UpdateListOnline response')
        self.assertEqual(1, result.model.list.list_id)
        self.assertTrue(result.model.list.is_restart_at_each_section, 'Validate UpdateListOnline response')

    #
    # Test for updating list level from document.
    #
    def test_update_list_level(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Lists'
        localFile = 'DocumentElements/Lists/ListsGet.doc'
        remoteFileName = 'TestUpdateListLevel.doc'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestListUpdate = asposewordscloud.ListLevelUpdate(alignment='Right')
        request = asposewordscloud.models.requests.UpdateListLevelRequest(name=remoteFileName, list_id=1, list_level=1, list_update=requestListUpdate, folder=remoteDataFolder)

        result = self.words_api.update_list_level(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating list level from document online.
    #
    def test_update_list_level_online(self):
        localFile = 'DocumentElements/Lists/ListsGet.doc'

        requestListUpdate = asposewordscloud.ListLevelUpdate(alignment='Right')
        request = asposewordscloud.models.requests.UpdateListLevelOnlineRequest(document=open(os.path.join(self.local_test_folder, localFile), 'rb'), list_id=1, list_level=1, list_update=requestListUpdate)

        result = self.words_api.update_list_level_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.model.list, 'Validate UpdateListLevelOnline response')
        self.assertIsNotNone(result.model.list.list_levels, 'Validate UpdateListLevelOnline response')
        self.assertIsNotNone(result.model.list.list_levels.list_level, 'Validate UpdateListLevelOnline response')
        self.assertEqual(9, len(result.model.list.list_levels.list_level))


    #
    # Test for inserting list from document.
    #
    def test_insert_list(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Lists'
        localFile = 'DocumentElements/Lists/ListsGet.doc'
        remoteFileName = 'TestInsertList.doc'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestListInsert = asposewordscloud.ListInsert(template='OutlineLegal')
        request = asposewordscloud.models.requests.InsertListRequest(name=remoteFileName, list_insert=requestListInsert, folder=remoteDataFolder)

        result = self.words_api.insert_list(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.list, 'Validate InsertList response')
        self.assertEqual(3, result.list.list_id)

    #
    # Test for inserting list from document online.
    #
    def test_insert_list_online(self):
        localFile = 'DocumentElements/Lists/ListsGet.doc'

        requestListInsert = asposewordscloud.ListInsert(template='OutlineLegal')
        request = asposewordscloud.models.requests.InsertListOnlineRequest(document=open(os.path.join(self.local_test_folder, localFile), 'rb'), list_insert=requestListInsert)

        result = self.words_api.insert_list_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

