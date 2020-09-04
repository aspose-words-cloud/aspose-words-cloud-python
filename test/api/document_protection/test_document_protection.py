# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_document_protection.py">
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
# Example of how to set document protection.
#
class TestDocumentProtection(BaseTestContext):
    #
    # Test for setting document protection.
    #
    def test_protect_document(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DocumentProtection'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestProtectDocument.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestProtectionRequest = asposewordscloud.ProtectionRequest(new_password='123')
        request = asposewordscloud.models.requests.ProtectDocumentRequest(name=remoteFileName, protection_request=requestProtectionRequest, folder=remoteDataFolder, dest_file_name=self.remote_test_out + '/' + remoteFileName)

        result = self.words_api.protect_document(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting document protection.
    #
    def test_get_document_protection(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DocumentProtection'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentProtection.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentProtectionRequest(name=remoteFileName, folder=remoteDataFolder)

        result = self.words_api.get_document_protection(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for changing document protection.
    #
    def test_change_document_protection(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DocumentProtection'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestChangeDocumentProtection.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestProtectionRequest = asposewordscloud.ProtectionRequest(new_password='321')
        request = asposewordscloud.models.requests.ProtectDocumentRequest(name=remoteFileName, protection_request=requestProtectionRequest, folder=remoteDataFolder)

        result = self.words_api.protect_document(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting unprotect document.
    #
    def test_delete_unprotect_document(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DocumentProtection'
        localFilePath = 'DocumentActions/DocumentProtection/SampleProtectedBlankWordDocument.docx'
        remoteFileName = 'TestDeleteUnprotectDocument.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFilePath), 'rb'))

        requestProtectionRequest = asposewordscloud.ProtectionRequest(password='aspose')
        request = asposewordscloud.models.requests.UnprotectDocumentRequest(name=remoteFileName, protection_request=requestProtectionRequest, folder=remoteDataFolder)

        result = self.words_api.unprotect_document(request)
        self.assertIsNotNone(result, 'Error has occurred.')

