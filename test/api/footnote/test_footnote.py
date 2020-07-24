# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_footnote.py">
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
# Example of how to work with footnotes.
#
class TestFootnote(BaseTestContext):
    #
    # Test for adding footnote.
    #
    def test_insert_footnote(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Footnotes'
        footnoteFolder = 'DocumentElements/Footnotes'
        remoteFileName = 'TestInsertFootnote.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, footnoteFolder + '/Footnote.doc'), 'rb'))

        requestFootnoteDto = asposewordscloud.FootnoteInsert(footnote_type='Endnote', text='test endnote')
        request = asposewordscloud.models.requests.InsertFootnoteRequest(name=remoteFileName, footnote_dto=requestFootnoteDto, node_path='', folder=remoteDataFolder)

        result = self.words_api.insert_footnote(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for adding footnote without node path.
    #
    def test_insert_footnote_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Footnotes'
        footnoteFolder = 'DocumentElements/Footnotes'
        remoteFileName = 'TestInsertFootnoteWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, footnoteFolder + '/Footnote.doc'), 'rb'))

        requestFootnoteDto = asposewordscloud.FootnoteInsert(footnote_type='Endnote', text='test endnote')
        request = asposewordscloud.models.requests.InsertFootnoteRequest(name=remoteFileName, footnote_dto=requestFootnoteDto, folder=remoteDataFolder)

        result = self.words_api.insert_footnote(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for deleting footnote.
    #
    def test_delete_footnote(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Footnotes'
        footnoteFolder = 'DocumentElements/Footnotes'
        remoteFileName = 'TestDeleteFootnote.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, footnoteFolder + '/Footnote.doc'), 'rb'))

        request = asposewordscloud.models.requests.DeleteFootnoteRequest(name=remoteFileName, index=0, node_path='', folder=remoteDataFolder)

        self.words_api.delete_footnote(request)


    #
    # Test for deleting footnote without node path.
    #
    def test_delete_footnote_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Footnotes'
        footnoteFolder = 'DocumentElements/Footnotes'
        remoteFileName = 'TestDeleteFootnoteWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, footnoteFolder + '/Footnote.doc'), 'rb'))

        request = asposewordscloud.models.requests.DeleteFootnoteRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        self.words_api.delete_footnote(request)


    #
    # Test for getting footnotes.
    #
    def test_get_footnotes(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Footnotes'
        footnoteFolder = 'DocumentElements/Footnotes'
        remoteFileName = 'TestGetFootnotes.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, footnoteFolder + '/Footnote.doc'), 'rb'))

        request = asposewordscloud.models.requests.GetFootnotesRequest(name=remoteFileName, node_path='', folder=remoteDataFolder)

        result = self.words_api.get_footnotes(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting footnotes without node path.
    #
    def test_get_footnotes_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Footnotes'
        footnoteFolder = 'DocumentElements/Footnotes'
        remoteFileName = 'TestGetFootnotesWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, footnoteFolder + '/Footnote.doc'), 'rb'))

        request = asposewordscloud.models.requests.GetFootnotesRequest(name=remoteFileName, folder=remoteDataFolder)

        result = self.words_api.get_footnotes(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting footnote.
    #
    def test_get_footnote(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Footnotes'
        footnoteFolder = 'DocumentElements/Footnotes'
        remoteFileName = 'TestGetFootnote.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, footnoteFolder + '/Footnote.doc'), 'rb'))

        request = asposewordscloud.models.requests.GetFootnoteRequest(name=remoteFileName, index=0, node_path='', folder=remoteDataFolder)

        result = self.words_api.get_footnote(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting footnote without node path.
    #
    def test_get_footnote_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Footnotes'
        footnoteFolder = 'DocumentElements/Footnotes'
        remoteFileName = 'TestGetFootnoteWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, footnoteFolder + '/Footnote.doc'), 'rb'))

        request = asposewordscloud.models.requests.GetFootnoteRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        result = self.words_api.get_footnote(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for updating footnote.
    #
    def test_update_footnote(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Footnotes'
        footnoteFolder = 'DocumentElements/Footnotes'
        remoteFileName = 'TestUpdateFootnote.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, footnoteFolder + '/Footnote.doc'), 'rb'))

        requestFootnoteDto = asposewordscloud.FootnoteUpdate(text='new text is here')
        request = asposewordscloud.models.requests.UpdateFootnoteRequest(name=remoteFileName, footnote_dto=requestFootnoteDto, index=0, node_path='', folder=remoteDataFolder)

        result = self.words_api.update_footnote(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for updating footnote without node path.
    #
    def test_update_footnote_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Footnotes'
        footnoteFolder = 'DocumentElements/Footnotes'
        remoteFileName = 'TestUpdateFootnoteWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, footnoteFolder + '/Footnote.doc'), 'rb'))

        requestFootnoteDto = asposewordscloud.FootnoteUpdate(text='new text is here')
        request = asposewordscloud.models.requests.UpdateFootnoteRequest(name=remoteFileName, footnote_dto=requestFootnoteDto, index=0, folder=remoteDataFolder)

        result = self.words_api.update_footnote(request)
        self.assertIsNotNone(result, 'Error has occurred.')
