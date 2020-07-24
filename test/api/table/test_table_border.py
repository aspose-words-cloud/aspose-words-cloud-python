# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_table_border.py">
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
# Example of how to work with table borders.
#
class TestTableBorder(BaseTestContext):
    #
    # Test for getting borders.
    #
    def test_get_borders(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestGetBorders.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetBordersRequest(name=remoteFileName, node_path='tables/1/rows/0/cells/0', folder=remoteDataFolder)

        result = self.words_api.get_borders(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting border.
    #
    def test_get_border(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestGetBorder.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetBorderRequest(name=remoteFileName, border_type='left', node_path='tables/1/rows/0/cells/0', folder=remoteDataFolder)

        result = self.words_api.get_border(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for deleting borders.
    #
    def test_delete_borders(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestDeleteBorders.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteBordersRequest(name=remoteFileName, node_path='tables/1/rows/0/cells/0', folder=remoteDataFolder)

        result = self.words_api.delete_borders(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for deleting border.
    #
    def test_delete_border(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestDeleteBorder.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteBorderRequest(name=remoteFileName, border_type='left', node_path='tables/1/rows/0/cells/0', folder=remoteDataFolder)

        result = self.words_api.delete_border(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for updating border.
    #
    def test_update_border(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestUpdateBorder.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestBorderPropertiesColor = asposewordscloud.XmlColor(alpha=2)
        requestBorderProperties = asposewordscloud.Border(border_type='Left', color=requestBorderPropertiesColor, distance_from_text=6, line_style='DashDotStroker', line_width=2, shadow=True)
        request = asposewordscloud.models.requests.UpdateBorderRequest(name=remoteFileName, border_properties=requestBorderProperties, border_type='left', node_path='tables/1/rows/0/cells/0', folder=remoteDataFolder)

        result = self.words_api.update_border(request)
        self.assertIsNotNone(result, 'Error has occurred.')
