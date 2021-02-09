# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_field.py">
#   Copyright (c) 2021 Aspose.Words for Cloud
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

        request = asposewordscloud.models.requests.GetFieldsRequest(name = remoteFileName, node_path = 'sections/0', folder = remoteDataFolder)

        result = self.words_api.get_fields(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.fields, 'Validate GetFields response')
        self.assertIsNotNone(result.fields.list, 'Validate GetFields response')
        self.assertEqual(1, len(result.fields.list))
        self.assertEqual('1', result.fields.list[0].result)

    #
    # Test for getting fields online.
    #
    def test_get_fields_online(self):
        fieldFolder = 'DocumentElements/Fields'

        request = asposewordscloud.models.requests.GetFieldsOnlineRequest(document = open(os.path.join(self.local_test_folder, fieldFolder + '/GetField.docx'), 'rb'), node_path = 'sections/0')

        result = self.words_api.get_fields_online(request)
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

        request = asposewordscloud.models.requests.GetFieldsRequest(name = remoteFileName, folder = remoteDataFolder)

        result = self.words_api.get_fields(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.fields, 'Validate GetFieldsWithoutNodePath response')
        self.assertIsNotNone(result.fields.list, 'Validate GetFieldsWithoutNodePath response')
        self.assertEqual(1, len(result.fields.list))
        self.assertEqual('1', result.fields.list[0].result)

    #
    # Test for getting field by index.
    #
    def test_get_field(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        fieldFolder = 'DocumentElements/Fields'
        localFileName = 'GetField.docx'
        remoteFileName = 'TestGetField.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, fieldFolder + '/' + localFileName), 'rb'))

        request = asposewordscloud.models.requests.GetFieldRequest(name = remoteFileName, index = 0, node_path = 'sections/0/paragraphs/0', folder = remoteDataFolder)

        result = self.words_api.get_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.field, 'Validate GetField response')
        self.assertEqual('1', result.field.result)

    #
    # Test for getting field by index online.
    #
    def test_get_field_online(self):
        fieldFolder = 'DocumentElements/Fields'

        request = asposewordscloud.models.requests.GetFieldOnlineRequest(document = open(os.path.join(self.local_test_folder, fieldFolder + '/GetField.docx'), 'rb'), index = 0, node_path = 'sections/0/paragraphs/0')

        result = self.words_api.get_field_online(request)
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

        request = asposewordscloud.models.requests.GetFieldRequest(name = remoteFileName, index = 0, folder = remoteDataFolder)

        result = self.words_api.get_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.field, 'Validate GetFieldWithoutNodePath response')
        self.assertEqual('1', result.field.result)

    #
    # Test for putting field.
    #
    def test_insert_field(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        textFolder = 'DocumentElements/Text'
        localFileName = 'SampleWordDocument.docx'
        remoteFileName = 'TestInsertField.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, textFolder + '/' + localFileName), 'rb'))

        requestField = asposewordscloud.FieldInsert(field_code = '{ NUMPAGES }')
        request = asposewordscloud.models.requests.InsertFieldRequest(name = remoteFileName, field = requestField, node_path = 'sections/0/paragraphs/0', folder = remoteDataFolder)

        result = self.words_api.insert_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.field, 'Validate InsertField response')
        self.assertEqual('{ NUMPAGES }', result.field.field_code)
        self.assertEqual('0.0.0.1', result.field.node_id)

    #
    # Test for putting field online.
    #
    def test_insert_field_online(self):
        fieldFolder = 'DocumentElements/Fields'

        requestField = asposewordscloud.FieldInsert(field_code = '{ NUMPAGES }')
        request = asposewordscloud.models.requests.InsertFieldOnlineRequest(document = open(os.path.join(self.local_test_folder, fieldFolder + '/GetField.docx'), 'rb'), field = requestField, node_path = 'sections/0/paragraphs/0')

        result = self.words_api.insert_field_online(request)
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

        requestField = asposewordscloud.FieldInsert(field_code = '{ NUMPAGES }')
        request = asposewordscloud.models.requests.InsertFieldRequest(name = remoteFileName, field = requestField, folder = remoteDataFolder)

        result = self.words_api.insert_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.field, 'Validate InsertFieldWithoutNodePath response')
        self.assertEqual('{ NUMPAGES }', result.field.field_code)
        self.assertEqual('5.0.22.0', result.field.node_id)

    #
    # Test for posting field.
    #
    def test_update_field(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        fieldFolder = 'DocumentElements/Fields'
        localFileName = 'GetField.docx'
        remoteFileName = 'TestUpdateField.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, fieldFolder + '/' + localFileName), 'rb'))

        requestField = asposewordscloud.FieldUpdate(field_code = '{ NUMPAGES }')
        request = asposewordscloud.models.requests.UpdateFieldRequest(name = remoteFileName, index = 0, field = requestField, node_path = 'sections/0/paragraphs/0', folder = remoteDataFolder)

        result = self.words_api.update_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.field, 'Validate UpdateField response')
        self.assertEqual('{ NUMPAGES }', result.field.field_code)
        self.assertEqual('0.0.0.0', result.field.node_id)

    #
    # Test for posting field online.
    #
    def test_update_field_online(self):
        fieldFolder = 'DocumentElements/Fields'

        requestField = asposewordscloud.FieldUpdate(field_code = '{ NUMPAGES }')
        request = asposewordscloud.models.requests.UpdateFieldOnlineRequest(document = open(os.path.join(self.local_test_folder, fieldFolder + '/GetField.docx'), 'rb'), index = 0, field = requestField, node_path = 'sections/0/paragraphs/0')

        result = self.words_api.update_field_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for inserting page numbers field.
    #
    def test_insert_page_numbers(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        localFileName = 'test_multi_pages.docx'
        remoteFileName = 'TestInsertPageNumbers.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, 'Common/' + localFileName), 'rb'))

        requestPageNumber = asposewordscloud.PageNumber(alignment = 'center', format = '{PAGE} of {NUMPAGES}')
        request = asposewordscloud.models.requests.InsertPageNumbersRequest(name = remoteFileName, page_number = requestPageNumber, folder = remoteDataFolder, dest_file_name = self.remote_test_out + '/' + remoteFileName)

        result = self.words_api.insert_page_numbers(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document, 'Validate InsertPageNumbers response')
        self.assertEqual('TestInsertPageNumbers.docx', result.document.file_name)

    #
    # Test for inserting page numbers field online.
    #
    def test_insert_page_numbers_online(self):
        localFileName = 'test_multi_pages.docx'

        requestPageNumber = asposewordscloud.PageNumber(alignment = 'center', format = '{PAGE} of {NUMPAGES}')
        request = asposewordscloud.models.requests.InsertPageNumbersOnlineRequest(document = open(os.path.join(self.local_test_folder, 'Common/' + localFileName), 'rb'), page_number = requestPageNumber)

        result = self.words_api.insert_page_numbers_online(request)
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

        request = asposewordscloud.models.requests.DeleteFieldRequest(name = remoteFileName, index = 0, node_path = 'sections/0/paragraphs/0', folder = remoteDataFolder)

        self.words_api.delete_field(request)


    #
    # Test for deleting field online.
    #
    def test_delete_field_online(self):
        fieldFolder = 'DocumentElements/Fields'

        request = asposewordscloud.models.requests.DeleteFieldOnlineRequest(document = open(os.path.join(self.local_test_folder, fieldFolder + '/GetField.docx'), 'rb'), index = 0, node_path = 'sections/0/paragraphs/0')

        result = self.words_api.delete_field_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting field without node path.
    #
    def test_delete_field_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        fieldFolder = 'DocumentElements/Fields'
        localFileName = 'GetField.docx'
        remoteFileName = 'TestDeleteFieldWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, fieldFolder + '/' + localFileName), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldRequest(name = remoteFileName, index = 0, folder = remoteDataFolder)

        self.words_api.delete_field(request)


    #
    # Test for deleting paragraph fields.
    #
    def test_delete_paragraph_fields(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        localFileName = 'test_multi_pages.docx'
        remoteFileName = 'TestDeleteParagraphFields.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, 'Common/' + localFileName), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldsRequest(name = remoteFileName, node_path = 'paragraphs/0', folder = remoteDataFolder)

        self.words_api.delete_fields(request)


    #
    # Test for deleting paragraph fields without node path.
    #
    def test_delete_paragraph_fields_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        localFileName = 'test_multi_pages.docx'
        remoteFileName = 'TestDeleteParagraphFieldsWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, 'Common/' + localFileName), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldsRequest(name = remoteFileName, folder = remoteDataFolder)

        self.words_api.delete_fields(request)


    #
    # Test for deleting section fields.
    #
    def test_delete_section_fields(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        localFileName = 'test_multi_pages.docx'
        remoteFileName = 'TestDeleteSectionFields.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, 'Common/' + localFileName), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldsRequest(name = remoteFileName, node_path = 'sections/0', folder = remoteDataFolder)

        self.words_api.delete_fields(request)


    #
    # Test for deleting section fields without node path.
    #
    def test_delete_section_fields_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        localFileName = 'test_multi_pages.docx'
        remoteFileName = 'TestDeleteSectionFieldsWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, 'Common/' + localFileName), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldsRequest(name = remoteFileName, folder = remoteDataFolder)

        self.words_api.delete_fields(request)


    #
    # Test for deleting paragraph fields in section.
    #
    def test_delete_section_paragraph_fields(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        localFileName = 'test_multi_pages.docx'
        remoteFileName = 'TestDeleteSectionParagraphFields.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, 'Common/' + localFileName), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldsRequest(name = remoteFileName, node_path = 'sections/0/paragraphs/0', folder = remoteDataFolder)

        self.words_api.delete_fields(request)


    #
    # Test for deleting fields.
    #
    def test_delete_document_fields(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        localFileName = 'test_multi_pages.docx'
        remoteFileName = 'TestDeleteSectionParagraphFields.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, 'Common/' + localFileName), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldsRequest(name = remoteFileName, node_path = '', folder = remoteDataFolder)

        self.words_api.delete_fields(request)


    #
    # Test for deleting fields online.
    #
    def test_delete_document_fields_online(self):
        localFileName = 'Common/test_multi_pages.docx'

        request = asposewordscloud.models.requests.DeleteFieldsOnlineRequest(document = open(os.path.join(self.local_test_folder, localFileName), 'rb'), node_path = '')

        result = self.words_api.delete_fields_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for posting updated fields.
    #
    def test_update_document_fields(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Fields'
        localFileName = 'test_multi_pages.docx'
        remoteFileName = 'TestUpdateDocumentFields.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, 'Common/' + localFileName), 'rb'))

        request = asposewordscloud.models.requests.UpdateFieldsRequest(name = remoteFileName, folder = remoteDataFolder)

        result = self.words_api.update_fields(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document, 'Validate UpdateDocumentFields response')
        self.assertEqual('TestUpdateDocumentFields.docx', result.document.file_name)

    #
    # Test for posting updated fields online.
    #
    def test_update_document_fields_online(self):
        localFile = 'Common/test_multi_pages.docx'

        request = asposewordscloud.models.requests.UpdateFieldsOnlineRequest(document = open(os.path.join(self.local_test_folder, localFile), 'rb'))

        result = self.words_api.update_fields_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

