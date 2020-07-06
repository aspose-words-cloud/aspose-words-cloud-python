# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_watermark.py">
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
# Example of how to work with watermarks.
#
class TestWatermark(BaseTestContext):
    #
    # Test for adding watermark image.
    #
    def test_insert_watermark_image(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentActions/Watermark'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestInsertWatermarkImage.docx'
        remoteImagePath = remoteDataFolder + '/TestInsertWatermarkImage.png'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))
        self.upload_file(remoteImagePath, open(os.path.join(self.local_test_folder, 'Common/aspose-cloud.png'), 'rb'))

        request = asposewordscloud.models.requests.InsertWatermarkImageRequest(name=remoteFileName, image_file=None, folder=remoteDataFolder, dest_file_name=self.remote_test_out + '/' + remoteFileName, image=remoteImagePath)

        result = self.words_api.insert_watermark_image(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for adding watermark text.
    #
    def test_insert_watermark_text(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentActions/Watermark'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestInsertWatermarkText.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestWatermarkText = asposewordscloud.WatermarkText(text='This is the text', rotation_angle=90)
        request = asposewordscloud.models.requests.InsertWatermarkTextRequest(name=remoteFileName, watermark_text=requestWatermarkText, folder=remoteDataFolder, dest_file_name=self.remote_test_out + '/' + remoteFileName)

        result = self.words_api.insert_watermark_text(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for deleting watermark.
    #
    def test_delete_watermark(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentActions/Watermark'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestDeleteWatermark.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteWatermarkRequest(name=remoteFileName, folder=remoteDataFolder, dest_file_name=self.remote_test_out + '/' + remoteFileName)

        result = self.words_api.delete_watermark(request)
        self.assertIsNotNone(result, 'Error has occurred.')
