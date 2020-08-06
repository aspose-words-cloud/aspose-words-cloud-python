# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_table.py">
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
# Example of how to work wtih table.
#
class TestTable(BaseTestContext):
    #
    # Test for getting tables.
    #
    def test_get_tables(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestGetTables.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetTablesRequest(name=remoteFileName, node_path='', folder=remoteDataFolder)

        result = self.words_api.get_tables(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting tables without node path.
    #
    def test_get_tables_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestGetTablesWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetTablesRequest(name=remoteFileName, folder=remoteDataFolder)

        result = self.words_api.get_tables(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting table.
    #
    def test_get_table(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestGetTable.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetTableRequest(name=remoteFileName, index=1, node_path='', folder=remoteDataFolder)

        result = self.words_api.get_table(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting table without node path.
    #
    def test_get_table_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestGetTableWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetTableRequest(name=remoteFileName, index=1, folder=remoteDataFolder)

        result = self.words_api.get_table(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for deleting table.
    #
    def test_delete_table(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestDeleteTable.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteTableRequest(name=remoteFileName, index=1, node_path='', folder=remoteDataFolder)

        self.words_api.delete_table(request)


    #
    # Test for deleting table without node path.
    #
    def test_delete_table_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestDeleteTableWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteTableRequest(name=remoteFileName, index=1, folder=remoteDataFolder)

        self.words_api.delete_table(request)


    #
    # Test for adding table.
    #
    def test_insert_table(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestInsertTable.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestTable = asposewordscloud.TableInsert(columns_count=5, rows_count=4)
        request = asposewordscloud.models.requests.InsertTableRequest(name=remoteFileName, table=requestTable, node_path='', folder=remoteDataFolder)

        result = self.words_api.insert_table(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for adding table without node path.
    #
    def test_insert_table_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestInsertTableWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestTable = asposewordscloud.TableInsert(columns_count=5, rows_count=4)
        request = asposewordscloud.models.requests.InsertTableRequest(name=remoteFileName, table=requestTable, folder=remoteDataFolder)

        result = self.words_api.insert_table(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting document properties.
    #
    def test_get_table_properties(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestGetTableProperties.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetTablePropertiesRequest(name=remoteFileName, index=1, node_path='', folder=remoteDataFolder)

        result = self.words_api.get_table_properties(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting document properties without node path.
    #
    def test_get_table_properties_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestGetTablePropertiesWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetTablePropertiesRequest(name=remoteFileName, index=1, folder=remoteDataFolder)

        result = self.words_api.get_table_properties(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for updating table properties.
    #
    def test_update_table_properties(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestUpdateTableProperties.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestProperties = asposewordscloud.TableProperties(alignment='Right', allow_auto_fit=False, bidi=True, bottom_padding=1, cell_spacing=2, style_options='ColumnBands')
        request = asposewordscloud.models.requests.UpdateTablePropertiesRequest(name=remoteFileName, properties=requestProperties, index=1, node_path='', folder=remoteDataFolder)

        result = self.words_api.update_table_properties(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for updating table properties without node path.
    #
    def test_update_table_properties_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestUpdateTablePropertiesWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestProperties = asposewordscloud.TableProperties(alignment='Right', allow_auto_fit=False, bidi=True, bottom_padding=1, cell_spacing=2, style_options='ColumnBands')
        request = asposewordscloud.models.requests.UpdateTablePropertiesRequest(name=remoteFileName, properties=requestProperties, index=1, folder=remoteDataFolder)

        result = self.words_api.update_table_properties(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting table row.
    #
    def test_get_table_row(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestGetTableRow.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetTableRowRequest(name=remoteFileName, table_path='tables/1', index=0, folder=remoteDataFolder)

        result = self.words_api.get_table_row(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for deleting table row.
    #
    def test_delete_table_row(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestDeleteTableRow.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteTableRowRequest(name=remoteFileName, table_path='tables/1', index=0, folder=remoteDataFolder)

        self.words_api.delete_table_row(request)


    #
    # Test for adding row.
    #
    def test_insert_table_row(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestInsertTableRow.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestRow = asposewordscloud.TableRowInsert(columns_count=5)
        request = asposewordscloud.models.requests.InsertTableRowRequest(name=remoteFileName, row=requestRow, table_path='sections/0/tables/2', folder=remoteDataFolder)

        result = self.words_api.insert_table_row(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting row format.
    #
    def test_get_table_row_format(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestGetTableRowFormat.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetTableRowFormatRequest(name=remoteFileName, table_path='sections/0/tables/2', index=0, folder=remoteDataFolder)

        result = self.words_api.get_table_row_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test updating row format.
    #
    def test_update_table_row_format(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestUpdateTableRowFormat.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestFormat = asposewordscloud.TableRowFormat(allow_break_across_pages=True, heading_format=True, height=10, height_rule='Auto')
        request = asposewordscloud.models.requests.UpdateTableRowFormatRequest(name=remoteFileName, format=requestFormat, table_path='sections/0/tables/2', index=0, folder=remoteDataFolder)

        result = self.words_api.update_table_row_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting table cell.
    #
    def test_get_table_cell(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestGetTableCell.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetTableCellRequest(name=remoteFileName, table_row_path='sections/0/tables/2/rows/0', index=0, folder=remoteDataFolder)

        result = self.words_api.get_table_cell(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for deleting cell.
    #
    def test_delete_table_cell(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestDeleteTableCell.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteTableCellRequest(name=remoteFileName, table_row_path='sections/0/tables/2/rows/0', index=0, folder=remoteDataFolder)

        self.words_api.delete_table_cell(request)


    #
    # Test for adding cell.
    #
    def test_insert_table_cell(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestInsertTableCell.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestCell = asposewordscloud.TableCellInsert()
        request = asposewordscloud.models.requests.InsertTableCellRequest(name=remoteFileName, cell=requestCell, table_row_path='sections/0/tables/2/rows/0', folder=remoteDataFolder)

        result = self.words_api.insert_table_cell(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting cell format.
    #
    def test_get_table_cell_format(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestGetTableCellFormat.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetTableCellFormatRequest(name=remoteFileName, table_row_path='sections/0/tables/2/rows/0', index=0, folder=remoteDataFolder)

        result = self.words_api.get_table_cell_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for updating cell format.
    #
    def test_update_table_cell_format(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestUpdateTableCellFormat.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestFormat = asposewordscloud.TableCellFormat(bottom_padding=5, fit_text=True, horizontal_merge='First', wrap_text=True)
        request = asposewordscloud.models.requests.UpdateTableCellFormatRequest(name=remoteFileName, format=requestFormat, table_row_path='sections/0/tables/2/rows/0', index=0, folder=remoteDataFolder)

        result = self.words_api.update_table_cell_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for table rendering.
    #
    def test_render_table(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestRenderTable.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.RenderTableRequest(name=remoteFileName, format='png', index=0, node_path='', folder=remoteDataFolder)

        result = self.words_api.render_table(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for table rendering without node path.
    #
    def test_render_table_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Tables'
        localFile = 'DocumentElements/Tables/TablesGet.docx'
        remoteFileName = 'TestRenderTableWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.RenderTableRequest(name=remoteFileName, format='png', index=0, folder=remoteDataFolder)

        result = self.words_api.render_table(request)
        self.assertIsNotNone(result, 'Error has occurred.')
