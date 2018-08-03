#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_comments.py">
#   Copyright (c) 2018 Aspose.Words for Cloud
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


class TestComments(BaseTestContext):
    test_folder = 'DocumentElements/Comments'

    #
    # Test for deleting comment
    #
    def test_delete_comment(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestDeleteComment.docx'
        comment_index = 0
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.DeleteCommentRequest(remote_name, comment_index,
                                                                        os.path.join(
                                                                            self.remote_test_folder,
                                                                            self.test_folder))
        result = self.words_api.delete_comment(request)
        self.assertTrue(result.code == 200, 'Error has occurred while delete comment')

    #
    # Test for getting comment
    #
    def test_get_comment(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetComment.docx'
        comment_index = 0
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.GetCommentRequest(remote_name, comment_index,
                                                                     os.path.join(
                                                                         self.remote_test_folder,
                                                                         self.test_folder))
        result = self.words_api.get_comment(request)
        self.assertTrue(result.code == 200, 'Error has occurred while get comment')

    #
    # Test for getting comment
    #
    def test_get_comments(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetComments.docx'
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.GetCommentsRequest(remote_name,
                                                                      os.path.join(
                                                                          self.remote_test_folder,
                                                                          self.test_folder))
        result = self.words_api.get_comments(request)
        self.assertTrue(result.code == 200, 'Error has occurred while get comments')

    #
    # Test for updating comment
    #
    def test_post_comment(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPostComment.docx'
        comment_index = 0
        node_link = asposewordscloud.NodeLink(None, '0.0.3')
        doc_pos = asposewordscloud.DocumentPosition(node_link, 0)
        body = asposewordscloud.Comment(None, 'Yaroslav Ekimov', initial='YE', range_start=doc_pos, range_end=doc_pos,
                                        text='A new comment')
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.PostCommentRequest(remote_name, comment_index, body,
                                                                      os.path.join(
                                                                          self.remote_test_folder,
                                                                          self.test_folder))
        result = self.words_api.post_comment(request)
        self.assertTrue(result.code == 200, 'Error has occurred while post comment')

    #
    # Test for adding comment
    #
    def test_put_comment(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPutComment.docx'
        node_link = asposewordscloud.NodeLink(None, '0.0.3')
        doc_pos = asposewordscloud.DocumentPosition(node_link, 0)
        body = asposewordscloud.Comment(None, 'Yaroslav Ekimov', initial='YE', range_start=doc_pos, range_end=doc_pos,
                                        text='A new comment')
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.PutCommentRequest(remote_name, body,
                                                                     os.path.join(
                                                                         self.remote_test_folder,
                                                                         self.test_folder))
        result = self.words_api.put_comment(request)
        self.assertTrue(result.code == 200, 'Error has occurred while put comment')
