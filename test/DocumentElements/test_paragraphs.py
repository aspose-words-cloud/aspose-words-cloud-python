#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_paragraphs.py">
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


class TestParagraphs(BaseTestContext):
    test_folder = 'DocumentElements/Paragraphs'

    #
    # Test for removing paragraph
    #
    def test_delete_paragraph(self):
        filename = 'test_doc.docx'
        remote_name = 'TestDeleteParagraph.docx'
        index = 0

        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.DeleteParagraphRequest(remote_name, index,
                                                                        os.path.join(
                                                                            self.remote_test_folder,
                                                                            self.test_folder))
        result = self.words_api.delete_paragraph(request)
        self.assertTrue(result.code == 200, 'Error has occurred while delete paragraph')

    #
    # Test for getting paragraph
    #
    def test_get_document_paragraph(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentParagraph.docx'
        index = 0

        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.GetDocumentParagraphRequest(remote_name, index,
                                                                             os.path.join(
                                                                                 self.remote_test_folder,
                                                                                 self.test_folder))
        result = self.words_api.get_document_paragraph(request)
        self.assertTrue(result.code == 200, 'Error has occurred while get document paragraph')

    #
    # Test for getting paragraph run
    #
    def test_get_document_paragraph_run(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentParagraphRun.docx'
        index = 0
        paragraph_path = 'paragraphs/0'

        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.GetDocumentParagraphRunRequest(remote_name, paragraph_path, index,
                                                                                os.path.join(
                                                                                    self.remote_test_folder,
                                                                                    self.test_folder))
        result = self.words_api.get_document_paragraph_run(request)
        self.assertTrue(result.code == 200, 'Error has occurred while get document paragraph run')

    #
    # Test for getting paragraph font
    #
    def test_get_document_paragraph_run_font(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentParagraphRunFont.docx'
        index = 0
        paragraph_path = 'paragraphs/0'

        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.GetDocumentParagraphRunFontRequest(remote_name, paragraph_path, index,
                                                                                    os.path.join(
                                                                                        self.remote_test_folder,
                                                                                        self.test_folder))
        result = self.words_api.get_document_paragraph_run_font(request)
        self.assertTrue(result.code == 200, 'Error has occurred while get document paragraph run font')

    #
    # Test for getting paragraph run
    #
    def test_get_document_paragraph_runs(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentParagraphRuns.docx'
        paragraph_path = 'sections/0/paragraphs/0'

        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.GetDocumentParagraphRunsRequest(remote_name, paragraph_path,
                                                                                 os.path.join(
                                                                                     self.remote_test_folder,
                                                                                     self.test_folder))
        result = self.words_api.get_document_paragraph_runs(request)
        self.assertTrue(result.code == 200, 'Error has occurred while get document paragraph runs')

    #
    # Test for getting paragraphs
    #
    def test_get_document_paragraphs(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentParagraphs.docx'
        node_path = 'sections/0'

        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.GetDocumentParagraphsRequest(remote_name,
                                                                              os.path.join(
                                                                                  self.remote_test_folder,
                                                                                  self.test_folder),
                                                                              node_path=node_path)
        result = self.words_api.get_document_paragraphs(request)
        self.assertTrue(result.code == 200, 'Error has occurred while get document paragraph')

    #
    # Test for updating paragraph font
    #
    def test_post_document_paragraph_run_font(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPostDocumentParagraphRunFont.docx'
        dest_name = os.path.join(self.remote_test_out, remote_name)
        index = 0
        paragraph_path = 'paragraphs/0'
        body = asposewordscloud.Font(bold=True)

        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.PostDocumentParagraphRunFontRequest(remote_name, body, paragraph_path,
                                                                                     index,
                                                                                     os.path.join(
                                                                                         self.remote_test_folder,
                                                                                         self.test_folder),
                                                                                     dest_file_name=dest_name)
        result = self.words_api.post_document_paragraph_run_font(request)
        self.assertTrue(result.code == 200, 'Error has occurred while update document paragraph font')

    #
    # Test for inserting paragraph
    #
    def test_put_paragraph(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPutParagraph.docx'
        node_path = 'sections/0'
        body = asposewordscloud.ParagraphInsert('This is a new paragraph for your document')

        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.PutParagraphRequest(remote_name, body,
                                                                     os.path.join(
                                                                         self.remote_test_folder,
                                                                         self.test_folder),
                                                                     node_path=node_path)
        result = self.words_api.put_paragraph(request)
        self.assertTrue(result.code == 200, 'Error has occurred while put document paragraph')

    #
    # Test for paragraph rendering
    #
    def test_render_paragraph(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestRenderParagraph.docx'
        index = 0
        format = 'png'

        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.RenderParagraphRequest(remote_name, format, index,
                                                                        os.path.join(
                                                                            self.remote_test_folder,
                                                                            self.test_folder))
        result = self.words_api.render_paragraph(request)
        self.assertTrue(len(result) > 0, 'Error has occurred while render paragraph')
