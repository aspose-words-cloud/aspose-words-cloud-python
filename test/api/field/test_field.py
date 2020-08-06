# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_field.py">
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
# Example of how to work with field.
#
class TestField(BaseTestContext):
    #
    # Test for getting fields.
    #
    def test_get_fields(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        fieldFolder = 'DocumentElements/Fields'
        localFileName = 'GetField.docx'
        remoteFileName = 'TestGetFields.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, fieldFolder + '/' + localFileName), 'rb'))

        request = asposewordscloud.models.requests.GetFieldsRequest(name=remoteFileName, node_path='sections/0', folder=remoteDataFolder)

        result = self.words_api.get_fields(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting fields without node path.
    #
    def test_get_fields_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        fieldFolder = 'DocumentElements/Fields'
        localFileName = 'GetField.docx'
        remoteFileName = 'TestGetFieldsWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, fieldFolder + '/' + localFileName), 'rb'))

        request = asposewordscloud.models.requests.GetFieldsRequest(name=remoteFileName, folder=remoteDataFolder)

        result = self.words_api.get_fields(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting field by index.
    #
    def test_get_field(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        fieldFolder = 'DocumentElements/Fields'
        localFileName = 'GetField.docx'
        remoteFileName = 'TestGetField.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, fieldFolder + '/' + localFileName), 'rb'))

        request = asposewordscloud.models.requests.GetFieldRequest(name=remoteFileName, index=0, node_path='sections/0/paragraphs/0', folder=remoteDataFolder)

        result = self.words_api.get_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting field by index without node path.
    #
    def test_get_field_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        fieldFolder = 'DocumentElements/Fields'
        localFileName = 'GetField.docx'
        remoteFileName = 'TestGetFieldWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, fieldFolder + '/' + localFileName), 'rb'))

        request = asposewordscloud.models.requests.GetFieldRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        result = self.words_api.get_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for putting field.
    #
    def test_insert_field(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        textFolder = 'DocumentElements/Text'
        localFileName = 'SampleWordDocument.docx'
        remoteFileName = 'TestInsertField.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, textFolder + '/' + localFileName), 'rb'))

        requestField = asposewordscloud.FieldInsert(field_code='{ NUMPAGES }')
        request = asposewordscloud.models.requests.InsertFieldRequest(name=remoteFileName, field=requestField, node_path='sections/0/paragraphs/0', folder=remoteDataFolder)

        result = self.words_api.insert_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for putting field without node path.
    #
    def test_insert_field_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        textFolder = 'DocumentElements/Text'
        localFileName = 'SampleWordDocument.docx'
        remoteFileName = 'TestInsertFieldWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, textFolder + '/' + localFileName), 'rb'))

        requestField = asposewordscloud.FieldInsert(field_code='{ NUMPAGES }')
        request = asposewordscloud.models.requests.InsertFieldRequest(name=remoteFileName, field=requestField, folder=remoteDataFolder)

        result = self.words_api.insert_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for posting field.
    #
    def test_update_field(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        fieldFolder = 'DocumentElements/Fields'
        localFileName = 'GetField.docx'
        remoteFileName = 'TestUpdateField.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, fieldFolder + '/' + localFileName), 'rb'))

        requestField = asposewordscloud.FieldUpdate(field_code='{ NUMPAGES }')
        request = asposewordscloud.models.requests.UpdateFieldRequest(name=remoteFileName, field=requestField, index=0, node_path='sections/0/paragraphs/0', folder=remoteDataFolder)

        result = self.words_api.update_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for inserting page numbers field.
    #
    def test_insert_page_numbers(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        localFileName = 'test_multi_pages.docx'
        remoteFileName = 'TestInsertPageNumbers.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, 'Common/' + localFileName), 'rb'))

        requestPageNumber = asposewordscloud.PageNumber(alignment='center', format='{PAGE} of {NUMPAGES}')
        request = asposewordscloud.models.requests.InsertPageNumbersRequest(name=remoteFileName, page_number=requestPageNumber, folder=remoteDataFolder, dest_file_name=self.remote_test_out + '/' + remoteFileName)

        result = self.words_api.insert_page_numbers(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for deleting field.
    #
    def test_delete_field(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        fieldFolder = 'DocumentElements/Fields'
        localFileName = 'GetField.docx'
        remoteFileName = 'TestDeleteField.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, fieldFolder + '/' + localFileName), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldRequest(name=remoteFileName, index=0, node_path='sections/0/paragraphs/0', folder=remoteDataFolder)

        self.words_api.delete_field(request)


    #
    # Test for deleting field without node path.
    #
    def test_delete_field_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        fieldFolder = 'DocumentElements/Fields'
        localFileName = 'GetField.docx'
        remoteFileName = 'TestDeleteFieldWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, fieldFolder + '/' + localFileName), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        self.words_api.delete_field(request)


    #
    # Test for deleting paragraph fields.
    #
    def test_delete_paragraph_fields(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        localFileName = 'test_multi_pages.docx'
        remoteFileName = 'TestDeleteParagraphFields.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, 'Common/' + localFileName), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldsRequest(name=remoteFileName, node_path='paragraphs/0', folder=remoteDataFolder)

        self.words_api.delete_fields(request)


    #
    # Test for deleting paragraph fields without node path.
    #
    def test_delete_paragraph_fields_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        localFileName = 'test_multi_pages.docx'
        remoteFileName = 'TestDeleteParagraphFieldsWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, 'Common/' + localFileName), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldsRequest(name=remoteFileName, folder=remoteDataFolder)

        self.words_api.delete_fields(request)


    #
    # Test for deleting section fields.
    #
    def test_delete_section_fields(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        localFileName = 'test_multi_pages.docx'
        remoteFileName = 'TestDeleteSectionFields.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, 'Common/' + localFileName), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldsRequest(name=remoteFileName, node_path='sections/0', folder=remoteDataFolder)

        self.words_api.delete_fields(request)


    #
    # Test for deleting section fields without node path.
    #
    def test_delete_section_fields_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        localFileName = 'test_multi_pages.docx'
        remoteFileName = 'TestDeleteSectionFieldsWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, 'Common/' + localFileName), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldsRequest(name=remoteFileName, folder=remoteDataFolder)

        self.words_api.delete_fields(request)


    #
    # Test for deleting paragraph fields in section.
    #
    def test_delete_section_paragraph_fields(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        localFileName = 'test_multi_pages.docx'
        remoteFileName = 'TestDeleteSectionParagraphFields.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, 'Common/' + localFileName), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldsRequest(name=remoteFileName, node_path='sections/0/paragraphs/0', folder=remoteDataFolder)

        self.words_api.delete_fields(request)


    #
    # Test for deleting fields.
    #
    def test_delete_document_fields(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        localFileName = 'test_multi_pages.docx'
        remoteFileName = 'TestDeleteSectionParagraphFields.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, 'Common/' + localFileName), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldsRequest(name=remoteFileName, node_path='', folder=remoteDataFolder)

        self.words_api.delete_fields(request)


    #
    # Test for posting updated fields.
    #
    def test_update_document_fields(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        localFileName = 'test_multi_pages.docx'
        remoteFileName = 'TestUpdateDocumentFields.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, 'Common/' + localFileName), 'rb'))

        request = asposewordscloud.models.requests.UpdateFieldsRequest(name=remoteFileName, folder=remoteDataFolder)

        result = self.words_api.update_fields(request)
        self.assertIsNotNone(result, 'Error has occurred.')
