#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_form_field.py">
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


class TestFormField(BaseTestContext):
    test_folder = 'DocumentElements/FormFields'

    #
    #  Test for updating footnote from document
    #
    def test_post_form_field(self):
        filename = 'FormFilled.docx'
        remote_name = 'TestPostFormField.docx'
        dest_name = os.path.join(self.remote_test_out, remote_name)
        index = 0
        body = asposewordscloud.FormFieldTextInput(name='FullName', enabled=True, calculate_on_exit=True, status_text='',
                                                 text_input_type='Regular', text_input_default='')
        with open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.PostFormFieldRequest(remote_name, body, index,
                                                                      os.path.join(
                                                                          self.remote_test_folder,
                                                                          self.test_folder),
                                                                      dest_file_name=dest_name, node_path='sections/0')
        result = self.words_api.post_form_field(request)
        self.assertTrue(result.code == 200, 'Error has occurred while update from field')

    #
    #  Test for inserting footnote from document
    #
    def test_put_form_field(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPutFormField.docx'
        dest_name = os.path.join(self.remote_test_out, remote_name)
        body = asposewordscloud.FormFieldTextInput(name='FullName', enabled=True, calculate_on_exit=True, status_text='',
                                                 text_input_type='Regular', text_input_default='123',
                                                 text_input_format='UPPERCASE')
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.PutFormFieldRequest(remote_name, body,
                                                                     os.path.join(
                                                                         self.remote_test_folder,
                                                                         self.test_folder),
                                                                     dest_file_name=dest_name, node_path='sections/0')
        result = self.words_api.put_form_field(request)
        self.assertTrue(result.code == 200, 'Error has occurred while insert from field')

    #
    #  Test for removing form field
    #
    def test_delete_form_field(self):
        filename = 'FormFilled.docx'
        remote_name = 'TestDeleteFormField.docx'
        index = 0
        with open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.DeleteFormFieldRequest(remote_name, index,
                                                                        os.path.join(
                                                                            self.remote_test_folder,
                                                                            self.test_folder),
                                                                        node_path='sections/0')
        result = self.words_api.delete_form_field(request)
        self.assertTrue(result.code == 200, 'Error has occurred while delete from field')

    #
    #  Test for getting form field
    #
    def test_get_form_field(self):
        filename = 'FormFilled.docx'
        remote_name = 'TestGetFormField.docx'
        index = 0
        with open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.GetFormFieldRequest(remote_name, index,
                                                                     os.path.join(
                                                                         self.remote_test_folder,
                                                                         self.test_folder),
                                                                     node_path='sections/0')
        result = self.words_api.get_form_field(request)
        self.assertTrue(result.code == 200, 'Error has occurred while get from field')

    #
    #  Test for getting form field
    #
    def test_get_form_fields(self):
        filename = 'FormFilled.docx'
        remote_name = 'TestGetFormFields.docx'
        with open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.GetFormFieldsRequest(remote_name,
                                                                      os.path.join(
                                                                          self.remote_test_folder,
                                                                          self.test_folder),
                                                                      node_path='sections/0')
        result = self.words_api.get_form_fields(request)
        self.assertTrue(result.code == 200, 'Error has occurred while get from fields')
