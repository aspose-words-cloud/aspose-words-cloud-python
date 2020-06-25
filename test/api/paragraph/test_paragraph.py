# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_paragraph.py">
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
# Example of how to work with paragraph.
#
class TestParagraph(BaseTestContext):
    #
    # Test for getting paragraph.
    #
    def test_get_document_paragraph_by_index(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentParagraphByIndex.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphRequest(name=remoteFileName, node_path='sections/0', index=0, folder=remoteDataFolder)

        result = self.words_api.get_paragraph(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting paragraph without node path.
    #
    def test_get_document_paragraph_by_index_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentParagraphByIndexWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphWithoutNodePathRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        result = self.words_api.get_paragraph_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting all paragraphs.
    #
    def test_get_document_paragraphs(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentParagraphs.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphsRequest(name=remoteFileName, node_path='sections/0', folder=remoteDataFolder)

        result = self.words_api.get_paragraphs(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting all paragraphs without node path.
    #
    def test_get_document_paragraphs_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentParagraphsWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphsWithoutNodePathRequest(name=remoteFileName, folder=remoteDataFolder)

        result = self.words_api.get_paragraphs_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting paragraph run.
    #
    def test_get_document_paragraph_run(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentParagraphRun.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetRunRequest(name=remoteFileName, paragraph_path='paragraphs/0', index=0, folder=remoteDataFolder)

        result = self.words_api.get_run(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting paragraph run font.
    #
    def test_get_document_paragraph_run_font(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentParagraphRunFont.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetRunFontRequest(name=remoteFileName, paragraph_path='paragraphs/0', index=0, folder=remoteDataFolder)

        result = self.words_api.get_run_font(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting paragraph runs.
    #
    def test_get_paragraph_runs(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetParagraphRuns.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetRunsRequest(name=remoteFileName, paragraph_path='sections/0/paragraphs/0', folder=remoteDataFolder)

        result = self.words_api.get_runs(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for updating paragraph run font.
    #
    def test_update_run_font(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestUpdateRunFont.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestFontDto = asposewordscloud.Font(bold=True)
        request = asposewordscloud.models.requests.UpdateRunFontRequest(name=remoteFileName, font_dto=requestFontDto, paragraph_path='paragraphs/0', index=0, folder=remoteDataFolder, dest_file_name=self.remote_test_out + '/' + remoteFileName)

        result = self.words_api.update_run_font(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for adding paragraph.
    #
    def test_insert_paragraph(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestInsertParagraph.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestParagraph = asposewordscloud.ParagraphInsert(text='This is a new paragraph for your document')
        request = asposewordscloud.models.requests.InsertParagraphRequest(name=remoteFileName, paragraph=requestParagraph, node_path='sections/0', folder=remoteDataFolder)

        result = self.words_api.insert_paragraph(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for adding paragraph without node path.
    #
    def test_insert_paragraph_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestInsertParagraphWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestParagraph = asposewordscloud.ParagraphInsert(text='This is a new paragraph for your document')
        request = asposewordscloud.models.requests.InsertParagraphWithoutNodePathRequest(name=remoteFileName, paragraph=requestParagraph, folder=remoteDataFolder)

        result = self.words_api.insert_paragraph_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for paragraph rendering.
    #
    def test_render_paragraph(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestRenderParagraph.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.RenderParagraphRequest(name=remoteFileName, format='png', node_path='', index=0, folder=remoteDataFolder)

        result = self.words_api.render_paragraph(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for paragraph rendering without node path.
    #
    def test_render_paragraph_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestRenderParagraphWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.RenderParagraphWithoutNodePathRequest(name=remoteFileName, format='png', index=0, folder=remoteDataFolder)

        result = self.words_api.render_paragraph_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting paragraph format settings.
    #
    def test_get_paragraph_format(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentParagraphs.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphFormatRequest(name=remoteFileName, node_path='', index=0, folder=remoteDataFolder)

        result = self.words_api.get_paragraph_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting paragraph format settings without node path.
    #
    def test_get_paragraph_format_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentParagraphsWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphFormatWithoutNodePathRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        result = self.words_api.get_paragraph_format_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for updating  paragraph format settings.
    #
    def test_update_paragraph_format(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentParagraphs.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestDto = asposewordscloud.ParagraphFormatUpdate(alignment='Right')
        request = asposewordscloud.models.requests.UpdateParagraphFormatRequest(name=remoteFileName, dto=requestDto, node_path='', index=0, folder=remoteDataFolder)

        result = self.words_api.update_paragraph_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for deleting  a paragraph.
    #
    def test_delete_paragraph(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestDeleteParagraph.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteParagraphRequest(name=remoteFileName, node_path='', index=0, folder=remoteDataFolder)

        self.words_api.delete_paragraph(request)


    #
    # Test for deleting  a paragraph without node path.
    #
    def test_delete_paragraph_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestDeleteParagraphWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteParagraphWithoutNodePathRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        self.words_api.delete_paragraph_without_node_path(request)


    #
    # Test for getting paragraph list format.
    #
    def test_get_paragraph_list_format(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        listFolder = 'DocumentElements/ParagraphListFormat'
        remoteFileName = 'TestParagraphGetListFormat.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, listFolder + '/ParagraphGetListFormat.doc'), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphListFormatRequest(name=remoteFileName, node_path='', index=0, folder=remoteDataFolder)

        result = self.words_api.get_paragraph_list_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting paragraph list format without node path.
    #
    def test_get_paragraph_list_format_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        listFolder = 'DocumentElements/ParagraphListFormat'
        remoteFileName = 'TestParagraphGetListFormatWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, listFolder + '/ParagraphGetListFormat.doc'), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphListFormatWithoutNodePathRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        result = self.words_api.get_paragraph_list_format_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for updating paragraph list format.
    #
    def test_update_paragraph_list_format(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        listFolder = 'DocumentElements/ParagraphListFormat'
        remoteFileName = 'TestUpdateParagraphListFormat.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, listFolder + '/ParagraphUpdateListFormat.doc'), 'rb'))

        requestDto = asposewordscloud.ListFormatUpdate(list_id=2)
        request = asposewordscloud.models.requests.UpdateParagraphListFormatRequest(name=remoteFileName, dto=requestDto, node_path='', index=0, folder=remoteDataFolder)

        result = self.words_api.update_paragraph_list_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for updating paragraph list format without node path.
    #
    def test_update_paragraph_list_format_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        listFolder = 'DocumentElements/ParagraphListFormat'
        remoteFileName = 'TestUpdateParagraphListFormatWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, listFolder + '/ParagraphUpdateListFormat.doc'), 'rb'))

        requestDto = asposewordscloud.ListFormatUpdate(list_id=2)
        request = asposewordscloud.models.requests.UpdateParagraphListFormatWithoutNodePathRequest(name=remoteFileName, dto=requestDto, index=0, folder=remoteDataFolder)

        result = self.words_api.update_paragraph_list_format_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for deleting paragraph list format.
    #
    def test_delete_paragraph_list_format(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        listFolder = 'DocumentElements/ParagraphListFormat'
        remoteFileName = 'TestDeleteParagraphListFormat.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, listFolder + '/ParagraphDeleteListFormat.doc'), 'rb'))

        request = asposewordscloud.models.requests.DeleteParagraphListFormatRequest(name=remoteFileName, node_path='', index=0, folder=remoteDataFolder)

        result = self.words_api.delete_paragraph_list_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for deleting paragraph list format without node path.
    #
    def test_delete_paragraph_list_format_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        listFolder = 'DocumentElements/ParagraphListFormat'
        remoteFileName = 'TestDeleteParagraphListFormatWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, listFolder + '/ParagraphDeleteListFormat.doc'), 'rb'))

        request = asposewordscloud.models.requests.DeleteParagraphListFormatWithoutNodePathRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        result = self.words_api.delete_paragraph_list_format_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting paragraph tab stops.
    #
    def test_get_paragraph_tab_stops(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tabStopFolder = 'DocumentElements/Paragraphs'
        remoteFileName = 'TestGetParagraphTabStops.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, tabStopFolder + '/ParagraphTabStops.docx'), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphTabStopsRequest(name=remoteFileName, node_path='', index=0, folder=remoteDataFolder)

        result = self.words_api.get_paragraph_tab_stops(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for getting paragraph tab stops without node path.
    #
    def test_get_paragraph_tab_stops_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tabStopFolder = 'DocumentElements/Paragraphs'
        remoteFileName = 'TestGetParagraphTabStopsWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, tabStopFolder + '/ParagraphTabStops.docx'), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphTabStopsWithoutNodePathRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        result = self.words_api.get_paragraph_tab_stops_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for inserting paragraph tab stop.
    #
    def test_insert_paragraph_tab_stops(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tabStopFolder = 'DocumentElements/Paragraphs'
        remoteFileName = 'TestInsertOrUpdateParagraphTabStop.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, tabStopFolder + '/ParagraphTabStops.docx'), 'rb'))

        requestDto = asposewordscloud.TabStopInsert(alignment='Left', leader='None', position=72)
        request = asposewordscloud.models.requests.InsertOrUpdateParagraphTabStopRequest(name=remoteFileName, dto=requestDto, node_path='', index=0, folder=remoteDataFolder)

        result = self.words_api.insert_or_update_paragraph_tab_stop(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for inserting paragraph tab stop without node path.
    #
    def test_insert_paragraph_tab_stops_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tabStopFolder = 'DocumentElements/Paragraphs'
        remoteFileName = 'TestInsertOrUpdateParagraphTabStopWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, tabStopFolder + '/ParagraphTabStops.docx'), 'rb'))

        requestDto = asposewordscloud.TabStopInsert(alignment='Left', leader='None', position=72)
        request = asposewordscloud.models.requests.InsertOrUpdateParagraphTabStopWithoutNodePathRequest(name=remoteFileName, dto=requestDto, index=0, folder=remoteDataFolder)

        result = self.words_api.insert_or_update_paragraph_tab_stop_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for deleting all paragraph tab stops.
    #
    def test_delete_all_paragraph_tab_stops(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tabStopFolder = 'DocumentElements/Paragraphs'
        remoteFileName = 'TestDeleteAllParagraphTabStops.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, tabStopFolder + '/ParagraphTabStops.docx'), 'rb'))

        request = asposewordscloud.models.requests.DeleteAllParagraphTabStopsRequest(name=remoteFileName, node_path='', index=0, folder=remoteDataFolder)

        result = self.words_api.delete_all_paragraph_tab_stops(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for deleting all paragraph tab stops without node path.
    #
    def test_delete_all_paragraph_tab_stops_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tabStopFolder = 'DocumentElements/Paragraphs'
        remoteFileName = 'TestDeleteAllParagraphTabStopsWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, tabStopFolder + '/ParagraphTabStops.docx'), 'rb'))

        request = asposewordscloud.models.requests.DeleteAllParagraphTabStopsWithoutNodePathRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        result = self.words_api.delete_all_paragraph_tab_stops_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for deleting a tab stops.
    #
    def test_delete_paragraph_tab_stop(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tabStopFolder = 'DocumentElements/Paragraphs'
        remoteFileName = 'TestDeleteParagraphTabStop.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, tabStopFolder + '/ParagraphTabStops.docx'), 'rb'))

        request = asposewordscloud.models.requests.DeleteParagraphTabStopRequest(name=remoteFileName, position=72, node_path='', index=0, folder=remoteDataFolder)

        result = self.words_api.delete_paragraph_tab_stop(request)
        self.assertIsNotNone(result, 'Error has occurred.')

    #
    # Test for deleting a tab stops without node path.
    #
    def test_delete_paragraph_tab_stop_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tabStopFolder = 'DocumentElements/Paragraphs'
        remoteFileName = 'TestDeleteParagraphTabStopWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, tabStopFolder + '/ParagraphTabStops.docx'), 'rb'))

        request = asposewordscloud.models.requests.DeleteParagraphTabStopWithoutNodePathRequest(name=remoteFileName, position=72, index=0, folder=remoteDataFolder)

        result = self.words_api.delete_paragraph_tab_stop_without_node_path(request)
        self.assertIsNotNone(result, 'Error has occurred.')
