#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_bookmarks.py">
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


class TestBookmarks(BaseTestContext):
    test_folder = 'DocumentElements/Bookmarks'

    #
    # Test for getting document bookmark by name
    #
    def test_get_bookmark_by_name(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentBookmarkByName.docx'
        bookmark_name = 'aspose'
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetBookmarkByNameRequest(remote_name, bookmark_name,
                                                                                  os.path.join(
                                                                                      self.remote_test_folder,
                                                                                      self.test_folder))
        result = self.words_api.get_bookmark_by_name(request)
        self.assertIsNotNone(result, 'Error has occurred while get document bookmark by name')

    #
    # Test for getting all bookmarks from document
    #
    def test_get_bookmarks(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentBookmarks.docx'
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetBookmarksRequest(remote_name,
                                                                             os.path.join(
                                                                                 self.remote_test_folder,
                                                                                 self.test_folder))
        result = self.words_api.get_bookmarks(request)
        self.assertIsNotNone(result, 'Error has occurred while get document bookmarks')

    #
    # Test for updating document bookmark
    #
    def test_update_bookmark(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPostUpdateDocumentBookmark.docx'
        bookmark_name = 'aspose'
        dest_name = os.path.join(self.remote_test_out, remote_name)
        body = asposewordscloud.BookmarkData(bookmark_name, 'This will be the text for Aspose')
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.UpdateBookmarkRequest(remote_name, body, bookmark_name,
                                                                                   os.path.join(
                                                                                       self.remote_test_folder,
                                                                                       self.test_folder),
                                                                                   dest_file_name=dest_name)
        result = self.words_api.update_bookmark(request)
        self.assertIsNotNone(result, 'Error has occurred while update document bookmark')
