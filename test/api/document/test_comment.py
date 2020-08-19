# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_comment.py">
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
# Example of how to get comments from document.
#
class TestComment(BaseTestContext):
    #
    # Test for getting comment by specified comment's index.
    #
    def test_get_comment(self):
        remoteDataFolder = self.remote_test_folder + '/Comments'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetComment.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetCommentRequest(name=remoteFileName, comment_index=0, folder=remoteDataFolder)

        result = self.words_api.get_comment(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting all comments from document.
    #
    def test_get_comments(self):
        remoteDataFolder = self.remote_test_folder + '/Comments'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetComments.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetCommentsRequest(name=remoteFileName, folder=remoteDataFolder)

        result = self.words_api.get_comments(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for adding comment.
    #
    def test_insert_comment(self):
        remoteDataFolder = self.remote_test_folder + '/Comments'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestInsertComment.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestCommentRangeStartNode = asposewordscloud.NodeLink(node_id='0.3.0.3')
        requestCommentRangeStart = asposewordscloud.DocumentPosition(node=requestCommentRangeStartNode, offset=0)
        requestCommentRangeEndNode = asposewordscloud.NodeLink(node_id='0.3.0.3')
        requestCommentRangeEnd = asposewordscloud.DocumentPosition(node=requestCommentRangeEndNode, offset=0)
        requestComment = asposewordscloud.CommentInsert(range_start=requestCommentRangeStart, range_end=requestCommentRangeEnd, initial='IA', author='Imran Anwar', text='A new Comment')
        request = asposewordscloud.models.requests.InsertCommentRequest(name=remoteFileName, comment=requestComment, folder=remoteDataFolder)

        result = self.words_api.insert_comment(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating comment.
    #
    def test_update_comment(self):
        remoteDataFolder = self.remote_test_folder + '/Comments'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestUpdateComment.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestCommentRangeStartNode = asposewordscloud.NodeLink(node_id='0.3.0')
        requestCommentRangeStart = asposewordscloud.DocumentPosition(node=requestCommentRangeStartNode, offset=0)
        requestCommentRangeEndNode = asposewordscloud.NodeLink(node_id='0.3.0')
        requestCommentRangeEnd = asposewordscloud.DocumentPosition(node=requestCommentRangeEndNode, offset=0)
        requestComment = asposewordscloud.CommentUpdate(range_start=requestCommentRangeStart, range_end=requestCommentRangeEnd, initial='IA', author='Imran Anwar', text='A new Comment')
        request = asposewordscloud.models.requests.UpdateCommentRequest(name=remoteFileName, comment_index=0, comment=requestComment, folder=remoteDataFolder)

        result = self.words_api.update_comment(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # A test for DeleteComment.
    #
    def test_delete_comment(self):
        remoteDataFolder = self.remote_test_folder + '/Comments'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestDeleteComment.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteCommentRequest(name=remoteFileName, comment_index=0, folder=remoteDataFolder, dest_file_name=self.remote_test_out + '/' + remoteFileName)

        self.words_api.delete_comment(request)

