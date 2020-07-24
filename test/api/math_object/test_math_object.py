# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_math_object.py">
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
# Example of how to work with MathObjects.
#
class TestMathObject(BaseTestContext):
    #
    # Test for getting mathObjects.
    #
    def test_get_office_math_objects(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/MathObjects'
        localFile = 'DocumentElements/MathObjects/MathObjects.docx'
        remoteFileName = 'TestGetOfficeMathObjects.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetOfficeMathObjectsRequest(name=remoteFileName, node_path='', folder=remoteDataFolder)

        result = self.words_api.get_office_math_objects(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting mathObjects without node path.
    #
    def test_get_office_math_objects_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/MathObjects'
        localFile = 'DocumentElements/MathObjects/MathObjects.docx'
        remoteFileName = 'TestGetOfficeMathObjectsWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetOfficeMathObjectsRequest(name=remoteFileName, folder=remoteDataFolder)

        result = self.words_api.get_office_math_objects(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting mathObject.
    #
    def test_get_office_math_object(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/MathObjects'
        localFile = 'DocumentElements/MathObjects/MathObjects.docx'
        remoteFileName = 'TestGetOfficeMathObject.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetOfficeMathObjectRequest(name=remoteFileName, index=0, node_path='', folder=remoteDataFolder)

        result = self.words_api.get_office_math_object(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting mathObject without node path.
    #
    def test_get_office_math_object_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/MathObjects'
        localFile = 'DocumentElements/MathObjects/MathObjects.docx'
        remoteFileName = 'TestGetOfficeMathObjectWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetOfficeMathObjectRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        result = self.words_api.get_office_math_object(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for rendering mathObject.
    #
    def test_render_math_object(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/MathObjects'
        localFile = 'DocumentElements/MathObjects/MathObjects.docx'
        remoteFileName = 'TestRenderMathObject.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.RenderMathObjectRequest(name=remoteFileName, format='png', index=0, node_path='', folder=remoteDataFolder)

        result = self.words_api.render_math_object(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for rendering mathObject without node path.
    #
    def test_render_math_object_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/MathObjects'
        localFile = 'DocumentElements/MathObjects/MathObjects.docx'
        remoteFileName = 'TestRenderMathObjectWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.RenderMathObjectRequest(name=remoteFileName, format='png', index=0, folder=remoteDataFolder)

        result = self.words_api.render_math_object(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for deleting mathObject.
    #
    def test_delete_office_math_object(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/MathObjects'
        localFile = 'DocumentElements/MathObjects/MathObjects.docx'
        remoteFileName = 'TestDeleteOfficeMathObject.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteOfficeMathObjectRequest(name=remoteFileName, index=0, node_path='', folder=remoteDataFolder)

        self.words_api.delete_office_math_object(request)


    #
    # Test for deleting mathObject without node path.
    #
    def test_delete_office_math_object_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/MathObjects'
        localFile = 'DocumentElements/MathObjects/MathObjects.docx'
        remoteFileName = 'TestDeleteOfficeMathObjectWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteOfficeMathObjectRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        self.words_api.delete_office_math_object(request)

