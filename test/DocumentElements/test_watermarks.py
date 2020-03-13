#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_watermarks.py">
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


class TestWatermarks(BaseTestContext):
    test_folder = 'DocumentElements/Watermarks'

    #
    #  Test for removing watermark
    #
    def test_delete_watermark(self):
        filename = 'test_doc.docx'
        remote_name = 'TestDeleteDocumentWatermark.docx'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.DeleteWatermarkRequest(remote_name,
                                                                                os.path.join(
                                                                                    self.remote_test_folder,
                                                                                    self.test_folder))
        result = self.words_api.delete_watermark(request)
        self.assertIsNotNone(result, 'Error has occurred while delete document watermark')

    #
    #  Test for inserting watermark image
    #
    def test_insert_watermark_image(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPostInsertDocumentWatermarkImage.docx'
        rotation_angle = 0
        dest_name = os.path.join(self.remote_test_out, remote_name)
        image = open(os.path.join(self.local_common_folder, 'aspose-cloud.png'), 'rb')

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.InsertWatermarkImageRequest(remote_name, image,
                                                                                         os.path.join(
                                                                                             self.remote_test_folder,
                                                                                             self.test_folder),
                                                                                         dest_file_name=dest_name,
                                                                                         rotation_angle=rotation_angle)
        result = self.words_api.insert_watermark_image(request)
        self.assertIsNotNone(result, 'Error has occurred while post insert document watermark')

    #
    #  Test for inserting watermark text
    #
    def test_insert_watermark_text(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPostInsertDocumentWatermarkText.docx'
        dest_name = os.path.join(self.remote_test_out, remote_name)
        body = asposewordscloud.WatermarkText('This is the text', 90)

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.InsertWatermarkTextRequest(remote_name, body,
                                                                                        os.path.join(
                                                                                            self.remote_test_folder,
                                                                                            self.test_folder),
                                                                                        dest_file_name=dest_name)
        result = self.words_api.insert_watermark_text(request)
        self.assertIsNotNone(result, 'Error has occurred while post insert document watermark text')
