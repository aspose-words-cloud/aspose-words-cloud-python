#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_fields.py">
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


class TestFields(BaseTestContext):
    test_folder = 'DocumentElements/Fields'

    #
    #  Test for getting fields from document
    #
    def test_get_fields(self):
        filename = 'GetField.docx'
        remote_name = 'TestGetFields.docx'
        with open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.GetFieldsRequest(remote_name,
                                                                  os.path.join(
                                                                      self.remote_test_folder,
                                                                      self.test_folder),
                                                                  node_path='sections/0')
        result = self.words_api.get_fields(request)
        self.assertTrue(result.code == 200, 'Error has occurred while get fields')

    #
    #  Test for getting field from document
    #
    def test_get_field(self):
        filename = 'GetField.docx'
        remote_name = 'TestGetField.docx'
        index = 0
        with open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.GetFieldRequest(remote_name, index,
                                                                 os.path.join(
                                                                     self.remote_test_folder,
                                                                     self.test_folder),
                                                                 node_path='sections/0/paragraphs/0')
        result = self.words_api.get_field(request)
        self.assertTrue(result.code == 200, 'Error has occurred while get field')

    #
    # Test for updating document field
    #
    def test_post_field(self):
        filename = 'GetField.docx'
        remote_name = 'TestPostField.docx'
        dest_name = os.path.join(self.remote_test_out, remote_name)
        index = 0
        body = asposewordscloud.Field(None, '0.0.3', '{ NUMPAGES }')
        with open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.PostFieldRequest(remote_name, body, index,
                                                                  os.path.join(
                                                                      self.remote_test_folder,
                                                                      self.test_folder),
                                                                  node_path='sections/0/paragraphs/0',
                                                                  dest_file_name=dest_name)
        result = self.words_api.post_field(request)
        self.assertTrue(result.code == 200, 'Error has occurred while post field')

    #
    # Test for inserting document field
    #
    def test_put_field(self):
        filename = 'GetField.docx'
        remote_name = 'TestPutField.docx'
        body = asposewordscloud.Field(None, '0.0.3', '{ NUMPAGES }')
        with open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.PutFieldRequest(remote_name, body,
                                                                 os.path.join(
                                                                     self.remote_test_folder,
                                                                     self.test_folder),
                                                                 node_path='sections/0/paragraphs/0')
        result = self.words_api.put_field(request)
        self.assertTrue(result.code == 200, 'Error has occurred while put field')

    #
    # Test for reevaluating fields in document
    #
    def test_post_update_document_fields(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPostUpdateDocumentFields.docx'
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.PostUpdateDocumentFieldsRequest(remote_name,
                                                                                 os.path.join(
                                                                                     self.remote_test_folder,
                                                                                     self.test_folder))
        result = self.words_api.post_update_document_fields(request)
        self.assertTrue(result.code == 200, 'Error has occurred while post update document fields')

    #
    # Test for inserting page numbers
    #
    def test_post_insert_page_numbers(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPostInsertPageNumbers.docx'
        dest_name = os.path.join(self.remote_test_out, remote_name)
        body = asposewordscloud.models.PageNumber('{PAGE} of { NUMPAGES }', 'center', False, True)
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.PostInsertPageNumbersRequest(remote_name, body,
                                                                              os.path.join(
                                                                                  self.remote_test_folder,
                                                                                  self.test_folder),
                                                                              dest_file_name=dest_name)
        result = self.words_api.post_insert_page_numbers(request)
        self.assertTrue(result.code == 200, 'Error has occurred while post insert page numbers')

    #
    # Test for removing field
    #
    def test_delete_field(self):
        filename = 'GetField.docx'
        remote_name = 'TestDeleteField.docx'
        index = 0
        with open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.DeleteFieldRequest(remote_name, index,
                                                                    os.path.join(
                                                                        self.remote_test_folder,
                                                                        self.test_folder),
                                                                    node_path='sections/0/paragraphs/0')
        result = self.words_api.delete_field(request)
        self.assertTrue(result.code == 200, 'Error has occurred while delete field')

    #
    # Test for removing field
    #
    def test_delete_fields(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestDeleteFields.docx'
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.DeleteFieldsRequest(remote_name,
                                                                     os.path.join(
                                                                         self.remote_test_folder,
                                                                         self.test_folder))
        result = self.words_api.delete_fields(request)
        self.assertTrue(result.code == 200, 'Error has occurred while delete fields')
