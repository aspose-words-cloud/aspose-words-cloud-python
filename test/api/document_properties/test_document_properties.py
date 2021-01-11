# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_document_properties.py">
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
# Example of how to get document properties.
#
class TestDocumentProperties(BaseTestContext):
    #
    # Test for getting document properties.
    #
    def test_get_document_properties(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DocumentProperties'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentProperties.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentPropertiesRequest(name=remoteFileName, folder=remoteDataFolder)

        result = self.words_api.get_document_properties(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document_properties, 'Validate GetDocumentProperties response')
        self.assertIsNotNone(result.document_properties.list, 'Validate GetDocumentProperties response')
        self.assertEqual(24, len(result.document_properties.list))
        self.assertIsNotNone(result.document_properties.list[0], 'Validate GetDocumentProperties response')
        self.assertEqual('Author', result.document_properties.list[0].name)
        self.assertEqual('', result.document_properties.list[0].value)

    #
    # Test for getting document properties online.
    #
    def test_get_document_properties_online(self):
        localFile = 'Common/test_multi_pages.docx'

        request = asposewordscloud.models.requests.GetDocumentPropertiesOnlineRequest(document=open(os.path.join(self.local_test_folder, localFile), 'rb'))

        result = self.words_api.get_document_properties_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # A test for GetDocumentProperty.
    #
    def test_get_document_property(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DocumentProperties'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentProperty.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentPropertyRequest(name=remoteFileName, property_name='Author', folder=remoteDataFolder)

        result = self.words_api.get_document_property(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document_property, 'Validate GetDocumentProperty response')
        self.assertEqual('Author', result.document_property.name)
        self.assertEqual('', result.document_property.value)

    #
    # A test for GetDocumentProperty online.
    #
    def test_get_document_property_online(self):
        localFile = 'Common/test_multi_pages.docx'

        request = asposewordscloud.models.requests.GetDocumentPropertyOnlineRequest(document=open(os.path.join(self.local_test_folder, localFile), 'rb'), property_name='Author')

        result = self.words_api.get_document_property_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting document property.
    #
    def test_delete_document_property(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DocumentProperties'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestDeleteDocumentProperty.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteDocumentPropertyRequest(name=remoteFileName, property_name='testProp', folder=remoteDataFolder, dest_file_name=self.remote_test_out + '/' + remoteFileName)

        self.words_api.delete_document_property(request)


    #
    # Test for deleting document property online.
    #
    def test_delete_document_property_online(self):
        localFile = 'Common/test_multi_pages.docx'

        request = asposewordscloud.models.requests.DeleteDocumentPropertyOnlineRequest(document=open(os.path.join(self.local_test_folder, localFile), 'rb'), property_name='testProp')

        result = self.words_api.delete_document_property_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating document property.
    #
    def test_update_document_property(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DocumentProperties'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestUpdateDocumentProperty.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestProperty = asposewordscloud.DocumentPropertyCreateOrUpdate(value='Imran Anwar')
        request = asposewordscloud.models.requests.CreateOrUpdateDocumentPropertyRequest(name=remoteFileName, property_name='AsposeAuthor', _property=requestProperty, folder=remoteDataFolder, dest_file_name=self.remote_test_out + '/' + remoteFileName)

        result = self.words_api.create_or_update_document_property(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document_property, 'Validate UpdateDocumentProperty response')
        self.assertEqual('AsposeAuthor', result.document_property.name)
        self.assertEqual('Imran Anwar', result.document_property.value)

    #
    # Test for updating document property online.
    #
    def test_update_document_property_online(self):
        localFile = 'Common/test_multi_pages.docx'

        requestProperty = asposewordscloud.DocumentPropertyCreateOrUpdate(value='Imran Anwar')
        request = asposewordscloud.models.requests.CreateOrUpdateDocumentPropertyOnlineRequest(document=open(os.path.join(self.local_test_folder, localFile), 'rb'), property_name='AsposeAuthor', _property=requestProperty)

        result = self.words_api.create_or_update_document_property_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

