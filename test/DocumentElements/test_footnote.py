#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_footnote.py">
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


class TestFootnote(BaseTestContext):
    test_folder = 'DocumentElements/Footnotes'

    #
    #  Test for getting footnote from document
    #
    def test_get_footnote(self):
        filename = 'Footnote.doc'
        remote_name = 'TestGetFootnote.docx'
        index = 0
        with open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.GetFootnoteRequest(remote_name, index,
                                                                    os.path.join(
                                                                        self.remote_test_folder,
                                                                        self.test_folder))
        result = self.words_api.get_footnote(request)
        self.assertTrue(result.code == 200, 'Error has occurred while get footnote')

    #
    #  Test for getting footnotes from document
    #
    def test_get_footnotes(self):
        filename = 'Footnote.doc'
        remote_name = 'TestGetFootnotes.docx'
        with open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.GetFootnotesRequest(remote_name,
                                                                     os.path.join(
                                                                         self.remote_test_folder,
                                                                         self.test_folder))
        result = self.words_api.get_footnotes(request)
        self.assertTrue(result.code == 200, 'Error has occurred while get footnotes')

    #
    #  Test for delete footnote from document
    #
    def test_delete_footnote(self):
        filename = 'Footnote.doc'
        remote_name = 'TestDeleteFootnote.docx'
        index = 0
        with open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.DeleteFootnoteRequest(remote_name, index,
                                                                       os.path.join(
                                                                           self.remote_test_folder,
                                                                           self.test_folder))
        result = self.words_api.delete_footnote(request)
        self.assertTrue(result.code == 200, 'Error has occurred while delete footnote')

    #
    #  Test for update footnote from document
    #
    def test_post_footnote(self):
        filename = 'Footnote.doc'
        remote_name = 'TestPostFootnote.docx'
        index = 0
        footnote = asposewordscloud.Footnote(text='new text is here')
        with open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.PostFootnoteRequest(remote_name, footnote, index,
                                                                     os.path.join(
                                                                         self.remote_test_folder,
                                                                         self.test_folder))
        result = self.words_api.post_footnote(request)
        self.assertTrue(result.code == 200, 'Error has occurred while update footnote')

    #
    #  Test for insert footnote from document
    #
    def test_put_footnote(self):
        filename = 'Footnote.doc'
        remote_name = 'TestPutFootnote.docx'
        footnote = asposewordscloud.Footnote(text='new text is here', footnote_type='Endnote')
        with open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.PutFootnoteRequest(remote_name, footnote,
                                                                    os.path.join(
                                                                        self.remote_test_folder,
                                                                        self.test_folder))
        result = self.words_api.put_footnote(request)
        self.assertTrue(result.code == 200, 'Error has occurred while insert footnote')
