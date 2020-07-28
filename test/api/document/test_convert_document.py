# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_convert_document.py">
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
# Example of how to convert document to one of the available formats.
#
class TestConvertDocument(BaseTestContext):
    #
    # Test for converting document to one of the available formats.
    #
    def test_save_as(self):
        remoteFolder = self.remote_test_folder + '/DocumentActions/ConvertDocument'
        localName = 'test_multi_pages.docx'
        remoteName = 'TestSaveAs.docx'

        self.upload_file(remoteFolder + '/' + remoteName, open(os.path.join(self.local_test_folder, 'Common/' + localName), 'rb'))

        requestSaveOptionsData = asposewordscloud.SaveOptionsData(save_format='pdf', file_name=self.remote_test_out + '/TestSaveAs.pdf')
        request = asposewordscloud.models.requests.SaveAsRequest(name=remoteName, save_options_data=requestSaveOptionsData, folder=remoteFolder)

        result = self.words_api.save_as(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for converting document online to one of the available formats.
    #
    def test_save_as_online(self):
        localName = 'test_multi_pages.docx'

        requestSaveOptionsData = asposewordscloud.SaveOptionsData(save_format='pdf', file_name=self.remote_test_out + '/TestSaveAs.pdf')
        request = asposewordscloud.models.requests.SaveAsOnlineRequest(document=open(os.path.join(self.local_test_folder, 'Common/' + localName), 'rb'), save_options_data=requestSaveOptionsData)

        result = self.words_api.save_as_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for converting document to one of the available formats.
    #
    def test_save_as_docx(self):
        remoteFolder = self.remote_test_folder + '/DocumentActions/ConvertDocument'
        localFolder = 'DocumentActions/ConvertDocument'
        localName = '45.pdf'
        remoteName = 'TestSaveAsFromPdfToDoc.pdf'

        self.upload_file(remoteFolder + '/' + remoteName, open(os.path.join(self.local_test_folder, localFolder + '/' + localName), 'rb'))

        requestSaveOptionsData = asposewordscloud.SaveOptionsData(save_format='docx', file_name=self.remote_test_out + '/TestSaveAsFromPdfToDoc.docx')
        request = asposewordscloud.models.requests.SaveAsRequest(name=remoteName, save_options_data=requestSaveOptionsData, folder=remoteFolder)

        result = self.words_api.save_as(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for converting document to one of the available formats.
    #
    def test_save_as_tiff(self):
        remoteFolder = self.remote_test_folder + '/DocumentActions/ConvertDocument'
        localName = 'test_multi_pages.docx'
        remoteName = 'TestSaveAsTiff.pdf'

        self.upload_file(remoteFolder + '/' + remoteName, open(os.path.join(self.local_test_folder, 'Common/' + localName), 'rb'))

        requestSaveOptions = asposewordscloud.TiffSaveOptionsData(save_format='tiff', file_name=self.remote_test_out + '/abc.tiff')
        request = asposewordscloud.models.requests.SaveAsTiffRequest(name=remoteName, save_options=requestSaveOptions, folder=remoteFolder)

        result = self.words_api.save_as_tiff(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # A test for ConvertDocument.
    #
    def test_convert_document(self):
        localFolder = 'DocumentActions/ConvertDocument'

        request = asposewordscloud.models.requests.ConvertDocumentRequest(document=open(os.path.join(self.local_test_folder, localFolder + '/test_uploadfile.docx'), 'rb'), format='pdf')

        result = self.words_api.convert_document(request)
        self.assertIsNotNone(result, 'Error has occurred.')
