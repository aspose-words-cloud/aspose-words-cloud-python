# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_styles.py">
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
# Example of how to work with styles.
#
class TestStyles(BaseTestContext):
    #
    # Test for getting styles from document.
    #
    def test_get_styles(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Styles'
        localFile = 'DocumentElements/Styles/GetStyles.docx'
        remoteFileName = 'TestGetStyles.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetStylesRequest(name=remoteFileName, folder=remoteDataFolder)

        result = self.words_api.get_styles(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting style from document.
    #
    def test_get_style(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Styles'
        localFile = 'DocumentElements/Styles/GetStyles.docx'
        remoteFileName = 'TestGetStyle.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetStyleRequest(name=remoteFileName, style_name='Heading 1', folder=remoteDataFolder)

        result = self.words_api.get_style(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating style from document.
    #
    def test_update_style(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Styles'
        localFile = 'DocumentElements/Styles/GetStyles.docx'
        remoteFileName = 'TestUpdateStyle.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestStyleUpdate = asposewordscloud.StyleUpdate(name='My Style')
        request = asposewordscloud.models.requests.UpdateStyleRequest(name=remoteFileName, style_update=requestStyleUpdate, style_name='Heading 1', folder=remoteDataFolder)

        result = self.words_api.update_style(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for inserting style from document.
    #
    def test_insert_style(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Styles'
        localFile = 'DocumentElements/Styles/GetStyles.docx'
        remoteFileName = 'TestInsertStyle.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestStyleInsert = asposewordscloud.StyleInsert(style_name='My Style', style_type='Paragraph')
        request = asposewordscloud.models.requests.InsertStyleRequest(name=remoteFileName, style_insert=requestStyleInsert, folder=remoteDataFolder)

        result = self.words_api.insert_style(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for coping style from document.
    #
    def test_copy_style(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Styles'
        localFile = 'DocumentElements/Styles/GetStyles.docx'
        remoteFileName = 'TestCopyStyle.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestStyleCopy = asposewordscloud.StyleCopy(style_name='Heading 1')
        request = asposewordscloud.models.requests.CopyStyleRequest(name=remoteFileName, style_copy=requestStyleCopy, folder=remoteDataFolder)

        result = self.words_api.copy_style(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting style from document element.
    #
    def test_get_style_from_document_element(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Styles'
        localFile = 'DocumentElements/Styles/GetStyles.docx'
        remoteFileName = 'TestGetStyleFromDocumentElement.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetStyleFromDocumentElementRequest(name=remoteFileName, styled_node_path='paragraphs/1/paragraphFormat', folder=remoteDataFolder)

        result = self.words_api.get_style_from_document_element(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for applying style to document element.
    #
    def test_apply_style_to_document_element(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Styles'
        localFile = 'DocumentElements/Styles/GetStyles.docx'
        remoteFileName = 'TestApplyStyleToDocumentElement.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestStyleApply = asposewordscloud.StyleApply(style_name='Heading 1')
        request = asposewordscloud.models.requests.ApplyStyleToDocumentElementRequest(name=remoteFileName, style_apply=requestStyleApply, styled_node_path='paragraphs/1/paragraphFormat', folder=remoteDataFolder)

        result = self.words_api.apply_style_to_document_element(request)
        self.assertIsNotNone(result, 'Error has occurred.')

