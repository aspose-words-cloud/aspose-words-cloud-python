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

        request = asposewordscloud.models.requests.GetParagraphRequest(name=remoteFileName, index=0, node_path='sections/0', folder=remoteDataFolder)

        result = self.words_api.get_paragraph(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.paragraph, 'Validate GetDocumentParagraphByIndex response')
        self.assertIsTrue(result.paragraph.node_id.startswith('0.0.0'))

    #
    # Test for getting paragraph without node path.
    #
    def test_get_document_paragraph_by_index_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentParagraphByIndexWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        result = self.words_api.get_paragraph(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.paragraph, 'Validate GetDocumentParagraphByIndexWithoutNodePath response')
        self.assertIsTrue(result.paragraph.node_id.startswith('0.0.0'))

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
        self.assertIsNotNone(result.paragraphs, 'Validate GetDocumentParagraphs response')
        self.assertIsNotNone(result.paragraphs.paragraph_link_list, 'Validate GetDocumentParagraphs response')
        self.assertEqual(15, len(result.paragraphs.paragraph_link_list))
        self.assertIsTrue(result.paragraphs.paragraph_link_list[0].text.startswith('Page 1 of 3'))

    #
    # Test for getting all paragraphs without node path.
    #
    def test_get_document_paragraphs_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentParagraphsWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphsRequest(name=remoteFileName, folder=remoteDataFolder)

        result = self.words_api.get_paragraphs(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.paragraphs, 'Validate GetDocumentParagraphsWithoutNodePath response')
        self.assertIsNotNone(result.paragraphs.paragraph_link_list, 'Validate GetDocumentParagraphsWithoutNodePath response')
        self.assertEqual(15, len(result.paragraphs.paragraph_link_list))
        self.assertIsTrue(result.paragraphs.paragraph_link_list[0].text.startswith('Page 1 of 3'))

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
        self.assertIsNotNone(result.run, 'Validate GetDocumentParagraphRun response')
        self.assertIsTrue(result.run.text.startswith('Page '))

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
        self.assertIsNotNone(result.font, 'Validate GetDocumentParagraphRunFont response')
        self.assertIsTrue(result.font.name.startswith('Times New Roman'))

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
        self.assertIsNotNone(result.runs, 'Validate GetParagraphRuns response')
        self.assertIsNotNone(result.runs.list, 'Validate GetParagraphRuns response')
        self.assertEqual(6, len(result.runs.list))
        self.assertIsTrue(result.runs.list[0].text.startswith('Page '))

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
        self.assertIsNotNone(result.font, 'Validate UpdateRunFont response')
        self.assertIsTrue(result.font.bold, 'Validate UpdateRunFont response')

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
        self.assertIsNotNone(result.paragraph, 'Validate InsertParagraph response')
        self.assertIsTrue(result.paragraph.node_id.startswith('0.3.8'))

    #
    # Test for adding paragraph without node path.
    #
    def test_insert_paragraph_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestInsertParagraphWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestParagraph = asposewordscloud.ParagraphInsert(text='This is a new paragraph for your document')
        request = asposewordscloud.models.requests.InsertParagraphRequest(name=remoteFileName, paragraph=requestParagraph, folder=remoteDataFolder)

        result = self.words_api.insert_paragraph(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.paragraph, 'Validate InsertParagraphWithoutNodePath response')
        self.assertIsTrue(result.paragraph.node_id.startswith('0.3.8'))

    #
    # Test for paragraph rendering.
    #
    def test_render_paragraph(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestRenderParagraph.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.RenderParagraphRequest(name=remoteFileName, format='png', index=0, node_path='', folder=remoteDataFolder)

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

        request = asposewordscloud.models.requests.RenderParagraphRequest(name=remoteFileName, format='png', index=0, folder=remoteDataFolder)

        result = self.words_api.render_paragraph(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting paragraph format settings.
    #
    def test_get_paragraph_format(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentParagraphs.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphFormatRequest(name=remoteFileName, index=0, node_path='', folder=remoteDataFolder)

        result = self.words_api.get_paragraph_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.paragraph_format, 'Validate GetParagraphFormat response')
        self.assertIsTrue(result.paragraph_format.style_name.startswith('Normal'))

    #
    # Test for getting paragraph format settings without node path.
    #
    def test_get_paragraph_format_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentParagraphsWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphFormatRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        result = self.words_api.get_paragraph_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.paragraph_format, 'Validate GetParagraphFormatWithoutNodePath response')
        self.assertIsTrue(result.paragraph_format.style_name.startswith('Normal'))

    #
    # Test for updating  paragraph format settings.
    #
    def test_update_paragraph_format(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentParagraphs.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestDto = asposewordscloud.ParagraphFormatUpdate(alignment='Right')
        request = asposewordscloud.models.requests.UpdateParagraphFormatRequest(name=remoteFileName, dto=requestDto, index=0, node_path='', folder=remoteDataFolder)

        result = self.words_api.update_paragraph_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.paragraph_format, 'Validate UpdateParagraphFormat response')


    #
    # Test for deleting  a paragraph.
    #
    def test_delete_paragraph(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestDeleteParagraph.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteParagraphRequest(name=remoteFileName, index=0, node_path='', folder=remoteDataFolder)

        self.words_api.delete_paragraph(request)


    #
    # Test for deleting  a paragraph without node path.
    #
    def test_delete_paragraph_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestDeleteParagraphWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteParagraphRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        self.words_api.delete_paragraph(request)


    #
    # Test for getting paragraph list format.
    #
    def test_get_paragraph_list_format(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        listFolder = 'DocumentElements/ParagraphListFormat'
        remoteFileName = 'TestParagraphGetListFormat.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, listFolder + '/ParagraphGetListFormat.doc'), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphListFormatRequest(name=remoteFileName, index=0, node_path='', folder=remoteDataFolder)

        result = self.words_api.get_paragraph_list_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.list_format, 'Validate GetParagraphListFormat response')
        self.assertEqual(1, result.list_format.list_id)

    #
    # Test for getting paragraph list format without node path.
    #
    def test_get_paragraph_list_format_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        listFolder = 'DocumentElements/ParagraphListFormat'
        remoteFileName = 'TestParagraphGetListFormatWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, listFolder + '/ParagraphGetListFormat.doc'), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphListFormatRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        result = self.words_api.get_paragraph_list_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.list_format, 'Validate GetParagraphListFormatWithoutNodePath response')
        self.assertEqual(1, result.list_format.list_id)

    #
    # Test for updating paragraph list format.
    #
    def test_update_paragraph_list_format(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        listFolder = 'DocumentElements/ParagraphListFormat'
        remoteFileName = 'TestUpdateParagraphListFormat.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, listFolder + '/ParagraphUpdateListFormat.doc'), 'rb'))

        requestDto = asposewordscloud.ListFormatUpdate(list_id=2)
        request = asposewordscloud.models.requests.UpdateParagraphListFormatRequest(name=remoteFileName, dto=requestDto, index=0, node_path='', folder=remoteDataFolder)

        result = self.words_api.update_paragraph_list_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.list_format, 'Validate UpdateParagraphListFormat response')
        self.assertEqual(2, result.list_format.list_id)

    #
    # Test for updating paragraph list format without node path.
    #
    def test_update_paragraph_list_format_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        listFolder = 'DocumentElements/ParagraphListFormat'
        remoteFileName = 'TestUpdateParagraphListFormatWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, listFolder + '/ParagraphUpdateListFormat.doc'), 'rb'))

        requestDto = asposewordscloud.ListFormatUpdate(list_id=2)
        request = asposewordscloud.models.requests.UpdateParagraphListFormatRequest(name=remoteFileName, dto=requestDto, index=0, folder=remoteDataFolder)

        result = self.words_api.update_paragraph_list_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.list_format, 'Validate UpdateParagraphListFormatWithoutNodePath response')
        self.assertEqual(2, result.list_format.list_id)

    #
    # Test for deleting paragraph list format.
    #
    def test_delete_paragraph_list_format(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        listFolder = 'DocumentElements/ParagraphListFormat'
        remoteFileName = 'TestDeleteParagraphListFormat.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, listFolder + '/ParagraphDeleteListFormat.doc'), 'rb'))

        request = asposewordscloud.models.requests.DeleteParagraphListFormatRequest(name=remoteFileName, index=0, node_path='', folder=remoteDataFolder)

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

        request = asposewordscloud.models.requests.DeleteParagraphListFormatRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        result = self.words_api.delete_paragraph_list_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting paragraph tab stops.
    #
    def test_get_paragraph_tab_stops(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tabStopFolder = 'DocumentElements/Paragraphs'
        remoteFileName = 'TestGetParagraphTabStops.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, tabStopFolder + '/ParagraphTabStops.docx'), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphTabStopsRequest(name=remoteFileName, index=0, node_path='', folder=remoteDataFolder)

        result = self.words_api.get_paragraph_tab_stops(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.tab_stops, 'Validate GetParagraphTabStops response')
        self.assertEqual(2, len(result.tab_stops))
        self.assertEqual(72, result.tab_stops[0].position)

    #
    # Test for getting paragraph tab stops without node path.
    #
    def test_get_paragraph_tab_stops_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tabStopFolder = 'DocumentElements/Paragraphs'
        remoteFileName = 'TestGetParagraphTabStopsWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, tabStopFolder + '/ParagraphTabStops.docx'), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphTabStopsRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        result = self.words_api.get_paragraph_tab_stops(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.tab_stops, 'Validate GetParagraphTabStopsWithoutNodePath response')
        self.assertEqual(2, len(result.tab_stops))
        self.assertEqual(72, result.tab_stops[0].position)

    #
    # Test for inserting paragraph tab stop.
    #
    def test_insert_paragraph_tab_stops(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tabStopFolder = 'DocumentElements/Paragraphs'
        remoteFileName = 'TestInsertOrUpdateParagraphTabStop.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, tabStopFolder + '/ParagraphTabStops.docx'), 'rb'))

        requestDto = asposewordscloud.TabStopInsert(alignment='Left', leader='None', position=100)
        request = asposewordscloud.models.requests.InsertOrUpdateParagraphTabStopRequest(name=remoteFileName, dto=requestDto, index=0, node_path='', folder=remoteDataFolder)

        result = self.words_api.insert_or_update_paragraph_tab_stop(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.tab_stops, 'Validate InsertParagraphTabStops response')
        self.assertEqual(3, len(result.tab_stops))
        self.assertEqual(100, result.tab_stops[1].position)



    #
    # Test for inserting paragraph tab stop without node path.
    #
    def test_insert_paragraph_tab_stops_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tabStopFolder = 'DocumentElements/Paragraphs'
        remoteFileName = 'TestInsertOrUpdateParagraphTabStopWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, tabStopFolder + '/ParagraphTabStops.docx'), 'rb'))

        requestDto = asposewordscloud.TabStopInsert(alignment='Left', leader='None', position=100)
        request = asposewordscloud.models.requests.InsertOrUpdateParagraphTabStopRequest(name=remoteFileName, dto=requestDto, index=0, folder=remoteDataFolder)

        result = self.words_api.insert_or_update_paragraph_tab_stop(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.tab_stops, 'Validate InsertParagraphTabStopsWithoutNodePath response')
        self.assertEqual(3, len(result.tab_stops))
        self.assertEqual(100, result.tab_stops[1].position)



    #
    # Test for deleting all paragraph tab stops.
    #
    def test_delete_all_paragraph_tab_stops(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tabStopFolder = 'DocumentElements/Paragraphs'
        remoteFileName = 'TestDeleteAllParagraphTabStops.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, tabStopFolder + '/ParagraphTabStops.docx'), 'rb'))

        request = asposewordscloud.models.requests.DeleteAllParagraphTabStopsRequest(name=remoteFileName, index=0, node_path='', folder=remoteDataFolder)

        result = self.words_api.delete_all_paragraph_tab_stops(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.tab_stops, 'Validate DeleteAllParagraphTabStops response')
        self.assertEqual(0, len(result.tab_stops))

    #
    # Test for deleting all paragraph tab stops without node path.
    #
    def test_delete_all_paragraph_tab_stops_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tabStopFolder = 'DocumentElements/Paragraphs'
        remoteFileName = 'TestDeleteAllParagraphTabStopsWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, tabStopFolder + '/ParagraphTabStops.docx'), 'rb'))

        request = asposewordscloud.models.requests.DeleteAllParagraphTabStopsRequest(name=remoteFileName, index=0, folder=remoteDataFolder)

        result = self.words_api.delete_all_paragraph_tab_stops(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.tab_stops, 'Validate DeleteAllParagraphTabStopsWithoutNodePath response')
        self.assertEqual(0, len(result.tab_stops))

    #
    # Test for deleting a tab stops.
    #
    def test_delete_paragraph_tab_stop(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tabStopFolder = 'DocumentElements/Paragraphs'
        remoteFileName = 'TestDeleteParagraphTabStop.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, tabStopFolder + '/ParagraphTabStops.docx'), 'rb'))

        request = asposewordscloud.models.requests.DeleteParagraphTabStopRequest(name=remoteFileName, position=72, index=0, node_path='', folder=remoteDataFolder)

        result = self.words_api.delete_paragraph_tab_stop(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.tab_stops, 'Validate DeleteParagraphTabStop response')
        self.assertEqual(1, len(result.tab_stops))

    #
    # Test for deleting a tab stops without node path.
    #
    def test_delete_paragraph_tab_stop_without_node_path(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tabStopFolder = 'DocumentElements/Paragraphs'
        remoteFileName = 'TestDeleteParagraphTabStopWithoutNodePath.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, tabStopFolder + '/ParagraphTabStops.docx'), 'rb'))

        request = asposewordscloud.models.requests.DeleteParagraphTabStopRequest(name=remoteFileName, position=72, index=0, folder=remoteDataFolder)

        result = self.words_api.delete_paragraph_tab_stop(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.tab_stops, 'Validate DeleteParagraphTabStopWithoutNodePath response')
        self.assertEqual(1, len(result.tab_stops))
