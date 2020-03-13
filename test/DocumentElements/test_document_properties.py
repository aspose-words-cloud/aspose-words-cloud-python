#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_document_properties.py">
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


class TestDocumentProperties(BaseTestContext):
    test_folder = 'DocumentElements/DocumentProperties'

    #
    # Test for adding/updating document property
    #
    def test_create_or_update_document_property(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPutUpdateDocumentProperty.docx'
        property_name = 'AsposeAuthor'
        _prop = asposewordscloud.DocumentProperty(name=property_name, value='Yaroslav Ekimov')
        
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.CreateOrUpdateDocumentPropertyRequest(remote_name, property_name,
                                                                                         _prop,
                                                                                         os.path.join(
                                                                                             self.remote_test_folder,
                                                                                             self.test_folder))
        result = self.words_api.create_or_update_document_property(request)
        self.assertIsNotNone(result, 'Error has occurred while create or update document property')

    #
    # Test for deleting document property
    #
    def test_delete_document_property(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestDeleteDocumentProperty.docx'
        dest_name = os.path.join(self.remote_test_out, remote_name)
        property_name = 'testProp'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.DeleteDocumentPropertyRequest(remote_name, property_name,
                                                                                 os.path.join(
                                                                                     self.remote_test_folder,
                                                                                     self.test_folder),
                                                                                 dest_file_name=dest_name)
        result = self.words_api.delete_document_property(request)
        self.assertIsNotNone(result, 'Error has occurred while delete property')

    #
    # Test for getting document properties
    #
    def test_get_document_properties(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentProperties.docx'
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetDocumentPropertiesRequest(remote_name,
                                                                                os.path.join(
                                                                                    self.remote_test_folder,
                                                                                    self.test_folder))
        result = self.words_api.get_document_properties(request)
        self.assertIsNotNone(result, 'Error has occurred while get properties')

    #
    # Test for getting document property
    #
    def test_get_document_property(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentProperty.docx'
        property_name = 'Author'
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetDocumentPropertyRequest(remote_name, property_name,
                                                                              os.path.join(
                                                                                  self.remote_test_folder,
                                                                                  self.test_folder))
        result = self.words_api.get_document_property(request)
        self.assertIsNotNone(result, 'Error has occurred while get property')

