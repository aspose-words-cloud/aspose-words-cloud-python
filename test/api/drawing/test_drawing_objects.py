# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_drawing_objects.py">
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
# Example of how to get drawing objects.
#
class TestDrawingObjects(BaseTestContext):
    #
    # Test for getting drawing objects from document.
    #
    def test_get_document_drawing_objects(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentDrawingObjects.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentDrawingObjectsRequest(name=remoteFileName, node_path='sections/0', folder=remoteDataFolder)

        result = self.words_api.get_document_drawing_objects(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting drawing objects from document without node path.
    #
    def test_get_document_drawing_objects_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentDrawingObjectsWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentDrawingObjectsRequest(name=remoteFileName, folder=remoteDataFolder)

        result = self.words_api.get_document_drawing_objects(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting drawing object by specified index.
    #
    def test_get_document_drawing_object_by_index(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentDrawingObjectByIndex.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentDrawingObjectByIndexRequest(name=remoteFileName, index=0, node_path='sections/0', folder=remoteDataFolder)

        result = self.words_api.get_document_drawing_object_by_index(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting drawing object by specified index without node path.
    #
    def test_get_document_drawing_object_by_index_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentDrawingObjectByIndexWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentDrawingObjectByIndexRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        result = self.words_api.get_document_drawing_object_by_index(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting drawing object by specified index and format.
    #
    def test_render_drawing_object(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentDrawingObjectByIndexWithFormat.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.RenderDrawingObjectRequest(name=remoteFileName, format='png', index=0, node_path='sections/0', folder=remoteDataFolder)

        result = self.words_api.render_drawing_object(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting drawing object by specified index and format without node path.
    #
    def test_render_drawing_object_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentDrawingObjectByIndexWithFormatWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.RenderDrawingObjectRequest(name=remoteFileName, format='png', index=0, folder=remoteDataFolder)

        result = self.words_api.render_drawing_object(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for reading drawing object's image data.
    #
    def test_get_document_drawing_object_image_data(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentDrawingObjectImageData.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentDrawingObjectImageDataRequest(name=remoteFileName, index=0, node_path='sections/0', folder=remoteDataFolder)

        result = self.words_api.get_document_drawing_object_image_data(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for reading drawing object's image data without node path.
    #
    def test_get_document_drawing_object_image_data_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentDrawingObjectImageDataWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentDrawingObjectImageDataRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        result = self.words_api.get_document_drawing_object_image_data(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting drawing object OLE data.
    #
    def test_get_document_drawing_object_ole_data(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        localDrawingFile = 'DocumentElements/DrawingObjects/sample_EmbeddedOLE.docx'
        remoteFileName = 'TestGetDocumentDrawingObjectOleData.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localDrawingFile), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentDrawingObjectOleDataRequest(name=remoteFileName, index=0, node_path='sections/0', folder=remoteDataFolder)

        result = self.words_api.get_document_drawing_object_ole_data(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting drawing object OLE data without node path.
    #
    def test_get_document_drawing_object_ole_data_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        localDrawingFile = 'DocumentElements/DrawingObjects/sample_EmbeddedOLE.docx'
        remoteFileName = 'TestGetDocumentDrawingObjectOleDataWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localDrawingFile), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentDrawingObjectOleDataRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        result = self.words_api.get_document_drawing_object_ole_data(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for adding drawing object.
    #
    def test_insert_drawing_object(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestInsetDrawingObject.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestDrawingObject = asposewordscloud.DrawingObjectInsert(height=0, left=0, top=0, width=0, relative_horizontal_position='Margin', relative_vertical_position='Margin', wrap_type='Inline')
        request = asposewordscloud.models.requests.InsertDrawingObjectRequest(name=remoteFileName, drawing_object=requestDrawingObject, image_file=open(os.path.join(self.local_test_folder, 'Common/aspose-cloud.png'), 'rb'), node_path='', folder=remoteDataFolder)

        result = self.words_api.insert_drawing_object(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for adding drawing object without node path.
    #
    def test_insert_drawing_object_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestInsetDrawingObjectWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestDrawingObject = asposewordscloud.DrawingObjectInsert(height=0, left=0, top=0, width=0, relative_horizontal_position='Margin', relative_vertical_position='Margin', wrap_type='Inline')
        request = asposewordscloud.models.requests.InsertDrawingObjectRequest(name=remoteFileName, drawing_object=requestDrawingObject, image_file=open(os.path.join(self.local_test_folder, 'Common/aspose-cloud.png'), 'rb'), folder=remoteDataFolder)

        result = self.words_api.insert_drawing_object(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for deleting drawing object.
    #
    def test_delete_drawing_object(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestDeleteDrawingObject.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteDrawingObjectRequest(name=remoteFileName, index=0, node_path='', folder=remoteDataFolder)

        self.words_api.delete_drawing_object(request)


    #
    # Test for deleting drawing object without node path.
    #
    def test_delete_drawing_object_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestDeleteDrawingObjectWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteDrawingObjectRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        self.words_api.delete_drawing_object(request)


    #
    # Test for updating drawing object.
    #
    def test_update_drawing_object(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestUpdateDrawingObject.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestDrawingObject = asposewordscloud.DrawingObjectUpdate(left=0)
        request = asposewordscloud.models.requests.UpdateDrawingObjectRequest(name=remoteFileName, drawing_object=requestDrawingObject, image_file=open(os.path.join(self.local_test_folder, 'Common/aspose-cloud.png'), 'rb'), index=0, node_path='', folder=remoteDataFolder)

        result = self.words_api.update_drawing_object(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for updating drawing object without node path.
    #
    def test_update_drawing_object_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestUpdateDrawingObjectWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestDrawingObject = asposewordscloud.DrawingObjectUpdate(left=0)
        request = asposewordscloud.models.requests.UpdateDrawingObjectRequest(name=remoteFileName, drawing_object=requestDrawingObject, image_file=open(os.path.join(self.local_test_folder, 'Common/aspose-cloud.png'), 'rb'), index=0, folder=remoteDataFolder)

        result = self.words_api.update_drawing_object(request)
        self.assertIsNotNone(result, 'Error has occurred.')
