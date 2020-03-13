#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_math_objects.py">
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


class TestMathObjects(BaseTestContext):
    test_folder = 'DocumentElements/MathObjects'

    #
    # Test for removing math object from document
    #
    def test_delete_office_math_object(self):
        filename = 'MathObjects.docx'
        remote_name = 'TestDeleteOfficeMathObject.docx'
        index = 0

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.DeleteOfficeMathObjectRequest(remote_name, '', index,
                                                                               os.path.join(
                                                                                   self.remote_test_folder,
                                                                                   self.test_folder))
        result = self.words_api.delete_office_math_object(request)
        self.assertIsNotNone(result, 'Error has occurred while delete math object')

    #
    # Test for removing math object from document wihtout node path
    #
    def test_delete_office_math_object_without_node_path(self):
        filename = 'MathObjects.docx'
        remote_name = 'TestDeleteOfficeMathObjectWithoutNodePath.docx'
        index = 0

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.DeleteOfficeMathObjectWithoutNodePathRequest(remote_name, index,
                                                                               os.path.join(
                                                                                   self.remote_test_folder,
                                                                                   self.test_folder))
        result = self.words_api.delete_office_math_object_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while delete math object')

    #
    # Test for getting math object from document
    #
    def test_get_office_math_object(self):
        filename = 'MathObjects.docx'
        remote_name = 'TestGetOfficeMathObject.docx'
        index = 0

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetOfficeMathObjectRequest(remote_name, '', index,  
                                                                            os.path.join(
                                                                                self.remote_test_folder,
                                                                                self.test_folder))
        result = self.words_api.get_office_math_object(request)
        self.assertIsNotNone(result, 'Error has occurred while get math object')

    #
    # Test for getting math object from document without node path
    #
    def test_get_office_math_object_without_node_path(self):
        filename = 'MathObjects.docx'
        remote_name = 'TestGetOfficeMathObjectWithoutNodePath.docx'
        index = 0

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetOfficeMathObjectWithoutNodePathRequest(remote_name, index,
                                                                            os.path.join(
                                                                                self.remote_test_folder,
                                                                                self.test_folder))
        result = self.words_api.get_office_math_object_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while get math object')

    #
    # Test for getting math objects from document
    #
    def test_get_office_math_objects(self):
        filename = 'MathObjects.docx'
        remote_name = 'TestGetOfficeMathObjects.docx'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetOfficeMathObjectsRequest(remote_name, '',
                                                                             os.path.join(
                                                                                 self.remote_test_folder,
                                                                                 self.test_folder))
        result = self.words_api.get_office_math_objects(request)
        self.assertIsNotNone(result, 'Error has occurred while get math objects')

    #
    # Test for getting math objects from document without node path
    #
    def test_get_office_math_objects_without_node_path(self):
        filename = 'MathObjects.docx'
        remote_name = 'TestGetOfficeMathObjectsWithoutNodePath.docx'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetOfficeMathObjectsWithoutNodePathRequest(remote_name,
                                                                             os.path.join(
                                                                                 self.remote_test_folder,
                                                                                 self.test_folder))
        result = self.words_api.get_office_math_objects_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while get math objects')

    #
    # Test for getting math object from document
    #
    def test_render_math_object(self):
        filename = 'MathObjects.docx'
        remote_name = 'TestRenderMathObject.docx'
        index = 0
        format = 'png'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.RenderMathObjectRequest(remote_name, format, '', index, 
                                                                         os.path.join(
                                                                             self.remote_test_folder,
                                                                             self.test_folder))
        result = self.words_api.render_math_object(request)
        self.assertIsNotNone(result, 'Error has occurred while render math objects')

    #
    # Test for getting math object from document without node paht
    #
    def test_render_math_object_without_node_path(self):
        filename = 'MathObjects.docx'
        remote_name = 'TestRenderMathObjectWithoutNodePath.docx'
        index = 0
        format = 'png'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.RenderMathObjectWithoutNodePathRequest(remote_name, format, index,
                                                                         os.path.join(
                                                                             self.remote_test_folder,
                                                                             self.test_folder))
        result = self.words_api.render_math_object_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while render math objects')
