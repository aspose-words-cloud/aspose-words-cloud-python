#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_convert_document.py">
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


class TestConvertDocument(BaseTestContext):
    test_folder = 'DocumentActions/ConvertDocument'

    #
    # Test for saving document with specified format
    #
    def test_save_as(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPostDocumentSaveAs.docx'
        dest_name = os.path.join(self.remote_test_out, 'TestPostDocumentSaveAs.pdf')
        save_options = asposewordscloud.SaveOptionsData(save_format='pdf', file_name=dest_name)
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))

        request = asposewordscloud.models.requests.SaveAsRequest(remote_name, save_options,
                                                                           os.path.join(self.remote_test_folder,
                                                                                        self.test_folder))
        result = self.words_api.save_as(request)
        self.assertTrue(result.save_result is not None, 'Error has occurred while convert document')

    #
    # Test for saving document with specified format
    #
    def test_post_save_document_as_from_pdf_to_doc(self):
        filename = '45.pdf'
        remote_name = 'TestPostDocumentSaveAsFromPdfToDoc.docx'
        dest_name = os.path.join(self.remote_test_out, 'TestPostDocumentSaveAs.docx')
        save_options = asposewordscloud.SaveOptionsData(save_format='docx', file_name=dest_name)
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))

        request = asposewordscloud.models.requests.SaveAsRequest(remote_name, save_options,
                                                                           os.path.join(self.remote_test_folder,
                                                                                        self.test_folder))
        result = self.words_api.save_as(request)
        self.assertTrue(result.save_result is not None, 'Error has occurred while convert document')

    #
    # Test for document conversion without storage
    #
    def test_convert_document(self):
        _format = 'pdf'
        filename = 'test_multi_pages.docx'
        request = asposewordscloud.models.requests.ConvertDocumentRequest(open(os.path.join(self.local_common_folder,
                                                                                        filename), 'rb'),
                                                                           _format)
        result = self.words_api.convert_document(request)
        self.assertTrue(len(result) > 0, 'Error has occurred while convert document')

    #
    # Test for saving document with specified format
    #
    def test_save_as_tiff(self):
        filename = '45.pdf'
        remote_name = 'TestPutDocumentSaveAsTiff.docx'
        dest_name = os.path.join(self.remote_test_out, 'TestPostDocumentSaveAsTiff.tiff')
        save_options = asposewordscloud.SaveOptionsData(save_format='tiff', file_name=dest_name)
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))

        request = asposewordscloud.models.requests.SaveAsTiffRequest(remote_name, save_options,
                                                                              os.path.join(self.remote_test_folder,
                                                                                           self.test_folder))
        result = self.words_api.save_as_tiff(request)
        self.assertTrue(result.save_result is not None, 'Error has occurred while convert document')

    #
    # Test for saving document with specified format
    #
    def test_get_document_with_format(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentWithFormat.docx'
        _format = 'text'
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetDocumentWithFormatRequest(remote_name, _format,
                                                                                os.path.join(self.remote_test_folder,
                                                                                             self.test_folder))
        result = self.words_api.get_document_with_format(request)
        self.assertTrue(len(result) > 0, 'Error has occurred while convert document')

    #
    # Test for saving document with specified format
    #
    def test_get_document_with_format_and_out_path(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentWithFormat.docx'
        _format = 'text'
        out_path = os.path.join(self.remote_test_out, remote_name)
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetDocumentWithFormatRequest(remote_name, _format,
                                                                                os.path.join(self.remote_test_folder,
                                                                                             self.test_folder),
                                                                                out_path=out_path)
        result = self.words_api.get_document_with_format(request)
        self.assertTrue(len(result) > 0, 'Error has occurred while convert document')
