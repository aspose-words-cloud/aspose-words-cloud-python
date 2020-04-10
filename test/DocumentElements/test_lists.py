#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_lists.py">
#   Copyright (c) 2019 Aspose.Words for Cloud
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
# --------------------------------------------------------------------------------------------------------------------
#

import os
import asposewordscloud.models.requests
from test.base_test_context import BaseTestContext


class TestLists(BaseTestContext):
    test_folder = 'DocumentElements/Lists'
    local_name = 'ListsGet.doc'

    def test_get_lists(self):
        remote_name = 'TestGetLists.doc'
        self.upload_file(os.path.join(self.remote_test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, self.local_name), 'rb'))
        request = asposewordscloud.models.requests.GetListsRequest(remote_name, self.remote_test_folder)
        _ = self.words_api.get_lists(request)

    def test_get_list(self):
        remote_name = 'TestGetList.doc'
        self.upload_file(os.path.join(self.remote_test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, self.local_name), 'rb'))
        request = asposewordscloud.models.requests.GetListRequest(remote_name, 1, self.remote_test_folder)
        _ = self.words_api.get_list(request)

    def test_update_list(self):
        remote_name = 'TestUpdateList.doc'
        self.upload_file(os.path.join(self.remote_test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, self.local_name), 'rb'))
        data = asposewordscloud.models.ListUpdate(True)
        request = asposewordscloud.models.requests.UpdateListRequest(remote_name, data, 1, self.remote_test_folder)
        _ = self.words_api.update_list(request)

    def test_update_list_level(self):
        remote_name = 'TestUpdateListLevel.doc'
        self.upload_file(os.path.join(self.remote_test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, self.local_name), 'rb'))
        data = asposewordscloud.models.ListLevelUpdate(alignment="Right")
        request = asposewordscloud.models.requests.UpdateListLevelRequest(remote_name, data, 1, 1, self.remote_test_folder)
        _ = self.words_api.update_list_level(request)

    def test_insert_list(self):
        remote_name = 'TestInsertList.doc'
        self.upload_file(os.path.join(self.remote_test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, self.local_name), 'rb'))
        data = asposewordscloud.models.ListInsert("OutlineLegal")
        request = asposewordscloud.models.requests.InsertListRequest(remote_name, data, self.remote_test_folder)
        _ = self.words_api.insert_list(request)
