#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_tables.py">
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


class TestTables(BaseTestContext):
    test_folder = 'DocumentElements/Tables'

    #
    # Test for removing table
    #
    def test_delete_table(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestDeleteTable.docx'
        index = 1

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.DeleteTableRequest(remote_name, '', index,
                                                                    os.path.join(
                                                                        self.remote_test_folder,
                                                                        self.test_folder))
        result = self.words_api.delete_table(request)
        self.assertIsNotNone(result, 'Error has occurred while delete table')

    #
    # Test for removing table without node path
    #
    def test_delete_table_without_node_path(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestDeleteTableWithoutNodePath.docx'
        index = 1

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.DeleteTableWithoutNodePathRequest(remote_name, index, 
                                                                    os.path.join(
                                                                        self.remote_test_folder,
                                                                        self.test_folder))
        result = self.words_api.delete_table_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while delete table')

    #
    # Test for removing table cell
    #
    def test_delete_table_cell(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestDeleteTableCell.docx'
        index = 0
        source_path = 'sections/0/tables/2/rows/0'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.DeleteTableCellRequest(remote_name, source_path, index,
                                                                          os.path.join(
                                                                              self.remote_test_folder,
                                                                              self.test_folder))
        result = self.words_api.delete_table_cell(request)
        self.assertIsNotNone(result, 'Error has occurred while delete table cell')

    #
    # Test for removing table row
    #
    def test_delete_table_row(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestDeleteTableRow.docx'
        index = 0
        source_path = 'tables/1'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.DeleteTableRowRequest(remote_name, source_path, index,
                                                                         os.path.join(
                                                                             self.remote_test_folder,
                                                                             self.test_folder))
        result = self.words_api.delete_table_row(request)
        self.assertIsNotNone(result, 'Error has occurred while delete table row')

    #
    # Test for getting table border
    #
    def test_get_border(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestGetBorder.docx'
        index = 0
        source_path = 'sections/0/tables/2/rows/0'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetBorderRequest(remote_name, source_path, index,
                                                                    os.path.join(
                                                                        self.remote_test_folder,
                                                                        self.test_folder))
        result = self.words_api.get_border(request)
        self.assertIsNotNone(result, 'Error has occurred while get border')

    #
    # Test for getting table borders
    #
    def test_get_borders(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestGetBorders.docx'
        source_path = 'sections/0/tables/2/rows/0'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetBordersRequest(remote_name, source_path,
                                                                     os.path.join(
                                                                         self.remote_test_folder,
                                                                         self.test_folder))
        result = self.words_api.get_borders(request)
        self.assertIsNotNone(result, 'Error has occurred while get borders')

    #
    # Test for getting table
    #
    def test_get_table(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestGetTable.docx'
        index = 1

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetTableRequest(remote_name, '', index,
                                                                 os.path.join(
                                                                     self.remote_test_folder,
                                                                     self.test_folder))
        result = self.words_api.get_table(request)
        self.assertIsNotNone(result, 'Error has occurred while get table')

    #
    # Test for getting table without node path
    #
    def test_get_table_without_node_path(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestGetTableWithoutNodePath.docx'
        index = 1

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetTableWithoutNodePathRequest(remote_name, index,
                                                                 os.path.join(
                                                                     self.remote_test_folder,
                                                                     self.test_folder))
        result = self.words_api.get_table_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while get table')

    #
    # Test for getting table cell
    #
    def test_get_table_cell(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestGetTableCell.docx'
        index = 0
        source_path = 'sections/0/tables/2/rows/0'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetTableCellRequest(remote_name, source_path, index,
                                                                       os.path.join(
                                                                           self.remote_test_folder,
                                                                           self.test_folder))
        result = self.words_api.get_table_cell(request)
        self.assertIsNotNone(result, 'Error has occurred while get table cell')

    #
    # Test for getting table cell format
    #
    def test_get_table_cell_format(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestGetTableCellFormat.docx'
        index = 0
        source_path = 'sections/0/tables/2/rows/0'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetTableCellFormatRequest(remote_name, source_path, index,
                                                                             os.path.join(
                                                                                 self.remote_test_folder,
                                                                                 self.test_folder))
        result = self.words_api.get_table_cell_format(request)
        self.assertIsNotNone(result, 'Error has occurred while get table cell format')

    #
    # Test for getting table row
    #
    def test_get_table_row(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestGetTableRow.docx'
        index = 0
        source_path = 'tables/1'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetTableRowRequest(remote_name, source_path, index,
                                                                      os.path.join(
                                                                          self.remote_test_folder,
                                                                          self.test_folder))
        result = self.words_api.get_table_row(request)
        self.assertIsNotNone(result, 'Error has occurred while get table row')

    #
    # Test for getting table row format
    #
    def test_get_table_row_format(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestGetTableRowFormat.docx'
        index = 0
        source_path = 'sections/0/tables/2'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetTableRowFormatRequest(remote_name, source_path, index,
                                                                            os.path.join(
                                                                                self.remote_test_folder,
                                                                                self.test_folder))
        result = self.words_api.get_table_row_format(request)
        self.assertIsNotNone(result, 'Error has occurred while get table row format')

    #
    # Test for getting tables
    #
    def test_get_tables(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestGetTables.docx'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetTablesRequest(remote_name, '',
                                                                  os.path.join(
                                                                      self.remote_test_folder,
                                                                      self.test_folder))
        result = self.words_api.get_tables(request)
        self.assertIsNotNone(result, 'Error has occurred while get tables')

    #
    # Test for getting tables without node path
    #
    def test_get_tables_without_node_path(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestGetTablesWithoutNodePath.docx'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetTablesWithoutNodePathRequest(remote_name,
                                                                  os.path.join(
                                                                      self.remote_test_folder,
                                                                      self.test_folder))
        result = self.words_api.get_tables_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while get tables')

    #
    # Test for inserting table
    #
    def test_insert_table(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestInsertTable.docx'
        body = asposewordscloud.TableInsert(columns_count=3, rows_count=5)

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.InsertTableRequest(remote_name, '',
                                                                    os.path.join(
                                                                        self.remote_test_folder,
                                                                        self.test_folder), table=body)
        result = self.words_api.insert_table(request)
        self.assertIsNotNone(result, 'Error has occurred while insert table')

    #
    # Test for inserting table without node path
    #
    def test_insert_table_without_node_path(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestInsertTableWithoutNodePath.docx'
        body = asposewordscloud.TableInsert(columns_count=3, rows_count=5)

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.InsertTableWithoutNodePathRequest(remote_name,
                                                                    os.path.join(
                                                                        self.remote_test_folder,
                                                                        self.test_folder), table=body)
        result = self.words_api.insert_table_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while insert table')

    #
    # Test for inserting table cell
    #
    def test_insert_table_cell(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestInsertTableCell.docx'
        body = asposewordscloud.TableCellInsert()
        source_path = 'sections/0/tables/2/rows/0'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.InsertTableCellRequest(remote_name, source_path,
                                                                          os.path.join(
                                                                              self.remote_test_folder,
                                                                              self.test_folder), cell=body)
        result = self.words_api.insert_table_cell(request)
        self.assertIsNotNone(result, 'Error has occurred while insert table cell')

    #
    # Test for inserting table row
    #
    def test_insert_table_row(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestInsertTableRow.docx'
        body = asposewordscloud.TableRowInsert(columns_count=5)
        source_path = 'sections/0/tables/2'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.InsertTableRowRequest(remote_name, source_path,
                                                                         os.path.join(
                                                                             self.remote_test_folder,
                                                                             self.test_folder), row=body)
        result = self.words_api.insert_table_row(request)
        self.assertIsNotNone(result, 'Error has occurred while insert table row')

    #
    # Test for rendering table
    #
    def test_render_table(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestRenderTable.docx'
        index = 0
        format = 'png'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.RenderTableRequest(remote_name, format, '', index,
                                                                    os.path.join(
                                                                        self.remote_test_folder,
                                                                        self.test_folder))
        result = self.words_api.render_table(request)
        self.assertTrue(len(result) > 0, 'Error has occurred while render table')

    #
    # Test for rendering table without node path
    #
    def test_render_table_without_node_path(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestRenderTableWithoutNodePath.docx'
        index = 0
        format = 'png'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.RenderTableWithoutNodePathRequest(remote_name, format, index,
                                                                    os.path.join(
                                                                        self.remote_test_folder,
                                                                        self.test_folder))
        result = self.words_api.render_table_without_node_path(request)
        self.assertTrue(len(result) > 0, 'Error has occurred while render table')

    #
    # Test for updating table cell format
    #
    def test_update_table_cell_format(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestUpdateTableCellFormat.docx'
        index = 0
        body = asposewordscloud.TableCellFormat(None, 5, True, 'First', wrap_text=True)
        source_path = 'sections/0/tables/2/rows/0'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.UpdateTableCellFormatRequest(remote_name, source_path, index,
                                                                                os.path.join(
                                                                                    self.remote_test_folder,
                                                                                    self.test_folder), format=body)
        result = self.words_api.update_table_cell_format(request)
        self.assertIsNotNone(result, 'Error has occurred while update table cell format')

    #
    # Test for getting table properties
    #
    def test_get_table_properties(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestGetTableProperties.docx'
        index = 1

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetTablePropertiesRequest(remote_name, '', index, 
                                                                           os.path.join(
                                                                               self.remote_test_folder,
                                                                               self.test_folder))
        result = self.words_api.get_table_properties(request)
        self.assertIsNotNone(result, 'Error has occurred while get table properties')

    #
    # Test for getting table properties without node path
    #
    def test_get_table_properties_without_node_path(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestGetTablePropertiesWithoutNodePath.docx'
        index = 1

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetTablePropertiesWithoutNodePathRequest(remote_name, index,
                                                                           os.path.join(
                                                                               self.remote_test_folder,
                                                                               self.test_folder))
        result = self.words_api.get_table_properties_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while get table properties')

    #
    # Test for updating table properties
    #
    def test_update_table_properties(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestUpdateTableProperties.docx'
        index = 1
        body = asposewordscloud.TableProperties(None, 'Right', False, True, 1, 2, 3, 4, right_padding=5,
                                                style_options='ColumnBands', top_padding=6)

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.UpdateTablePropertiesRequest(remote_name, '', index,
                                                                              os.path.join(
                                                                                  self.remote_test_folder,
                                                                                  self.test_folder), properties=body)
        result = self.words_api.update_table_properties(request)
        self.assertIsNotNone(result, 'Error has occurred while update table properties')

    #
    # Test for updating table properties without node path
    #
    def test_update_table_properties_without_node_path(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestUpdateTablePropertiesWithoutNodePath.docx'
        index = 1
        body = asposewordscloud.TableProperties(None, 'Right', False, True, 1, 2, 3, 4, right_padding=5,
                                              style_options='ColumnBands', top_padding=6)

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.UpdateTablePropertiesWithoutNodePathRequest(remote_name, index,
                                                                              os.path.join(
                                                                                  self.remote_test_folder,
                                                                                  self.test_folder), properties=body)
        result = self.words_api.update_table_properties_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred while update table properties')

    #
    # Test for updating table row format
    #
    def test_update_table_row_format(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestUpdateTableRowFormat.docx'
        index = 0
        body = asposewordscloud.TableRowFormat(None, True, True, 10, 'Auto')
        source_path = 'sections/0/tables/2'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.UpdateTableRowFormatRequest(remote_name, source_path, index,
                                                                               os.path.join(
                                                                                   self.remote_test_folder,
                                                                                   self.test_folder), format=body)
        result = self.words_api.update_table_row_format(request)
        self.assertIsNotNone(result, 'Error has occurred while update table row format')

    #
    # Test for removing border
    #
    def test_delete_border(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestDeleteTableBorder.docx'
        dest_name = os.path.join(self.remote_test_out, remote_name)
        index = 0
        source_path = 'tables/1/rows/0/cells/0/'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.DeleteBorderRequest(remote_name, source_path, index,
                                                                       os.path.join(
                                                                           self.remote_test_folder,
                                                                           self.test_folder), dest_file_name=dest_name)
        result = self.words_api.delete_border(request)
        self.assertIsNotNone(result, 'Error has occurred while delete table border')

    #
    # Test for removing border
    #
    def test_delete_borders(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestDeleteTableBorders.docx'
        source_path = 'tables/1/rows/0/cells/0/'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.DeleteBordersRequest(remote_name, source_path,
                                                                        os.path.join(
                                                                            self.remote_test_folder,
                                                                            self.test_folder))
        result = self.words_api.delete_borders(request)
        self.assertIsNotNone(result, 'Error has occurred while delete table borders')

    #
    # Test for updating borders
    #
    def test_update_border(self):
        filename = 'TablesGet.docx'
        remote_name = 'TestUpdateBorder.docx'
        index = 0
        body = asposewordscloud.Border(None, 'Left', asposewordscloud.XmlColor(None, 2), 6, 'DashDotStroker', 2, True)
        source_path = 'tables/1/rows/0/cells/0/'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.UpdateBorderRequest(remote_name, body, source_path, index,
                                                                       os.path.join(
                                                                           self.remote_test_folder,
                                                                           self.test_folder))
        result = self.words_api.update_border(request)
        self.assertIsNotNone(result, 'Error has occurred while update border')
