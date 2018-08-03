#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_document_protection.py">
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


class TestDocumentProtection(BaseTestContext):
    test_folder = 'DocumentActions/DocumentProtection'

    #
    # Test for getting document protection
    #
    def test_get_document_protection(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentProtection.docx'
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)

        request = asposewordscloud.models.requests.GetDocumentProtectionRequest(remote_name,
                                                                                os.path.join(self.remote_test_folder,
                                                                                             self.test_folder))
        result = self.words_api.get_document_protection(request)
        self.assertTrue(result.code == 200, 'Error has occurred while get protect document')

    #
    # Test for inserting document protection
    #
    def test_put_protect_document(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPutProtectDocument.docx'
        body = asposewordscloud.ProtectionRequest(new_password='123')
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)

        request = asposewordscloud.models.requests.PutProtectDocumentRequest(remote_name, body,
                                                                             os.path.join(self.remote_test_folder,
                                                                                          self.test_folder))
        result = self.words_api.put_protect_document(request)
        self.assertTrue(result.code == 200, 'Error has occurred while put protect document')

    #
    # Test for updating document protection
    #
    def test_post_change_document_protection(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPostChangeDocumentProtection.docx'
        body = asposewordscloud.ProtectionRequest(new_password='')
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)

        request = asposewordscloud.models.requests.PostChangeDocumentProtectionRequest(remote_name, body,
                                                                                       os.path.join(
                                                                                           self.remote_test_folder,
                                                                                           self.test_folder))
        result = self.words_api.post_change_document_protection(request)
        self.assertTrue(result.code == 200, 'Error has occurred while put protect document')

    #
    # Test for removing document protection
    #
    def test_delete_unprotect_document(self):
        filename = 'SampleProtectedBlankWordDocument.docx'
        remote_name = 'TestDeleteUnprotectDocument.docx'
        body = asposewordscloud.ProtectionRequest('aspose')
        with open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)

        request = asposewordscloud.models.requests.DeleteUnprotectDocumentRequest(remote_name, body,
                                                                                  os.path.join(
                                                                                      self.remote_test_folder,
                                                                                      self.test_folder))
        result = self.words_api.delete_unprotect_document(request)
        self.assertTrue(result.code == 200, 'Error has occurred while put protect document')
