# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_form_field.py">
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
# Example of how to work with form field.
#
class TestFormField(BaseTestContext):
    #
    # Test for posting form field.
    #
    def test_update_form_field(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/FormFields'
        fieldFolder = 'DocumentElements/FormFields'
        remoteFileName = 'TestUpdateFormField.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, fieldFolder + '/FormFilled.docx'), 'rb'))

        requestFormField = asposewordscloud.FormFieldTextInput(name='FullName', enabled=True, calculate_on_exit=True, status_text='', text_input_type='Regular', text_input_default='No name')
        request = asposewordscloud.models.requests.UpdateFormFieldRequest(name=remoteFileName, form_field=requestFormField, index=0, node_path='sections/0', folder=remoteDataFolder, dest_file_name=self.remote_test_out + '/' + remoteFileName)

        result = self.words_api.update_form_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for posting form field without node path.
    #
    def test_update_form_field_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/FormFields'
        fieldFolder = 'DocumentElements/FormFields'
        remoteFileName = 'TestUpdateFormFieldWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, fieldFolder + '/FormFilled.docx'), 'rb'))

        requestFormField = asposewordscloud.FormFieldTextInput(name='FullName', enabled=True, calculate_on_exit=True, status_text='', text_input_type='Regular', text_input_default='No name')
        request = asposewordscloud.models.requests.UpdateFormFieldRequest(name=remoteFileName, form_field=requestFormField, index=0, folder=remoteDataFolder, dest_file_name=self.remote_test_out + '/' + remoteFileName)

        result = self.words_api.update_form_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting form field.
    #
    def test_get_form_field(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/FormFields'
        fieldFolder = 'DocumentElements/FormFields'
        remoteFileName = 'TestGetFormField.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, fieldFolder + '/FormFilled.docx'), 'rb'))

        request = asposewordscloud.models.requests.GetFormFieldRequest(name=remoteFileName, index=0, node_path='sections/0', folder=remoteDataFolder)

        result = self.words_api.get_form_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting form field without node path.
    #
    def test_get_form_field_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/FormFields'
        fieldFolder = 'DocumentElements/FormFields'
        remoteFileName = 'TestGetFormFieldWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, fieldFolder + '/FormFilled.docx'), 'rb'))

        request = asposewordscloud.models.requests.GetFormFieldRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        result = self.words_api.get_form_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting form fields.
    #
    def test_get_form_fields(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/FormFields'
        fieldFolder = 'DocumentElements/FormFields'
        remoteFileName = 'TestGetFormFields.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, fieldFolder + '/FormFilled.docx'), 'rb'))

        request = asposewordscloud.models.requests.GetFormFieldsRequest(name=remoteFileName, node_path='sections/0', folder=remoteDataFolder)

        result = self.words_api.get_form_fields(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting form fields without node path.
    #
    def test_get_form_fields_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/FormFields'
        fieldFolder = 'DocumentElements/FormFields'
        remoteFileName = 'TestGetFormFieldsWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, fieldFolder + '/FormFilled.docx'), 'rb'))

        request = asposewordscloud.models.requests.GetFormFieldsRequest(name=remoteFileName, folder=remoteDataFolder)

        result = self.words_api.get_form_fields(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for insert form field without node path.
    #
    def test_insert_form_field(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/FormFields'
        remoteFileName = 'TestInsertFormField.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, 'Common/test_multi_pages.docx'), 'rb'))

        requestFormField = asposewordscloud.FormFieldTextInput(name='FullName', enabled=True, calculate_on_exit=True, status_text='', text_input_type='Regular', text_input_default='123', text_input_format='UPPERCASE')
        request = asposewordscloud.models.requests.InsertFormFieldRequest(name=remoteFileName, form_field=requestFormField, node_path='sections/0/paragraphs/0', folder=remoteDataFolder, dest_file_name=self.remote_test_out + '/' + remoteFileName)

        result = self.words_api.insert_form_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for insert form field without node path.
    #
    def test_insert_form_field_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/FormFields'
        remoteFileName = 'TestInsertFormFieldWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, 'Common/test_multi_pages.docx'), 'rb'))

        requestFormField = asposewordscloud.FormFieldTextInput(name='FullName', enabled=True, calculate_on_exit=True, status_text='', text_input_type='Regular', text_input_default='123', text_input_format='UPPERCASE')
        request = asposewordscloud.models.requests.InsertFormFieldRequest(name=remoteFileName, form_field=requestFormField, folder=remoteDataFolder, dest_file_name=self.remote_test_out + '/' + remoteFileName)

        result = self.words_api.insert_form_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for deleting form field.
    #
    def test_delete_form_field(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/FormFields'
        fieldFolder = 'DocumentElements/FormFields'
        remoteFileName = 'TestDeleteFormField.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, fieldFolder + '/FormFilled.docx'), 'rb'))

        request = asposewordscloud.models.requests.DeleteFormFieldRequest(name=remoteFileName, index=0, node_path='sections/0', folder=remoteDataFolder, dest_file_name=self.remote_test_out + '/' + remoteFileName)

        self.words_api.delete_form_field(request)


    #
    # Test for deleting form field without node path.
    #
    def test_delete_form_field_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/FormFields'
        fieldFolder = 'DocumentElements/FormFields'
        remoteFileName = 'TestDeleteFormFieldWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, fieldFolder + '/FormFilled.docx'), 'rb'))

        request = asposewordscloud.models.requests.DeleteFormFieldRequest(name=remoteFileName, index=0, folder=remoteDataFolder, dest_file_name=self.remote_test_out + '/' + remoteFileName)

        self.words_api.delete_form_field(request)

