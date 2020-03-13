#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_paragraphs.py">
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


class TestParagraphs(BaseTestContext):
    test_folder = 'DocumentElements/Paragraphs'

    #
    # Test for removing paragraph
    #
    def test_delete_paragraph(self):
        filename = 'test_doc.docx'
        remote_name = 'TestDeleteParagraph.docx'
        index = 0

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.DeleteParagraphRequest(remote_name, '', index,
                                                                          os.path.join(
                                                                              self.remote_test_folder,
                                                                              self.test_folder))
        result = self.words_api.delete_paragraph(request)
        self.assertIsNotNone(result, 'Error has occurred while delete paragraph')

    #
    # Test for removing paragraph without node path
    #
    def test_delete_paragraph_without_node_path(self):
        filename = 'test_doc.docx'
        remote_name = 'TestDeleteParagraphWithoutNodePath.docx'
        index = 0

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.DeleteParagraphWithoutNodePathRequest(remote_name, index,
                                                                          os.path.join(
                                                                              self.remote_test_folder,
                                                                              self.test_folder))
        result = self.words_api.delete_paragraph_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while delete paragraph')

    #
    # Test for getting paragraph
    #
    def test_get_paragraph(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentParagraph.docx'
        index = 0

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetParagraphRequest(remote_name, '', index,
                                                                               os.path.join(
                                                                                   self.remote_test_folder,
                                                                                   self.test_folder))
        result = self.words_api.get_paragraph(request)
        self.assertIsNotNone(result, 'Error has occurred while get document paragraph')

    #
    # Test for getting paragraph without node path
    #
    def test_get_paragraph_without_node_path(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentParagraphWithoutNodePath.docx'
        index = 0

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetParagraphWithoutNodePathRequest(remote_name, index,
                                                                               os.path.join(
                                                                                   self.remote_test_folder,
                                                                                   self.test_folder))
        result = self.words_api.get_paragraph_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while get document paragraph')

    #
    # Test for getting paragraph run
    #
    def test_get_run(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentParagraphRun.docx'
        index = 0
        paragraph_path = 'paragraphs/0'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetRunRequest(remote_name, paragraph_path, index,
                                                                                  os.path.join(
                                                                                      self.remote_test_folder,
                                                                                      self.test_folder))
        result = self.words_api.get_run(request)
        self.assertIsNotNone(result, 'Error has occurred while get document paragraph run')

    #
    # Test for getting paragraph font
    #
    def test_get_run_font(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentParagraphRunFont.docx'
        index = 0
        paragraph_path = 'paragraphs/0'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetRunFontRequest(remote_name, paragraph_path,
                                                                                      index,
                                                                                      os.path.join(
                                                                                          self.remote_test_folder,
                                                                                          self.test_folder))
        result = self.words_api.get_run_font(request)
        self.assertIsNotNone(result, 'Error has occurred while get document paragraph run font')

    #
    # Test for getting paragraph run
    #
    def test_get_runs(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentParagraphRuns.docx'
        paragraph_path = 'sections/0/paragraphs/0'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetRunsRequest(remote_name, paragraph_path,
                                                                                   os.path.join(
                                                                                       self.remote_test_folder,
                                                                                       self.test_folder))
        result = self.words_api.get_runs(request)
        self.assertIsNotNone(result, 'Error has occurred while get document paragraph runs')

    #
    # Test for getting paragraphs
    #
    def test_get_paragraphs(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentParagraphs.docx'
        node_path = 'sections/0'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetParagraphsRequest(remote_name,node_path,
                                                                                folder= os.path.join(
                                                                                    self.remote_test_folder,
                                                                                    self.test_folder))
        result = self.words_api.get_paragraphs(request)
        self.assertIsNotNone(result, 'Error has occurred while get document paragraph')

    #
    # Test for getting paragraphs without node path
    #
    def test_get_paragraphs_without_node_path(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentParagraphsWithoutNodePath.docx'
        node_path = 'sections/0'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetParagraphsWithoutNodePathRequest(remote_name,
                                                                                folder= os.path.join(
                                                                                    self.remote_test_folder,
                                                                                    self.test_folder))
        result = self.words_api.get_paragraphs_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while get document paragraph')

    #
    # Test for updating paragraph font
    #
    def test_update_run_font(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPostDocumentParagraphRunFont.docx'
        dest_name = os.path.join(self.remote_test_out, remote_name)
        index = 0
        paragraph_path = 'paragraphs/0'
        body = asposewordscloud.Font(bold=True)

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.UpdateRunFontRequest(remote_name, body,
                                                                                       paragraph_path,
                                                                                       index,
                                                                                       os.path.join(
                                                                                           self.remote_test_folder,
                                                                                           self.test_folder),
                                                                                       dest_file_name=dest_name)
        result = self.words_api.update_run_font(request)
        self.assertIsNotNone(result, 'Error has occurred while update document paragraph font')

    #
    # Test for inserting paragraph
    #
    def test_insert_paragraph(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPutParagraph.docx'
        node_path = 'sections/0'
        body = asposewordscloud.ParagraphInsert('This is a new paragraph for your document')

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.InsertParagraphRequest(remote_name, body,
                                                                       folder= os.path.join(
                                                                           self.remote_test_folder,
                                                                           self.test_folder),
                                                                       node_path=node_path)
        result = self.words_api.insert_paragraph(request)
        self.assertIsNotNone(result, 'Error has occurred while put document paragraph')

    #
    # Test for paragraph rendering
    #
    def test_render_paragraph(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestRenderParagraph.docx'
        index = 0
        format = 'png'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.RenderParagraphRequest(remote_name, format, '', index,
                                                                          os.path.join(
                                                                              self.remote_test_folder,
                                                                              self.test_folder))
        result = self.words_api.render_paragraph(request)
        self.assertIsNotNone(result, 'Error has occurred while render paragraph')

    #
    # Test for paragraph rendering without node path
    #
    def test_render_paragraph_without_node_path(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestRenderParagraphWithoutNodePath.docx'
        index = 0
        format = 'png'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.RenderParagraphWithoutNodePathRequest(remote_name, format, index,
                                                                          os.path.join(
                                                                              self.remote_test_folder,
                                                                              self.test_folder))
        result = self.words_api.render_paragraph_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while render paragraph')

    #
    # Test for getting paragraph format
    #
    def test_get_paragraph_format(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'GetDocumentParagraphFormat.docx'
        index = 0

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetParagraphFormatRequest(remote_name, '', index,
                                                                                     os.path.join(
                                                                                         self.remote_test_folder,
                                                                                         self.test_folder))
        result = self.words_api.get_paragraph_format(request)
        self.assertIsNotNone(result, 'Error has occurred while get document paragraph format')

    #
    # Test for getting paragraph format without node path
    #
    def test_get_paragraph_format_without_node_path(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'GetDocumentParagraphFormatWithoutNodePath.docx'
        index = 0

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetParagraphFormatWithoutNodePathRequest(remote_name, index,
                                                                                     os.path.join(
                                                                                         self.remote_test_folder,
                                                                                         self.test_folder))
        result = self.words_api.get_paragraph_format_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while get document paragraph format')

    #
    # Test for updating paragraph format
    #
    def test_update_paragraph_format(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'PostDocumentParagraphFormat.docx'
        index = 0
        body = asposewordscloud.ParagraphFormat(alignment='Right')

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.UpdateParagraphFormatRequest(remote_name, body, '', index,
                                                                                      folder=os.path.join(
                                                                                          self.remote_test_folder,
                                                                                          self.test_folder))
        result = self.words_api.update_paragraph_format(request)
        self.assertIsNotNone(result, 'Error has occurred while update section page setup')
