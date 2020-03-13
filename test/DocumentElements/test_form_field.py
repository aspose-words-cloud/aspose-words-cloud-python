#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_form_field.py">
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


class TestFormField(BaseTestContext):
    test_folder = 'DocumentElements/FormFields'

    #
    #  Test for updating footnote from document
    #
    def test_update_form_field(self):
        filename = 'FormFilled.docx'
        remote_name = 'TestPostFormField.docx'
        dest_name = os.path.join(self.remote_test_out, remote_name)
        index = 0
        body = asposewordscloud.FormFieldTextInput(name='FullName', enabled=True, calculate_on_exit=True, status_text='',
                                                 text_input_type='Regular', text_input_default='')
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.UpdateFormFieldRequest(remote_name, body, 'sections/0', index,
                                                                      folder= os.path.join(
                                                                          self.remote_test_folder,
                                                                          self.test_folder),
                                                                      dest_file_name=dest_name)
        result = self.words_api.update_form_field(request)
        self.assertIsNotNone(result, 'Error has occurred while update from field')

    #
    #  Test for updating footnote from document without node path
    #
    def test_update_form_field_without_node_path(self):
        filename = 'FormFilled.docx'
        remote_name = 'TestPostFormFieldWithoutNodePath.docx'
        dest_name = os.path.join(self.remote_test_out, remote_name)
        index = 0
        body = asposewordscloud.FormFieldTextInput(name='FullName', enabled=True, calculate_on_exit=True, status_text='',
                                                 text_input_type='Regular', text_input_default='')
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.UpdateFormFieldWithoutNodePathRequest(remote_name, body, index,
                                                                      folder= os.path.join(
                                                                          self.remote_test_folder,
                                                                          self.test_folder),
                                                                      dest_file_name=dest_name)
        result = self.words_api.update_form_field_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while update from field')

    #
    #  Test for inserting footnote from document
    #
    def test_insert_form_field(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPutFormField.docx'
        dest_name = os.path.join(self.remote_test_out, remote_name)
        body = asposewordscloud.FormFieldTextInput(name='FullName', enabled=True, calculate_on_exit=True, status_text='',
                                                 text_input_type='Regular', text_input_default='123',
                                                 text_input_format='UPPERCASE')
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.InsertFormFieldRequest(remote_name, body, 'sections/0',
                                                                     folder= os.path.join(
                                                                         self.remote_test_folder,
                                                                         self.test_folder),
                                                                     dest_file_name=dest_name)
        result = self.words_api.insert_form_field(request)
        self.assertIsNotNone(result, 'Error has occurred while insert from field')

    #
    #  Test for inserting footnote from document without node path
    #
    def test_insert_form_field_without_node_path(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPutFormFieldWithoutNodePath.docx'
        dest_name = os.path.join(self.remote_test_out, remote_name)
        body = asposewordscloud.FormFieldTextInput(name='FullName', enabled=True, calculate_on_exit=True, status_text='',
                                                 text_input_type='Regular', text_input_default='123',
                                                 text_input_format='UPPERCASE')
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.InsertFormFieldWithoutNodePathRequest(remote_name, body,
                                                                     folder= os.path.join(
                                                                         self.remote_test_folder,
                                                                         self.test_folder),
                                                                     dest_file_name=dest_name)
        result = self.words_api.insert_form_field_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while insert from field')

    #
    #  Test for removing form field
    #
    def test_delete_form_field(self):
        filename = 'FormFilled.docx'
        remote_name = 'TestDeleteFormField.docx'
        index = 0
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.DeleteFormFieldRequest(remote_name,'sections/0', index,
                                                                        folder = os.path.join(
                                                                            self.remote_test_folder,
                                                                            self.test_folder))
        result = self.words_api.delete_form_field(request)
        self.assertIsNotNone(result, 'Error has occurred while delete from field')

    #
    #  Test for removing form field without node path
    #
    def test_delete_form_field_without_node_path(self):
        filename = 'FormFilled.docx'
        remote_name = 'TestDeleteFormFieldWithoutNodePath.docx'
        index = 0
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.DeleteFormFieldWithoutNodePathRequest(remote_name, index,
                                                                        folder = os.path.join(
                                                                            self.remote_test_folder,
                                                                            self.test_folder))
        result = self.words_api.delete_form_field_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while delete from field')

    #
    #  Test for getting form field
    #
    def test_get_form_field(self):
        filename = 'FormFilled.docx'
        remote_name = 'TestGetFormField.docx'
        index = 0
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetFormFieldRequest(remote_name, 'sections/0', index,
                                                                     folder= os.path.join(
                                                                         self.remote_test_folder,
                                                                         self.test_folder))
        result = self.words_api.get_form_field(request)
        self.assertIsNotNone(result, 'Error has occurred while get from field')

    #
    #  Test for getting form field without node path
    #
    def test_get_form_field_without_node_path(self):
        filename = 'FormFilled.docx'
        remote_name = 'TestGetFormFieldWithoutNodePath.docx'
        index = 0
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetFormFieldWithoutNodePathRequest(remote_name, index,
                                                                     folder= os.path.join(
                                                                         self.remote_test_folder,
                                                                         self.test_folder))
        result = self.words_api.get_form_field_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while get from field')

    #
    #  Test for getting form field
    #
    def test_get_form_fields(self):
        filename = 'FormFilled.docx'
        remote_name = 'TestGetFormFields.docx'
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetFormFieldsRequest(remote_name, 'sections/0',
                                                                      folder= os.path.join(
                                                                          self.remote_test_folder,
                                                                          self.test_folder))
        result = self.words_api.get_form_fields(request)
        self.assertIsNotNone(result, 'Error has occurred while get from fields')

    #
    #  Test for getting form field without node path
    #
    def test_get_form_fields_without_node_path(self):
        filename = 'FormFilled.docx'
        remote_name = 'TestGetFormFieldsWithoutNodePath.docx'
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetFormFieldsWithoutNodePathRequest(remote_name,
                                                                      folder= os.path.join(
                                                                          self.remote_test_folder,
                                                                          self.test_folder))
        result = self.words_api.get_form_fields_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while get from fields')
