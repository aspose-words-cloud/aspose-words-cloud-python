#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_fields.py">
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


class TestFields(BaseTestContext):
    test_folder = 'DocumentElements/Fields'

    #
    #  Test for getting fields from document
    #
    def test_get_fields(self):
        filename = 'GetField.docx'
        remote_name = 'TestGetFields.docx'
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetFieldsRequest(remote_name,'sections/0',
                                                                  folder= os.path.join(
                                                                      self.remote_test_folder,
                                                                      self.test_folder))
        result = self.words_api.get_fields(request)
        self.assertIsNotNone(result, 'Error has occurred while get fields')

    #
    #  Test for getting fields from document without node path
    #
    def test_get_fields_without_node_path(self):
        filename = 'GetField.docx'
        remote_name = 'TestGetFieldsWithoutNodePath.docx'
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetFieldsWithoutNodePathRequest(remote_name,
                                                                  folder= os.path.join(
                                                                      self.remote_test_folder,
                                                                      self.test_folder))
        result = self.words_api.get_fields_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while get fields')

    #
    #  Test for getting field from document
    #
    def test_get_field(self):
        filename = 'GetField.docx'
        remote_name = 'TestGetField.docx'
        index = 0
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetFieldRequest(remote_name,'sections/0/paragraphs/0', index,
                                                                 folder= os.path.join(
                                                                     self.remote_test_folder,
                                                                     self.test_folder))
        result = self.words_api.get_field(request)
        self.assertIsNotNone(result, 'Error has occurred while get field')

    #
    #  Test for getting field from document
    #
    def test_get_field_without_node_path(self):
        filename = 'GetField.docx'
        remote_name = 'TestGetFieldWithoutNodePath.docx'
        index = 0
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetFieldWithoutNodePathRequest(remote_name, index,
                                                                 folder= os.path.join(
                                                                     self.remote_test_folder,
                                                                     self.test_folder))
        result = self.words_api.get_field_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while get field')

    #
    # Test for updating document field
    #
    def test_update_field(self):
        filename = 'GetField.docx'
        remote_name = 'TestPostField.docx'
        dest_name = os.path.join(self.remote_test_out, remote_name)
        index = 0
        body = asposewordscloud.Field(None, '0.0.3', '{ NUMPAGES }')
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.UpdateFieldRequest(remote_name, body,'sections/0/paragraphs/0', index,
                                                                  folder= os.path.join(
                                                                      self.remote_test_folder,
                                                                      self.test_folder),
                                                                  dest_file_name=dest_name)
        result = self.words_api.update_field(request)
        self.assertIsNotNone(result, 'Error has occurred while post field')

    #
    # Test for inserting document field
    #
    def test_insert_field(self):
        filename = 'GetField.docx'
        remote_name = 'TestPutField.docx'
        body = asposewordscloud.Field(None, '0.0.3', '{ NUMPAGES }')
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.InsertFieldRequest(remote_name, body,'sections/0/paragraphs/0',
                                                                 folder= os.path.join(
                                                                     self.remote_test_folder,
                                                                     self.test_folder))
        result = self.words_api.insert_field(request)
        self.assertIsNotNone(result, 'Error has occurred while put field')

    #
    # Test for inserting document field without node path
    #
    def test_insert_field_without_node_path(self):
        filename = 'GetField.docx'
        remote_name = 'TestPutFieldWithoutNodePath.docx'
        body = asposewordscloud.Field(None, '0.0.3', '{ NUMPAGES }')
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.InsertFieldWithoutNodePathRequest(remote_name, body,
                                                                 folder= os.path.join(
                                                                     self.remote_test_folder,
                                                                     self.test_folder))
        result = self.words_api.insert_field_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while put field')

    #
    # Test for reevaluating fields in document
    #
    def test_update_fields(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPostUpdateDocumentFields.docx'
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.UpdateFieldsRequest(remote_name,
                                                                                 os.path.join(
                                                                                     self.remote_test_folder,
                                                                                     self.test_folder))
        result = self.words_api.update_fields(request)
        self.assertIsNotNone(result, 'Error has occurred while post update document fields')

    #
    # Test for inserting page numbers
    #
    def test_insert_page_numbers(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPostInsertPageNumbers.docx'
        dest_name = os.path.join(self.remote_test_out, remote_name)
        body = asposewordscloud.models.PageNumber('{PAGE} of { NUMPAGES }', 'center', False, True)
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.InsertPageNumbersRequest(remote_name, body,
                                                                              os.path.join(
                                                                                  self.remote_test_folder,
                                                                                  self.test_folder),
                                                                              dest_file_name=dest_name)
        result = self.words_api.insert_page_numbers(request)
        self.assertIsNotNone(result, 'Error has occurred while post insert page numbers')

    #
    # Test for removing field
    #
    def test_delete_field(self):
        filename = 'GetField.docx'
        remote_name = 'TestDeleteField.docx'
        index = 0
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.DeleteFieldRequest(remote_name, 'sections/0/paragraphs/0', index,
                                                                    folder= os.path.join(
                                                                        self.remote_test_folder,
                                                                        self.test_folder))
        result = self.words_api.delete_field(request)
        self.assertIsNotNone(result, 'Error has occurred while delete field')

    #
    # Test for removing field without node path
    #
    def test_delete_field_without_node_path(self):
        filename = 'GetField.docx'
        remote_name = 'TestDeleteFieldWithoutNodePath.docx'
        index = 0
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.DeleteFieldWithoutNodePathRequest(remote_name, index,
                                                                    folder= os.path.join(
                                                                        self.remote_test_folder,
                                                                        self.test_folder))
        result = self.words_api.delete_field_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while delete field')

    #
    # Test for removing field
    #
    def test_delete_fields(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestDeleteFields.docx'
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.DeleteFieldsRequest(remote_name,
                                                                    'sections/0',
                                                                     os.path.join(
                                                                         self.remote_test_folder,
                                                                         self.test_folder))
        result = self.words_api.delete_fields(request)
        self.assertIsNotNone(result, 'Error has occurred while delete fields')

    #
    # Test for removing field without node path
    #
    def test_delete_fields_without_node_path(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestDeleteFieldsWithoutNodePath.docx'
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.DeleteFieldsWithoutNodePathRequest(remote_name,
                                                                     os.path.join(
                                                                         self.remote_test_folder,
                                                                         self.test_folder))
        result = self.words_api.delete_fields_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while delete fields')
