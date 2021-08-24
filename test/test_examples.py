# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="TestExamples.py">
#   Copyright (c) 2021 Aspose.Words for Cloud
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
import asposewordscloud
import asposewordscloud.models.requests
from asposewordscloud.rest import ApiException
from shutil import copyfile
from test.base_test_context import BaseTestContext

class TestExamples(BaseTestContext):
    def setUp(self):
        super().setUp()

    def test_accept_all_revisions(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        file_name = 'test_doc.docx'

        # Upload original document to cloud storage.
        my_var1 = open(os.path.join(documents_dir, file_name), 'rb')
        my_var2 = file_name
        upload_file_request = asposewordscloud.models.requests.UploadFileRequest(file_content=my_var1, path=my_var2)
        words_api.upload_file(upload_file_request)

        # Calls AcceptAllRevisions method for document in cloud.
        my_var3 = file_name
        request = asposewordscloud.models.requests.AcceptAllRevisionsRequest(name=my_var3)
        words_api.accept_all_revisions(request)

    def test_accept_all_revisions_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        accept_request = asposewordscloud.models.requests.AcceptAllRevisionsOnlineRequest(document=request_document)
        words_api.accept_all_revisions_online(accept_request)

    def test_append_document(self):
        words_api = self.words_api
        remote_file_name= 'Sample.docx'

        request_document_list_document_entries0 = asposewordscloud.DocumentEntry(href=remote_file_name, import_format_mode='KeepSourceFormatting')
        request_document_list_document_entries = [request_document_list_document_entries0]
        request_document_list = asposewordscloud.DocumentEntryList(document_entries=request_document_list_document_entries)
        append_request = asposewordscloud.models.requests.AppendDocumentRequest(name=remote_file_name, document_list=request_document_list)
        words_api.append_document(append_request)

    def test_append_document_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_document_list_document_entries0 = asposewordscloud.DocumentEntry(href='Sample.docx', import_format_mode='KeepSourceFormatting')
        request_document_list_document_entries = [request_document_list_document_entries0]
        request_document_list = asposewordscloud.DocumentEntryList(document_entries=request_document_list_document_entries)
        append_request = asposewordscloud.models.requests.AppendDocumentOnlineRequest(document=request_document, document_list=request_document_list)
        words_api.append_document_online(append_request)

    def test_apply_style_to_document_element(self):
        words_api = self.words_api
        request_style_apply = asposewordscloud.StyleApply(style_name='Heading 1')
        apply_style_request = asposewordscloud.models.requests.ApplyStyleToDocumentElementRequest(name='Sample.docx', styled_node_path='paragraphs/1/paragraphFormat', style_apply=request_style_apply)
        words_api.apply_style_to_document_element(apply_style_request)

    def test_apply_style_to_document_element_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_style_apply = asposewordscloud.StyleApply(style_name='Heading 1')
        apply_style_request = asposewordscloud.models.requests.ApplyStyleToDocumentElementOnlineRequest(document=request_document, styled_node_path='paragraphs/1/paragraphFormat', style_apply=request_style_apply)
        words_api.apply_style_to_document_element_online(apply_style_request)

    def test_build_report(self):
        words_api = self.words_api
        request_report_engine_settings_report_build_options = ['AllowMissingMembers', 'RemoveEmptyParagraphs']
        request_report_engine_settings = asposewordscloud.ReportEngineSettings(data_source_type='Json', report_build_options=request_report_engine_settings_report_build_options)
        build_report_request = asposewordscloud.models.requests.BuildReportRequest(name='Sample.docx', data='Data.json', report_engine_settings=request_report_engine_settings)
        words_api.build_report(build_report_request)

    def test_build_report_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_template = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_report_engine_settings = asposewordscloud.ReportEngineSettings(data_source_type='Json', data_source_name='persons')
        build_report_request = asposewordscloud.models.requests.BuildReportOnlineRequest(template=request_template, data='Data.json', report_engine_settings=request_report_engine_settings)
        words_api.build_report_online(build_report_request)

    def test_classify(self):
        words_api = self.words_api
        classify_request = asposewordscloud.models.requests.ClassifyRequest(text='Try text classification', best_classes_count='3')
        words_api.classify(classify_request)

    def test_classify_document(self):
        words_api = self.words_api
        classify_request = asposewordscloud.models.requests.ClassifyDocumentRequest(name='Sample.docx', best_classes_count='3')
        words_api.classify_document(classify_request)

    def test_classify_document_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        classify_request = asposewordscloud.models.requests.ClassifyDocumentOnlineRequest(document=request_document, best_classes_count='3')
        words_api.classify_document_online(classify_request)

    def test_compare_document(self):
        words_api = self.words_api
        request_compare_data = asposewordscloud.CompareData(author='author', comparing_with_document='TestCompareDocument2.doc', date_time=dateutil.parser.isoparse('2015-10-26T00:00:00.0000000Z'))
        compare_request = asposewordscloud.models.requests.CompareDocumentRequest(name='TestCompareDocument1.doc', compare_data=request_compare_data, dest_file_name='/TestCompareDocumentOut.doc')
        words_api.compare_document(compare_request)

    def test_compare_document_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'compareTestDoc1.doc'), 'rb')
        request_compare_data = asposewordscloud.CompareData(author='author', comparing_with_document='TestCompareDocument2.doc', date_time=dateutil.parser.isoparse('2015-10-26T00:00:00.0000000Z'))
        request_comparing_document = open(os.path.join(documents_dir, 'compareTestDoc2.doc'), 'rb')
        compare_request = asposewordscloud.models.requests.CompareDocumentOnlineRequest(document=request_document, compare_data=request_compare_data, comparing_document=request_comparing_document, dest_file_name='/TestCompareDocumentOut.doc')
        words_api.compare_document_online(compare_request)

    def test_convert_document(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        convert_request = asposewordscloud.models.requests.ConvertDocumentRequest(document=request_document, format='pdf')
        words_api.convert_document(convert_request)

    def test_copy_file(self):
        words_api = self.words_api
        copy_request = asposewordscloud.models.requests.CopyFileRequest(dest_path='/TestCopyFileDest.docx', src_path='Sample.docx')
        words_api.copy_file(copy_request)

    def test_copy_folder(self):
        words_api = self.words_api
        folder_to_copy= '/TestCopyFolder'

        copy_request = asposewordscloud.models.requests.CopyFolderRequest(dest_path=folder_to_copy + 'Dest', src_path=folder_to_copy + 'Src')
        words_api.copy_folder(copy_request)

    def test_copy_style(self):
        words_api = self.words_api
        request_style_copy = asposewordscloud.StyleCopy(style_name='Heading 1')
        copy_request = asposewordscloud.models.requests.CopyStyleRequest(name='Sample.docx', style_copy=request_style_copy)
        words_api.copy_style(copy_request)

    def test_copy_style_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_style_copy = asposewordscloud.StyleCopy(style_name='Heading 1')
        copy_request = asposewordscloud.models.requests.CopyStyleOnlineRequest(document=request_document, style_copy=request_style_copy)
        words_api.copy_style_online(copy_request)

    def test_create_document(self):
        words_api = self.words_api
        create_request = asposewordscloud.models.requests.CreateDocumentRequest(file_name='Sample.docx')
        words_api.create_document(create_request)

    def test_create_folder(self):
        words_api = self.words_api
        create_request = asposewordscloud.models.requests.CreateFolderRequest(path='/TestCreateFolder')
        words_api.create_folder(create_request)

    def test_create_or_update_document_property(self):
        words_api = self.words_api
        request_property = asposewordscloud.DocumentPropertyCreateOrUpdate(value='Imran Anwar')
        create_request = asposewordscloud.models.requests.CreateOrUpdateDocumentPropertyRequest(name='Sample.docx', property_name='AsposeAuthor', _property=request_property)
        words_api.create_or_update_document_property(create_request)

    def test_create_or_update_document_property_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_property = asposewordscloud.DocumentPropertyCreateOrUpdate(value='Imran Anwar')
        create_request = asposewordscloud.models.requests.CreateOrUpdateDocumentPropertyOnlineRequest(document=request_document, property_name='AsposeAuthor', _property=request_property)
        words_api.create_or_update_document_property_online(create_request)

    def test_delete_all_paragraph_tab_stops(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteAllParagraphTabStopsRequest(name='Sample.docx', index=0)
        words_api.delete_all_paragraph_tab_stops(delete_request)

    def test_delete_all_paragraph_tab_stops_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteAllParagraphTabStopsOnlineRequest(document=request_document, index=0)
        words_api.delete_all_paragraph_tab_stops_online(delete_request)

    def test_delete_border(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteBorderRequest(name='Sample.docx', border_type='left', node_path='tables/1/rows/0/cells/0')
        words_api.delete_border(delete_request)

    def test_delete_border_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteBorderOnlineRequest(document=request_document, border_type='left', node_path='tables/1/rows/0/cells/0')
        words_api.delete_border_online(delete_request)

    def test_delete_borders(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteBordersRequest(name='Sample.docx', node_path='tables/1/rows/0/cells/0')
        words_api.delete_borders(delete_request)

    def test_delete_borders_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteBordersOnlineRequest(document=request_document, node_path='tables/1/rows/0/cells/0')
        words_api.delete_borders_online(delete_request)

    def test_delete_comment(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteCommentRequest(name='Sample.docx', comment_index=0)
        words_api.delete_comment(delete_request)

    def test_delete_comment_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteCommentOnlineRequest(document=request_document, comment_index=0)
        words_api.delete_comment_online(delete_request)

    def test_delete_comments(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteCommentsRequest(name='Sample.docx')
        words_api.delete_comments(delete_request)

    def test_delete_comments_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteCommentsOnlineRequest(document=request_document)
        words_api.delete_comments_online(delete_request)

    def test_delete_custom_xml_part(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteCustomXmlPartRequest(name='Sample.docx', custom_xml_part_index=0)
        words_api.delete_custom_xml_part(delete_request)

    def test_delete_custom_xml_part_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteCustomXmlPartOnlineRequest(document=request_document, custom_xml_part_index=0)
        words_api.delete_custom_xml_part_online(delete_request)

    def test_delete_custom_xml_parts(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteCustomXmlPartsRequest(name='Sample.docx')
        words_api.delete_custom_xml_parts(delete_request)

    def test_delete_custom_xml_parts_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteCustomXmlPartsOnlineRequest(document=request_document)
        words_api.delete_custom_xml_parts_online(delete_request)

    def test_delete_document_property(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteDocumentPropertyRequest(name='Sample.docx', property_name='testProp')
        words_api.delete_document_property(delete_request)

    def test_delete_document_property_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteDocumentPropertyOnlineRequest(document=request_document, property_name='testProp')
        words_api.delete_document_property_online(delete_request)

    def test_delete_drawing_object(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteDrawingObjectRequest(name='Sample.docx', index=0)
        words_api.delete_drawing_object(delete_request)

    def test_delete_drawing_object_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteDrawingObjectOnlineRequest(document=request_document, index=0)
        words_api.delete_drawing_object_online(delete_request)

    def test_delete_field(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteFieldRequest(name='Sample.docx', index=0)
        words_api.delete_field(delete_request)

    def test_delete_field_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteFieldOnlineRequest(document=request_document, index=0, node_path='sections/0/paragraphs/0')
        words_api.delete_field_online(delete_request)

    def test_delete_fields(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteFieldsRequest(name='Sample.docx')
        words_api.delete_fields(delete_request)

    def test_delete_fields_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteFieldsOnlineRequest(document=request_document)
        words_api.delete_fields_online(delete_request)

    def test_delete_file(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteFileRequest(path='Sample.docx')
        words_api.delete_file(delete_request)

    def test_delete_folder(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteFolderRequest(path='')
        words_api.delete_folder(delete_request)

    def test_delete_footnote(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteFootnoteRequest(name='Sample.docx', index=0)
        words_api.delete_footnote(delete_request)

    def test_delete_footnote_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteFootnoteOnlineRequest(document=request_document, index=0)
        words_api.delete_footnote_online(delete_request)

    def test_delete_form_field(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteFormFieldRequest(name='Sample.docx', index=0)
        words_api.delete_form_field(delete_request)

    def test_delete_form_field_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteFormFieldOnlineRequest(document=request_document, index=0, node_path='sections/0')
        words_api.delete_form_field_online(delete_request)

    def test_delete_header_footer(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteHeaderFooterRequest(name='Sample.docx', section_path='', index=0)
        words_api.delete_header_footer(delete_request)

    def test_delete_header_footer_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteHeaderFooterOnlineRequest(document=request_document, section_path='', index=0)
        words_api.delete_header_footer_online(delete_request)

    def test_delete_headers_footers(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteHeadersFootersRequest(name='Sample.docx', section_path='')
        words_api.delete_headers_footers(delete_request)

    def test_delete_headers_footers_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteHeadersFootersOnlineRequest(document=request_document, section_path='')
        words_api.delete_headers_footers_online(delete_request)

    def test_delete_macros(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteMacrosRequest(name='Sample.docx')
        words_api.delete_macros(delete_request)

    def test_delete_macros_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteMacrosOnlineRequest(document=request_document)
        words_api.delete_macros_online(delete_request)

    def test_delete_office_math_object(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteOfficeMathObjectRequest(name='Sample.docx', index=0)
        words_api.delete_office_math_object(delete_request)

    def test_delete_office_math_object_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteOfficeMathObjectOnlineRequest(document=request_document, index=0)
        words_api.delete_office_math_object_online(delete_request)

    def test_delete_paragraph(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteParagraphRequest(name='Sample.docx', index=0)
        words_api.delete_paragraph(delete_request)

    def test_delete_paragraph_list_format(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteParagraphListFormatRequest(name='Sample.docx', index=0)
        words_api.delete_paragraph_list_format(delete_request)

    def test_delete_paragraph_list_format_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteParagraphListFormatOnlineRequest(document=request_document, index=0)
        words_api.delete_paragraph_list_format_online(delete_request)

    def test_delete_paragraph_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteParagraphOnlineRequest(document=request_document, index=0)
        words_api.delete_paragraph_online(delete_request)

    def test_delete_paragraph_tab_stop(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteParagraphTabStopRequest(name='Sample.docx', position=72.0, index=0)
        words_api.delete_paragraph_tab_stop(delete_request)

    def test_delete_paragraph_tab_stop_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteParagraphTabStopOnlineRequest(document=request_document, position=72.0, index=0)
        words_api.delete_paragraph_tab_stop_online(delete_request)

    def test_delete_run(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteRunRequest(name='Sample.docx', paragraph_path='paragraphs/1', index=0)
        words_api.delete_run(delete_request)

    def test_delete_run_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteRunOnlineRequest(document=request_document, paragraph_path='paragraphs/1', index=0)
        words_api.delete_run_online(delete_request)

    def test_delete_section(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteSectionRequest(name='Sample.docx', section_index=0)
        words_api.delete_section(delete_request)

    def test_delete_section_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteSectionOnlineRequest(document=request_document, section_index=0)
        words_api.delete_section_online(delete_request)

    def test_delete_table(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteTableRequest(name='Sample.docx', index=1)
        words_api.delete_table(delete_request)

    def test_delete_table_cell(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteTableCellRequest(name='Sample.docx', table_row_path='sections/0/tables/2/rows/0', index=0)
        words_api.delete_table_cell(delete_request)

    def test_delete_table_cell_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteTableCellOnlineRequest(document=request_document, table_row_path='sections/0/tables/2/rows/0', index=0)
        words_api.delete_table_cell_online(delete_request)

    def test_delete_table_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteTableOnlineRequest(document=request_document, index=1)
        words_api.delete_table_online(delete_request)

    def test_delete_table_row(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteTableRowRequest(name='Sample.docx', table_path='tables/1', index=0)
        words_api.delete_table_row(delete_request)

    def test_delete_table_row_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteTableRowOnlineRequest(document=request_document, table_path='tables/1', index=0)
        words_api.delete_table_row_online(delete_request)

    def test_delete_watermark(self):
        words_api = self.words_api
        delete_request = asposewordscloud.models.requests.DeleteWatermarkRequest(name='Sample.docx')
        words_api.delete_watermark(delete_request)

    def test_delete_watermark_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        delete_request = asposewordscloud.models.requests.DeleteWatermarkOnlineRequest(document=request_document)
        words_api.delete_watermark_online(delete_request)

    def test_download_file(self):
        words_api = self.words_api
        download_request = asposewordscloud.models.requests.DownloadFileRequest(path='Sample.docx')
        words_api.download_file(download_request)

    def test_execute_mail_merge(self):
        words_api = self.words_api
        mail_merge_request = asposewordscloud.models.requests.ExecuteMailMergeRequest(name='Sample.docx', data='TestExecuteTemplateData.txt')
        words_api.execute_mail_merge(mail_merge_request)

    def test_execute_mail_merge_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_template = open(os.path.join(documents_dir, 'TestExecuteTemplate.doc'), 'rb')
        request_data = open(os.path.join(documents_dir, 'TestExecuteTemplateData.txt'), 'rb')
        mail_merge_request = asposewordscloud.models.requests.ExecuteMailMergeOnlineRequest(template=request_template, data=request_data)
        words_api.execute_mail_merge_online(mail_merge_request)

    def test_get_available_fonts(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetAvailableFontsRequest()
        words_api.get_available_fonts(request)

    def test_get_bookmark_by_name(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetBookmarkByNameRequest(name='Sample.docx', bookmark_name='aspose')
        words_api.get_bookmark_by_name(request)

    def test_get_bookmark_by_name_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetBookmarkByNameOnlineRequest(document=request_document, bookmark_name='aspose')
        words_api.get_bookmark_by_name_online(request)

    def test_get_bookmarks(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetBookmarksRequest(name='Sample.docx')
        words_api.get_bookmarks(request)

    def test_get_bookmarks_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetBookmarksOnlineRequest(document=request_document)
        words_api.get_bookmarks_online(request)

    def test_get_border(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetBorderRequest(name='Sample.docx', border_type='left', node_path='tables/1/rows/0/cells/0')
        words_api.get_border(request)

    def test_get_border_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetBorderOnlineRequest(document=request_document, border_type='left', node_path='tables/1/rows/0/cells/0')
        words_api.get_border_online(request)

    def test_get_borders(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetBordersRequest(name='Sample.docx', node_path='tables/1/rows/0/cells/0')
        words_api.get_borders(request)

    def test_get_borders_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetBordersOnlineRequest(document=request_document, node_path='tables/1/rows/0/cells/0')
        words_api.get_borders_online(request)

    def test_get_comment(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetCommentRequest(name='Sample.docx', comment_index=0)
        words_api.get_comment(request)

    def test_get_comment_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetCommentOnlineRequest(document=request_document, comment_index=0)
        words_api.get_comment_online(request)

    def test_get_comments(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetCommentsRequest(name='Sample.docx')
        words_api.get_comments(request)

    def test_get_comments_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetCommentsOnlineRequest(document=request_document)
        words_api.get_comments_online(request)

    def test_get_custom_xml_part(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetCustomXmlPartRequest(name='Sample.docx', custom_xml_part_index=0)
        words_api.get_custom_xml_part(request)

    def test_get_custom_xml_part_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetCustomXmlPartOnlineRequest(document=request_document, custom_xml_part_index=0)
        words_api.get_custom_xml_part_online(request)

    def test_get_custom_xml_parts(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetCustomXmlPartsRequest(name='Sample.docx')
        words_api.get_custom_xml_parts(request)

    def test_get_custom_xml_parts_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetCustomXmlPartsOnlineRequest(document=request_document)
        words_api.get_custom_xml_parts_online(request)

    def test_get_document(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetDocumentRequest(document_name='Sample.docx')
        words_api.get_document(request)

    def test_get_document_drawing_object_by_index(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetDocumentDrawingObjectByIndexRequest(name='Sample.docx', index=0)
        words_api.get_document_drawing_object_by_index(request)

    def test_get_document_drawing_object_by_index_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetDocumentDrawingObjectByIndexOnlineRequest(document=request_document, index=0, node_path='sections/0')
        words_api.get_document_drawing_object_by_index_online(request)

    def test_get_document_drawing_object_image_data(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetDocumentDrawingObjectImageDataRequest(name='Sample.docx', index=0)
        words_api.get_document_drawing_object_image_data(request)

    def test_get_document_drawing_object_image_data_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetDocumentDrawingObjectImageDataOnlineRequest(document=request_document, index=0, node_path='sections/0')
        words_api.get_document_drawing_object_image_data_online(request)

    def test_get_document_drawing_object_ole_data(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetDocumentDrawingObjectOleDataRequest(name='Sample.docx', index=0)
        words_api.get_document_drawing_object_ole_data(request)

    def test_get_document_drawing_object_ole_data_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetDocumentDrawingObjectOleDataOnlineRequest(document=request_document, index=0, node_path='sections/0')
        words_api.get_document_drawing_object_ole_data_online(request)

    def test_get_document_drawing_objects(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetDocumentDrawingObjectsRequest(name='Sample.docx')
        words_api.get_document_drawing_objects(request)

    def test_get_document_drawing_objects_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetDocumentDrawingObjectsOnlineRequest(document=request_document, node_path='sections/0')
        words_api.get_document_drawing_objects_online(request)

    def test_get_document_field_names(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetDocumentFieldNamesRequest(name='Sample.docx')
        words_api.get_document_field_names(request)

    def test_get_document_field_names_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_template = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetDocumentFieldNamesOnlineRequest(template=request_template, use_non_merge_fields=True)
        words_api.get_document_field_names_online(request)

    def test_get_document_hyperlink_by_index(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetDocumentHyperlinkByIndexRequest(name='Sample.docx', hyperlink_index=0)
        words_api.get_document_hyperlink_by_index(request)

    def test_get_document_hyperlink_by_index_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetDocumentHyperlinkByIndexOnlineRequest(document=request_document, hyperlink_index=0)
        words_api.get_document_hyperlink_by_index_online(request)

    def test_get_document_hyperlinks(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetDocumentHyperlinksRequest(name='Sample.docx')
        words_api.get_document_hyperlinks(request)

    def test_get_document_hyperlinks_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetDocumentHyperlinksOnlineRequest(document=request_document)
        words_api.get_document_hyperlinks_online(request)

    def test_get_document_properties(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetDocumentPropertiesRequest(name='Sample.docx')
        words_api.get_document_properties(request)

    def test_get_document_properties_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetDocumentPropertiesOnlineRequest(document=request_document)
        words_api.get_document_properties_online(request)

    def test_get_document_property(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetDocumentPropertyRequest(name='Sample.docx', property_name='Author')
        words_api.get_document_property(request)

    def test_get_document_property_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetDocumentPropertyOnlineRequest(document=request_document, property_name='Author')
        words_api.get_document_property_online(request)

    def test_get_document_protection(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetDocumentProtectionRequest(name='Sample.docx')
        words_api.get_document_protection(request)

    def test_get_document_protection_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetDocumentProtectionOnlineRequest(document=request_document)
        words_api.get_document_protection_online(request)

    def test_get_document_statistics(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetDocumentStatisticsRequest(name='Sample.docx')
        words_api.get_document_statistics(request)

    def test_get_document_statistics_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetDocumentStatisticsOnlineRequest(document=request_document)
        words_api.get_document_statistics_online(request)

    def test_get_document_with_format(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetDocumentWithFormatRequest(name='Sample.docx', format='text', out_path='/TestGetDocumentWithFormatAndOutPath.text')
        words_api.get_document_with_format(request)

    def test_get_field(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetFieldRequest(name='Sample.docx', index=0)
        words_api.get_field(request)

    def test_get_field_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetFieldOnlineRequest(document=request_document, index=0, node_path='sections/0/paragraphs/0')
        words_api.get_field_online(request)

    def test_get_fields(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetFieldsRequest(name='Sample.docx')
        words_api.get_fields(request)

    def test_get_fields_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetFieldsOnlineRequest(document=request_document, node_path='sections/0')
        words_api.get_fields_online(request)

    def test_get_files_list(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetFilesListRequest(path='')
        words_api.get_files_list(request)

    def test_get_footnote(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetFootnoteRequest(name='Sample.docx', index=0)
        words_api.get_footnote(request)

    def test_get_footnote_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        request = asposewordscloud.models.requests.GetFootnoteOnlineRequest(document=request_document, index=0)
        words_api.get_footnote_online(request)

    def test_get_footnotes(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetFootnotesRequest(name='Sample.docx')
        words_api.get_footnotes(request)

    def test_get_footnotes_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        request = asposewordscloud.models.requests.GetFootnotesOnlineRequest(document=request_document)
        words_api.get_footnotes_online(request)

    def test_get_form_field(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetFormFieldRequest(name='Sample.docx', index=0)
        words_api.get_form_field(request)

    def test_get_form_field_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetFormFieldOnlineRequest(document=request_document, index=0, node_path='sections/0')
        words_api.get_form_field_online(request)

    def test_get_form_fields(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetFormFieldsRequest(name='Sample.docx')
        words_api.get_form_fields(request)

    def test_get_form_fields_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetFormFieldsOnlineRequest(document=request_document, node_path='sections/0')
        words_api.get_form_fields_online(request)

    def test_get_header_footer(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetHeaderFooterRequest(name='Sample.docx', header_footer_index=0)
        words_api.get_header_footer(request)

    def test_get_header_footer_of_section(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetHeaderFooterOfSectionRequest(name='Sample.docx', header_footer_index=0, section_index=0)
        words_api.get_header_footer_of_section(request)

    def test_get_header_footer_of_section_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        request = asposewordscloud.models.requests.GetHeaderFooterOfSectionOnlineRequest(document=request_document, header_footer_index=0, section_index=0)
        words_api.get_header_footer_of_section_online(request)

    def test_get_header_footer_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        request = asposewordscloud.models.requests.GetHeaderFooterOnlineRequest(document=request_document, header_footer_index=0)
        words_api.get_header_footer_online(request)

    def test_get_header_footers(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetHeaderFootersRequest(name='Sample.docx', section_path='')
        words_api.get_header_footers(request)

    def test_get_header_footers_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        request = asposewordscloud.models.requests.GetHeaderFootersOnlineRequest(document=request_document, section_path='')
        words_api.get_header_footers_online(request)

    def test_get_list(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetListRequest(name='TestGetLists.doc', list_id=1)
        words_api.get_list(request)

    def test_get_list_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        request = asposewordscloud.models.requests.GetListOnlineRequest(document=request_document, list_id=1)
        words_api.get_list_online(request)

    def test_get_lists(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetListsRequest(name='TestGetLists.doc')
        words_api.get_lists(request)

    def test_get_lists_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        request = asposewordscloud.models.requests.GetListsOnlineRequest(document=request_document)
        words_api.get_lists_online(request)

    def test_get_office_math_object(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetOfficeMathObjectRequest(name='Sample.docx', index=0)
        words_api.get_office_math_object(request)

    def test_get_office_math_object_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetOfficeMathObjectOnlineRequest(document=request_document, index=0)
        words_api.get_office_math_object_online(request)

    def test_get_office_math_objects(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetOfficeMathObjectsRequest(name='Sample.docx')
        words_api.get_office_math_objects(request)

    def test_get_office_math_objects_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetOfficeMathObjectsOnlineRequest(document=request_document)
        words_api.get_office_math_objects_online(request)

    def test_get_paragraph(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetParagraphRequest(name='Sample.docx', index=0)
        words_api.get_paragraph(request)

    def test_get_paragraph_format(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetParagraphFormatRequest(name='Sample.docx', index=0)
        words_api.get_paragraph_format(request)

    def test_get_paragraph_format_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetParagraphFormatOnlineRequest(document=request_document, index=0)
        words_api.get_paragraph_format_online(request)

    def test_get_paragraph_list_format(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetParagraphListFormatRequest(name='Sample.docx', index=0)
        words_api.get_paragraph_list_format(request)

    def test_get_paragraph_list_format_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        request = asposewordscloud.models.requests.GetParagraphListFormatOnlineRequest(document=request_document, index=0)
        words_api.get_paragraph_list_format_online(request)

    def test_get_paragraph_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetParagraphOnlineRequest(document=request_document, index=0, node_path='sections/0')
        words_api.get_paragraph_online(request)

    def test_get_paragraphs(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetParagraphsRequest(name='Sample.docx')
        words_api.get_paragraphs(request)

    def test_get_paragraphs_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetParagraphsOnlineRequest(document=request_document, node_path='sections/0')
        words_api.get_paragraphs_online(request)

    def test_get_paragraph_tab_stops(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetParagraphTabStopsRequest(name='Sample.docx', index=0)
        words_api.get_paragraph_tab_stops(request)

    def test_get_paragraph_tab_stops_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetParagraphTabStopsOnlineRequest(document=request_document, index=0)
        words_api.get_paragraph_tab_stops_online(request)

    def test_get_public_key(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetPublicKeyRequest()
        words_api.get_public_key(request)

    def test_get_range_text(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetRangeTextRequest(name='Sample.docx', range_start_identifier='id0.0.0', range_end_identifier='id0.0.1')
        words_api.get_range_text(request)

    def test_get_range_text_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        request = asposewordscloud.models.requests.GetRangeTextOnlineRequest(document=request_document, range_start_identifier='id0.0.0', range_end_identifier='id0.0.1')
        words_api.get_range_text_online(request)

    def test_get_run(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetRunRequest(name='Sample.docx', paragraph_path='paragraphs/0', index=0)
        words_api.get_run(request)

    def test_get_run_font(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetRunFontRequest(name='Sample.docx', paragraph_path='paragraphs/0', index=0)
        words_api.get_run_font(request)

    def test_get_run_font_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetRunFontOnlineRequest(document=request_document, paragraph_path='paragraphs/0', index=0)
        words_api.get_run_font_online(request)

    def test_get_run_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetRunOnlineRequest(document=request_document, paragraph_path='paragraphs/0', index=0)
        words_api.get_run_online(request)

    def test_get_runs(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetRunsRequest(name='Sample.docx', paragraph_path='sections/0/paragraphs/0')
        words_api.get_runs(request)

    def test_get_runs_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetRunsOnlineRequest(document=request_document, paragraph_path='sections/0/paragraphs/0')
        words_api.get_runs_online(request)

    def test_get_section(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetSectionRequest(name='Sample.docx', section_index=0)
        words_api.get_section(request)

    def test_get_section_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetSectionOnlineRequest(document=request_document, section_index=0)
        words_api.get_section_online(request)

    def test_get_section_page_setup(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetSectionPageSetupRequest(name='Sample.docx', section_index=0)
        words_api.get_section_page_setup(request)

    def test_get_section_page_setup_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetSectionPageSetupOnlineRequest(document=request_document, section_index=0)
        words_api.get_section_page_setup_online(request)

    def test_get_sections(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetSectionsRequest(name='Sample.docx')
        words_api.get_sections(request)

    def test_get_sections_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetSectionsOnlineRequest(document=request_document)
        words_api.get_sections_online(request)

    def test_get_style(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetStyleRequest(name='Sample.docx', style_name='Heading 1')
        words_api.get_style(request)

    def test_get_style_from_document_element(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetStyleFromDocumentElementRequest(name='Sample.docx', styled_node_path='paragraphs/1/paragraphFormat')
        words_api.get_style_from_document_element(request)

    def test_get_style_from_document_element_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetStyleFromDocumentElementOnlineRequest(document=request_document, styled_node_path='paragraphs/1/paragraphFormat')
        words_api.get_style_from_document_element_online(request)

    def test_get_style_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetStyleOnlineRequest(document=request_document, style_name='Heading 1')
        words_api.get_style_online(request)

    def test_get_styles(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetStylesRequest(name='Sample.docx')
        words_api.get_styles(request)

    def test_get_styles_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetStylesOnlineRequest(document=request_document)
        words_api.get_styles_online(request)

    def test_get_table(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetTableRequest(name='Sample.docx', index=1)
        words_api.get_table(request)

    def test_get_table_cell(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetTableCellRequest(name='Sample.docx', table_row_path='sections/0/tables/2/rows/0', index=0)
        words_api.get_table_cell(request)

    def test_get_table_cell_format(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetTableCellFormatRequest(name='Sample.docx', table_row_path='sections/0/tables/2/rows/0', index=0)
        words_api.get_table_cell_format(request)

    def test_get_table_cell_format_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetTableCellFormatOnlineRequest(document=request_document, table_row_path='sections/0/tables/2/rows/0', index=0)
        words_api.get_table_cell_format_online(request)

    def test_get_table_cell_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetTableCellOnlineRequest(document=request_document, table_row_path='sections/0/tables/2/rows/0', index=0)
        words_api.get_table_cell_online(request)

    def test_get_table_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetTableOnlineRequest(document=request_document, index=1)
        words_api.get_table_online(request)

    def test_get_table_properties(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetTablePropertiesRequest(name='Sample.docx', index=1)
        words_api.get_table_properties(request)

    def test_get_table_properties_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetTablePropertiesOnlineRequest(document=request_document, index=1)
        words_api.get_table_properties_online(request)

    def test_get_table_row(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetTableRowRequest(name='Sample.docx', table_path='tables/1', index=0)
        words_api.get_table_row(request)

    def test_get_table_row_format(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetTableRowFormatRequest(name='Sample.docx', table_path='sections/0/tables/2', index=0)
        words_api.get_table_row_format(request)

    def test_get_table_row_format_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetTableRowFormatOnlineRequest(document=request_document, table_path='sections/0/tables/2', index=0)
        words_api.get_table_row_format_online(request)

    def test_get_table_row_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetTableRowOnlineRequest(document=request_document, table_path='tables/1', index=0)
        words_api.get_table_row_online(request)

    def test_get_tables(self):
        words_api = self.words_api
        request = asposewordscloud.models.requests.GetTablesRequest(name='Sample.docx')
        words_api.get_tables(request)

    def test_get_tables_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request = asposewordscloud.models.requests.GetTablesOnlineRequest(document=request_document)
        words_api.get_tables_online(request)

    def test_insert_comment(self):
        words_api = self.words_api
        request_comment_range_start_node = asposewordscloud.NodeLink(node_id='0.3.0.3')
        request_comment_range_start = asposewordscloud.DocumentPosition(node=request_comment_range_start_node, offset=0)
        request_comment_range_end_node = asposewordscloud.NodeLink(node_id='0.3.0.3')
        request_comment_range_end = asposewordscloud.DocumentPosition(node=request_comment_range_end_node, offset=0)
        request_comment = asposewordscloud.CommentInsert(range_start=request_comment_range_start, range_end=request_comment_range_end, initial='IA', author='Imran Anwar', text='A new Comment')
        insert_request = asposewordscloud.models.requests.InsertCommentRequest(name='Sample.docx', comment=request_comment)
        words_api.insert_comment(insert_request)

    def test_insert_comment_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_comment_range_start_node = asposewordscloud.NodeLink(node_id='0.3.0.3')
        request_comment_range_start = asposewordscloud.DocumentPosition(node=request_comment_range_start_node, offset=0)
        request_comment_range_end_node = asposewordscloud.NodeLink(node_id='0.3.0.3')
        request_comment_range_end = asposewordscloud.DocumentPosition(node=request_comment_range_end_node, offset=0)
        request_comment = asposewordscloud.CommentInsert(range_start=request_comment_range_start, range_end=request_comment_range_end, initial='IA', author='Imran Anwar', text='A new Comment')
        insert_request = asposewordscloud.models.requests.InsertCommentOnlineRequest(document=request_document, comment=request_comment)
        words_api.insert_comment_online(insert_request)

    def test_insert_custom_xml_part(self):
        words_api = self.words_api
        request_custom_xml_part = asposewordscloud.CustomXmlPartInsert(id='hello', data='<data>Hello world</data>')
        insert_request = asposewordscloud.models.requests.InsertCustomXmlPartRequest(name='Sample.docx', custom_xml_part=request_custom_xml_part)
        words_api.insert_custom_xml_part(insert_request)

    def test_insert_custom_xml_part_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_custom_xml_part = asposewordscloud.CustomXmlPartInsert(id='hello', data='<data>Hello world</data>')
        insert_request = asposewordscloud.models.requests.InsertCustomXmlPartOnlineRequest(document=request_document, custom_xml_part=request_custom_xml_part)
        words_api.insert_custom_xml_part_online(insert_request)

    def test_insert_drawing_object(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_drawing_object = asposewordscloud.DrawingObjectInsert(height=0, left=0, top=0, width=0, relative_horizontal_position='Margin', relative_vertical_position='Margin', wrap_type='Inline')
        request_image_file = open(os.path.join(documents_dir, 'Common/aspose-cloud.png'), 'rb')
        insert_request = asposewordscloud.models.requests.InsertDrawingObjectRequest(name='Sample.docx', drawing_object=request_drawing_object, image_file=request_image_file)
        words_api.insert_drawing_object(insert_request)

    def test_insert_drawing_object_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_drawing_object = asposewordscloud.DrawingObjectInsert(height=0, left=0, top=0, width=0, relative_horizontal_position='Margin', relative_vertical_position='Margin', wrap_type='Inline')
        request_image_file = open(os.path.join(documents_dir, 'Common/aspose-cloud.png'), 'rb')
        insert_request = asposewordscloud.models.requests.InsertDrawingObjectOnlineRequest(document=request_document, drawing_object=request_drawing_object, image_file=request_image_file)
        words_api.insert_drawing_object_online(insert_request)

    def test_insert_field(self):
        words_api = self.words_api
        request_field = asposewordscloud.FieldInsert(field_code='{ NUMPAGES }')
        insert_request = asposewordscloud.models.requests.InsertFieldRequest(name='Sample.docx', field=request_field)
        words_api.insert_field(insert_request)

    def test_insert_field_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_field = asposewordscloud.FieldInsert(field_code='{ NUMPAGES }')
        insert_request = asposewordscloud.models.requests.InsertFieldOnlineRequest(document=request_document, field=request_field, node_path='sections/0/paragraphs/0')
        words_api.insert_field_online(insert_request)

    def test_insert_footnote(self):
        words_api = self.words_api
        request_footnote_dto = asposewordscloud.FootnoteInsert(footnote_type='Endnote', text='test endnote')
        insert_request = asposewordscloud.models.requests.InsertFootnoteRequest(name='Sample.docx', footnote_dto=request_footnote_dto)
        words_api.insert_footnote(insert_request)

    def test_insert_footnote_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        request_footnote_dto = asposewordscloud.FootnoteInsert(footnote_type='Endnote', text='test endnote')
        insert_request = asposewordscloud.models.requests.InsertFootnoteOnlineRequest(document=request_document, footnote_dto=request_footnote_dto)
        words_api.insert_footnote_online(insert_request)

    def test_insert_form_field(self):
        words_api = self.words_api
        request_form_field = asposewordscloud.FormFieldTextInput(name='FullName', enabled=True, calculate_on_exit=True, status_text='', text_input_type='Regular', text_input_default='123', text_input_format='UPPERCASE')
        insert_request = asposewordscloud.models.requests.InsertFormFieldRequest(name='Sample.docx', form_field=request_form_field)
        words_api.insert_form_field(insert_request)

    def test_insert_form_field_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_form_field = asposewordscloud.FormFieldTextInput(name='FullName', enabled=True, calculate_on_exit=True, status_text='', text_input_type='Regular', text_input_default='123', text_input_format='UPPERCASE')
        insert_request = asposewordscloud.models.requests.InsertFormFieldOnlineRequest(document=request_document, form_field=request_form_field, node_path='sections/0/paragraphs/0')
        words_api.insert_form_field_online(insert_request)

    def test_insert_header_footer(self):
        words_api = self.words_api
        insert_request = asposewordscloud.models.requests.InsertHeaderFooterRequest(name='Sample.docx', section_path='', header_footer_type='FooterEven')
        words_api.insert_header_footer(insert_request)

    def test_insert_header_footer_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        insert_request = asposewordscloud.models.requests.InsertHeaderFooterOnlineRequest(document=request_document, section_path='', header_footer_type='FooterEven')
        words_api.insert_header_footer_online(insert_request)

    def test_insert_list(self):
        words_api = self.words_api
        request_list_insert = asposewordscloud.ListInsert(template='OutlineLegal')
        insert_request = asposewordscloud.models.requests.InsertListRequest(name='TestGetLists.doc', list_insert=request_list_insert)
        words_api.insert_list(insert_request)

    def test_insert_list_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        request_list_insert = asposewordscloud.ListInsert(template='OutlineLegal')
        insert_request = asposewordscloud.models.requests.InsertListOnlineRequest(document=request_document, list_insert=request_list_insert)
        words_api.insert_list_online(insert_request)

    def test_insert_or_update_paragraph_tab_stop(self):
        words_api = self.words_api
        request_tab_stop_insert_dto = asposewordscloud.TabStopInsert(alignment='Left', leader='None', position=100.0)
        insert_request = asposewordscloud.models.requests.InsertOrUpdateParagraphTabStopRequest(name='Sample.docx', index=0, tab_stop_insert_dto=request_tab_stop_insert_dto)
        words_api.insert_or_update_paragraph_tab_stop(insert_request)

    def test_insert_or_update_paragraph_tab_stop_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_tab_stop_insert_dto = asposewordscloud.TabStopInsert(alignment='Left', leader='None', position=72)
        insert_request = asposewordscloud.models.requests.InsertOrUpdateParagraphTabStopOnlineRequest(document=request_document, tab_stop_insert_dto=request_tab_stop_insert_dto, index=0)
        words_api.insert_or_update_paragraph_tab_stop_online(insert_request)

    def test_insert_page_numbers(self):
        words_api = self.words_api
        request_page_number = asposewordscloud.PageNumber(alignment='center', format='{PAGE} of {NUMPAGES}')
        insert_request = asposewordscloud.models.requests.InsertPageNumbersRequest(name='Sample.docx', page_number=request_page_number)
        words_api.insert_page_numbers(insert_request)

    def test_insert_page_numbers_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Common/Sample.docx'), 'rb')
        request_page_number = asposewordscloud.PageNumber(alignment='center', format='{PAGE} of {NUMPAGES}')
        insert_request = asposewordscloud.models.requests.InsertPageNumbersOnlineRequest(document=request_document, page_number=request_page_number)
        words_api.insert_page_numbers_online(insert_request)

    def test_insert_paragraph(self):
        words_api = self.words_api
        request_paragraph = asposewordscloud.ParagraphInsert(text='This is a new paragraph for your document')
        insert_request = asposewordscloud.models.requests.InsertParagraphRequest(name='Sample.docx', paragraph=request_paragraph)
        words_api.insert_paragraph(insert_request)

    def test_insert_paragraph_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_paragraph = asposewordscloud.ParagraphInsert(text='This is a new paragraph for your document')
        insert_request = asposewordscloud.models.requests.InsertParagraphOnlineRequest(document=request_document, paragraph=request_paragraph, node_path='sections/0')
        words_api.insert_paragraph_online(insert_request)

    def test_insert_run(self):
        words_api = self.words_api
        request_run = asposewordscloud.RunInsert(text='run with text')
        insert_request = asposewordscloud.models.requests.InsertRunRequest(name='Sample.docx', paragraph_path='paragraphs/1', run=request_run)
        words_api.insert_run(insert_request)

    def test_insert_run_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        request_run = asposewordscloud.RunInsert(text='run with text')
        insert_request = asposewordscloud.models.requests.InsertRunOnlineRequest(document=request_document, paragraph_path='paragraphs/1', run=request_run)
        words_api.insert_run_online(insert_request)

    def test_insert_style(self):
        words_api = self.words_api
        request_style_insert = asposewordscloud.StyleInsert(style_name='My Style', style_type='Paragraph')
        insert_request = asposewordscloud.models.requests.InsertStyleRequest(name='Sample.docx', style_insert=request_style_insert)
        words_api.insert_style(insert_request)

    def test_insert_style_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_style_insert = asposewordscloud.StyleInsert(style_name='My Style', style_type='Paragraph')
        insert_request = asposewordscloud.models.requests.InsertStyleOnlineRequest(document=request_document, style_insert=request_style_insert)
        words_api.insert_style_online(insert_request)

    def test_insert_table(self):
        words_api = self.words_api
        request_table = asposewordscloud.TableInsert(columns_count=5, rows_count=4)
        insert_request = asposewordscloud.models.requests.InsertTableRequest(name='Sample.docx', table=request_table)
        words_api.insert_table(insert_request)

    def test_insert_table_cell(self):
        words_api = self.words_api
        request_cell = asposewordscloud.TableCellInsert()
        insert_request = asposewordscloud.models.requests.InsertTableCellRequest(name='Sample.docx', table_row_path='sections/0/tables/2/rows/0', cell=request_cell)
        words_api.insert_table_cell(insert_request)

    def test_insert_table_cell_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_cell = asposewordscloud.TableCellInsert()
        insert_request = asposewordscloud.models.requests.InsertTableCellOnlineRequest(document=request_document, table_row_path='sections/0/tables/2/rows/0', cell=request_cell)
        words_api.insert_table_cell_online(insert_request)

    def test_insert_table_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_table = asposewordscloud.TableInsert(columns_count=5, rows_count=4)
        insert_request = asposewordscloud.models.requests.InsertTableOnlineRequest(document=request_document, table=request_table)
        words_api.insert_table_online(insert_request)

    def test_insert_table_row(self):
        words_api = self.words_api
        request_row = asposewordscloud.TableRowInsert(columns_count=5)
        insert_request = asposewordscloud.models.requests.InsertTableRowRequest(name='Sample.docx', table_path='sections/0/tables/2', row=request_row)
        words_api.insert_table_row(insert_request)

    def test_insert_table_row_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_row = asposewordscloud.TableRowInsert(columns_count=5)
        insert_request = asposewordscloud.models.requests.InsertTableRowOnlineRequest(document=request_document, table_path='sections/0/tables/2', row=request_row)
        words_api.insert_table_row_online(insert_request)

    def test_insert_watermark_image(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        insert_request = asposewordscloud.models.requests.InsertWatermarkImageRequest(name='Sample.docx', image_file=None, image='Sample.png')
        words_api.insert_watermark_image(insert_request)

    def test_insert_watermark_image_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_image_file = open(os.path.join(documents_dir, 'Common/aspose-cloud.png'), 'rb')
        insert_request = asposewordscloud.models.requests.InsertWatermarkImageOnlineRequest(document=request_document, image_file=request_image_file)
        words_api.insert_watermark_image_online(insert_request)

    def test_insert_watermark_text(self):
        words_api = self.words_api
        request_watermark_text = asposewordscloud.WatermarkText(text='This is the text', rotation_angle=90.0)
        insert_request = asposewordscloud.models.requests.InsertWatermarkTextRequest(name='Sample.docx', watermark_text=request_watermark_text)
        words_api.insert_watermark_text(insert_request)

    def test_insert_watermark_text_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_watermark_text = asposewordscloud.WatermarkText(text='This is the text', rotation_angle=90)
        insert_request = asposewordscloud.models.requests.InsertWatermarkTextOnlineRequest(document=request_document, watermark_text=request_watermark_text)
        words_api.insert_watermark_text_online(insert_request)

    def test_load_web_document(self):
        words_api = self.words_api
        request_data_save_options = asposewordscloud.SaveOptionsData(file_name='google.doc', save_format='doc', dml_effects_rendering_mode='1', dml_rendering_mode='1', update_sdt_content=False, zip_output=False)
        request_data = asposewordscloud.LoadWebDocumentData(loading_document_url='http://google.com', save_options=request_data_save_options)
        load_request = asposewordscloud.models.requests.LoadWebDocumentRequest(data=request_data)
        words_api.load_web_document(load_request)

    def test_move_file(self):
        words_api = self.words_api
        move_request = asposewordscloud.models.requests.MoveFileRequest(dest_path='/TestMoveFileDest_Sample.docx', src_path='Sample.docx')
        words_api.move_file(move_request)

    def test_move_folder(self):
        words_api = self.words_api
        move_request = asposewordscloud.models.requests.MoveFolderRequest(dest_path='/TestMoveFolderDest_Sample', src_path='/TestMoveFolderSrc')
        words_api.move_folder(move_request)

    def test_optimize_document(self):
        words_api = self.words_api
        request_options = asposewordscloud.OptimizationOptions(ms_word_version='Word2002')
        optimize_request = asposewordscloud.models.requests.OptimizeDocumentRequest(name='Sample.docx', options=request_options)
        words_api.optimize_document(optimize_request)

    def test_optimize_document_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_options = asposewordscloud.OptimizationOptions(ms_word_version='Word2002')
        optimize_request = asposewordscloud.models.requests.OptimizeDocumentOnlineRequest(document=request_document, options=request_options)
        words_api.optimize_document_online(optimize_request)

    def test_protect_document(self):
        words_api = self.words_api
        request_protection_request = asposewordscloud.ProtectionRequest(password='123', protection_type='ReadOnly')
        protect_request = asposewordscloud.models.requests.ProtectDocumentRequest(name='Sample.docx', protection_request=request_protection_request)
        words_api.protect_document(protect_request)

    def test_protect_document_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_protection_request = asposewordscloud.ProtectionRequest(new_password='123')
        protect_request = asposewordscloud.models.requests.ProtectDocumentOnlineRequest(document=request_document, protection_request=request_protection_request)
        words_api.protect_document_online(protect_request)

    def test_reject_all_revisions(self):
        words_api = self.words_api
        reject_request = asposewordscloud.models.requests.RejectAllRevisionsRequest(name='Sample.docx')
        words_api.reject_all_revisions(reject_request)

    def test_reject_all_revisions_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        reject_request = asposewordscloud.models.requests.RejectAllRevisionsOnlineRequest(document=request_document)
        words_api.reject_all_revisions_online(reject_request)

    def test_remove_range(self):
        words_api = self.words_api
        remove_request = asposewordscloud.models.requests.RemoveRangeRequest(name='Sample.docx', range_start_identifier='id0.0.0', range_end_identifier='id0.0.1')
        words_api.remove_range(remove_request)

    def test_remove_range_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        remove_request = asposewordscloud.models.requests.RemoveRangeOnlineRequest(document=request_document, range_start_identifier='id0.0.0', range_end_identifier='id0.0.1')
        words_api.remove_range_online(remove_request)

    def test_render_drawing_object(self):
        words_api = self.words_api
        render_request = asposewordscloud.models.requests.RenderDrawingObjectRequest(name='Sample.docx', format='png', index=0)
        words_api.render_drawing_object(render_request)

    def test_render_drawing_object_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        render_request = asposewordscloud.models.requests.RenderDrawingObjectOnlineRequest(document=request_document, format='png', index=0, node_path='sections/0')
        words_api.render_drawing_object_online(render_request)

    def test_render_math_object(self):
        words_api = self.words_api
        render_request = asposewordscloud.models.requests.RenderMathObjectRequest(name='Sample.docx', format='png', index=0)
        words_api.render_math_object(render_request)

    def test_render_math_object_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        render_request = asposewordscloud.models.requests.RenderMathObjectOnlineRequest(document=request_document, format='png', index=0)
        words_api.render_math_object_online(render_request)

    def test_render_page(self):
        words_api = self.words_api
        render_request = asposewordscloud.models.requests.RenderPageRequest(name='Sample.docx', page_index=1, format='bmp')
        words_api.render_page(render_request)

    def test_render_page_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        render_request = asposewordscloud.models.requests.RenderPageOnlineRequest(document=request_document, page_index=1, format='bmp')
        words_api.render_page_online(render_request)

    def test_render_paragraph(self):
        words_api = self.words_api
        render_request = asposewordscloud.models.requests.RenderParagraphRequest(name='Sample.docx', format='png', index=0)
        words_api.render_paragraph(render_request)

    def test_render_paragraph_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        render_request = asposewordscloud.models.requests.RenderParagraphOnlineRequest(document=request_document, format='png', index=0)
        words_api.render_paragraph_online(render_request)

    def test_render_table(self):
        words_api = self.words_api
        render_request = asposewordscloud.models.requests.RenderTableRequest(name='Sample.docx', format='png', index=0)
        words_api.render_table(render_request)

    def test_render_table_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        render_request = asposewordscloud.models.requests.RenderTableOnlineRequest(document=request_document, format='png', index=0)
        words_api.render_table_online(render_request)

    def test_replace_text(self):
        words_api = self.words_api
        request_replace_text = asposewordscloud.ReplaceTextParameters(old_value='Testing', new_value='Aspose testing')
        replace_request = asposewordscloud.models.requests.ReplaceTextRequest(name='Sample.docx', replace_text=request_replace_text)
        words_api.replace_text(replace_request)

    def test_replace_text_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_replace_text = asposewordscloud.ReplaceTextParameters(old_value='aspose', new_value='aspose new')
        replace_request = asposewordscloud.models.requests.ReplaceTextOnlineRequest(document=request_document, replace_text=request_replace_text)
        words_api.replace_text_online(replace_request)

    def test_replace_with_text(self):
        words_api = self.words_api
        request_range_text = asposewordscloud.ReplaceRange(text='Replaced header')
        replace_request = asposewordscloud.models.requests.ReplaceWithTextRequest(name='Sample.docx', range_start_identifier='id0.0.0', range_text=request_range_text, range_end_identifier='id0.0.1')
        words_api.replace_with_text(replace_request)

    def test_replace_with_text_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        request_range_text = asposewordscloud.ReplaceRange(text='Replaced header')
        replace_request = asposewordscloud.models.requests.ReplaceWithTextOnlineRequest(document=request_document, range_start_identifier='id0.0.0', range_text=request_range_text, range_end_identifier='id0.0.1')
        words_api.replace_with_text_online(replace_request)

    def test_reset_cache(self):
        words_api = self.words_api
        reset_request = asposewordscloud.models.requests.ResetCacheRequest()
        words_api.reset_cache(reset_request)

    def test_save_as(self):
        words_api = self.words_api
        request_save_options_data = asposewordscloud.SaveOptionsData(save_format='docx', file_name='/TestSaveAsFromPdfToDoc.docx')
        save_request = asposewordscloud.models.requests.SaveAsRequest(name='Sample.docx', save_options_data=request_save_options_data)
        words_api.save_as(save_request)

    def test_save_as_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Common/test_multi_pages.docx'), 'rb')
        request_save_options_data = asposewordscloud.SaveOptionsData(save_format='pdf', file_name='/TestSaveAs.pdf')
        save_request = asposewordscloud.models.requests.SaveAsOnlineRequest(document=request_document, save_options_data=request_save_options_data)
        words_api.save_as_online(save_request)

    def test_save_as_range(self):
        words_api = self.words_api
        request_document_parameters = asposewordscloud.RangeDocument(document_name='/NewDoc.docx')
        save_request = asposewordscloud.models.requests.SaveAsRangeRequest(name='Sample.docx', range_start_identifier='id0.0.0', document_parameters=request_document_parameters, range_end_identifier='id0.0.1')
        words_api.save_as_range(save_request)

    def test_save_as_range_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        request_document_parameters = asposewordscloud.RangeDocument(document_name='/NewDoc.docx')
        save_request = asposewordscloud.models.requests.SaveAsRangeOnlineRequest(document=request_document, range_start_identifier='id0.0.0', document_parameters=request_document_parameters, range_end_identifier='id0.0.1')
        words_api.save_as_range_online(save_request)

    def test_save_as_tiff(self):
        words_api = self.words_api
        request_save_options = asposewordscloud.TiffSaveOptionsData(save_format='tiff', file_name='/abc.tiff')
        save_request = asposewordscloud.models.requests.SaveAsTiffRequest(name='Sample.docx', save_options=request_save_options)
        words_api.save_as_tiff(save_request)

    def test_save_as_tiff_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Common/test_multi_pages.docx'), 'rb')
        request_save_options = asposewordscloud.TiffSaveOptionsData(save_format='tiff', file_name='/abc.tiff')
        save_request = asposewordscloud.models.requests.SaveAsTiffOnlineRequest(document=request_document, save_options=request_save_options)
        words_api.save_as_tiff_online(save_request)

    def test_search(self):
        words_api = self.words_api
        search_request = asposewordscloud.models.requests.SearchRequest(name='Sample.docx', pattern='aspose')
        words_api.search(search_request)

    def test_search_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        search_request = asposewordscloud.models.requests.SearchOnlineRequest(document=request_document, pattern='aspose')
        words_api.search_online(search_request)

    def test_split_document(self):
        words_api = self.words_api
        split_request = asposewordscloud.models.requests.SplitDocumentRequest(name='Sample.docx', format='text', dest_file_name='/TestSplitDocument.text', _from=1, to=2)
        words_api.split_document(split_request)

    def test_split_document_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        split_request = asposewordscloud.models.requests.SplitDocumentOnlineRequest(document=request_document, format='text', dest_file_name='/TestSplitDocument.text', _from=1, to=2)
        words_api.split_document_online(split_request)

    def test_unprotect_document(self):
        words_api = self.words_api
        request_protection_request = asposewordscloud.ProtectionRequest(password='aspose')
        unprotect_request = asposewordscloud.models.requests.UnprotectDocumentRequest(name='Sample.docx', protection_request=request_protection_request)
        words_api.unprotect_document(unprotect_request)

    def test_unprotect_document_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_protection_request = asposewordscloud.ProtectionRequest(password='aspose')
        unprotect_request = asposewordscloud.models.requests.UnprotectDocumentOnlineRequest(document=request_document, protection_request=request_protection_request)
        words_api.unprotect_document_online(unprotect_request)

    def test_update_bookmark(self):
        words_api = self.words_api
        bookmark_name= 'aspose'

        request_bookmark_data = asposewordscloud.BookmarkData(name=bookmark_name, text='This will be the text for Aspose')
        update_request = asposewordscloud.models.requests.UpdateBookmarkRequest(name='Sample.docx', bookmark_name=bookmark_name, bookmark_data=request_bookmark_data)
        words_api.update_bookmark(update_request)

    def test_update_bookmark_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        bookmark_name= 'aspose'

        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_bookmark_data = asposewordscloud.BookmarkData(name=bookmark_name, text='This will be the text for Aspose')
        update_request = asposewordscloud.models.requests.UpdateBookmarkOnlineRequest(document=request_document, bookmark_name=bookmark_name, bookmark_data=request_bookmark_data, dest_file_name='Sample.docx')
        words_api.update_bookmark_online(update_request)

    def test_update_border(self):
        words_api = self.words_api
        request_border_properties_color = asposewordscloud.XmlColor(web='#AABBCC')
        request_border_properties = asposewordscloud.Border(border_type='Left', color=request_border_properties_color, distance_from_text=6.0, line_style='DashDotStroker', line_width=2.0, shadow=True)
        update_request = asposewordscloud.models.requests.UpdateBorderRequest(name='Sample.docx', border_type='left', border_properties=request_border_properties, node_path='tables/1/rows/0/cells/0')
        words_api.update_border(update_request)

    def test_update_border_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_border_properties_color = asposewordscloud.XmlColor(web='#AABBCC')
        request_border_properties = asposewordscloud.Border(border_type='Left', color=request_border_properties_color, distance_from_text=6, line_style='DashDotStroker', line_width=2, shadow=True)
        update_request = asposewordscloud.models.requests.UpdateBorderOnlineRequest(document=request_document, border_properties=request_border_properties, border_type='left', node_path='tables/1/rows/0/cells/0')
        words_api.update_border_online(update_request)

    def test_update_comment(self):
        words_api = self.words_api
        request_comment_range_start_node = asposewordscloud.NodeLink(node_id='0.3.0')
        request_comment_range_start = asposewordscloud.DocumentPosition(node=request_comment_range_start_node, offset=0)
        request_comment_range_end_node = asposewordscloud.NodeLink(node_id='0.3.0')
        request_comment_range_end = asposewordscloud.DocumentPosition(node=request_comment_range_end_node, offset=0)
        request_comment = asposewordscloud.CommentUpdate(range_start=request_comment_range_start, range_end=request_comment_range_end, initial='IA', author='Imran Anwar', text='A new Comment')
        update_request = asposewordscloud.models.requests.UpdateCommentRequest(name='Sample.docx', comment_index=0, comment=request_comment)
        words_api.update_comment(update_request)

    def test_update_comment_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_comment_range_start_node = asposewordscloud.NodeLink(node_id='0.3.0')
        request_comment_range_start = asposewordscloud.DocumentPosition(node=request_comment_range_start_node, offset=0)
        request_comment_range_end_node = asposewordscloud.NodeLink(node_id='0.3.0')
        request_comment_range_end = asposewordscloud.DocumentPosition(node=request_comment_range_end_node, offset=0)
        request_comment = asposewordscloud.CommentUpdate(range_start=request_comment_range_start, range_end=request_comment_range_end, initial='IA', author='Imran Anwar', text='A new Comment')
        update_request = asposewordscloud.models.requests.UpdateCommentOnlineRequest(document=request_document, comment_index=0, comment=request_comment)
        words_api.update_comment_online(update_request)

    def test_update_custom_xml_part(self):
        words_api = self.words_api
        request_custom_xml_part = asposewordscloud.CustomXmlPartUpdate(data='<data>Hello world</data>')
        update_request = asposewordscloud.models.requests.UpdateCustomXmlPartRequest(name='Sample.docx', custom_xml_part_index=0, custom_xml_part=request_custom_xml_part)
        words_api.update_custom_xml_part(update_request)

    def test_update_custom_xml_part_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_custom_xml_part = asposewordscloud.CustomXmlPartUpdate(data='<data>Hello world</data>')
        update_request = asposewordscloud.models.requests.UpdateCustomXmlPartOnlineRequest(document=request_document, custom_xml_part_index=0, custom_xml_part=request_custom_xml_part)
        words_api.update_custom_xml_part_online(update_request)

    def test_update_drawing_object(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_drawing_object = asposewordscloud.DrawingObjectUpdate(left=0)
        request_image_file = open(os.path.join(documents_dir, 'Common/aspose-cloud.png'), 'rb')
        update_request = asposewordscloud.models.requests.UpdateDrawingObjectRequest(name='Sample.docx', drawing_object=request_drawing_object, image_file=request_image_file, index=0)
        words_api.update_drawing_object(update_request)

    def test_update_drawing_object_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_drawing_object = asposewordscloud.DrawingObjectUpdate(left=0)
        request_image_file = open(os.path.join(documents_dir, 'Common/aspose-cloud.png'), 'rb')
        update_request = asposewordscloud.models.requests.UpdateDrawingObjectOnlineRequest(document=request_document, drawing_object=request_drawing_object, image_file=request_image_file, index=0)
        words_api.update_drawing_object_online(update_request)

    def test_update_field(self):
        words_api = self.words_api
        request_field = asposewordscloud.FieldUpdate(field_code='{ NUMPAGES }')
        update_request = asposewordscloud.models.requests.UpdateFieldRequest(name='Sample.docx', index=0, field=request_field, node_path='sections/0/paragraphs/0')
        words_api.update_field(update_request)

    def test_update_field_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_field = asposewordscloud.FieldUpdate(field_code='{ NUMPAGES }')
        update_request = asposewordscloud.models.requests.UpdateFieldOnlineRequest(document=request_document, field=request_field, index=0, node_path='sections/0/paragraphs/0')
        words_api.update_field_online(update_request)

    def test_update_fields(self):
        words_api = self.words_api
        update_request = asposewordscloud.models.requests.UpdateFieldsRequest(name='Sample.docx')
        words_api.update_fields(update_request)

    def test_update_fields_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        update_request = asposewordscloud.models.requests.UpdateFieldsOnlineRequest(document=request_document)
        words_api.update_fields_online(update_request)

    def test_update_footnote(self):
        words_api = self.words_api
        request_footnote_dto = asposewordscloud.FootnoteUpdate(text='new text is here')
        update_request = asposewordscloud.models.requests.UpdateFootnoteRequest(name='Sample.docx', index=0, footnote_dto=request_footnote_dto)
        words_api.update_footnote(update_request)

    def test_update_footnote_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        request_footnote_dto = asposewordscloud.FootnoteUpdate(text='new text is here')
        update_request = asposewordscloud.models.requests.UpdateFootnoteOnlineRequest(document=request_document, footnote_dto=request_footnote_dto, index=0)
        words_api.update_footnote_online(update_request)

    def test_update_form_field(self):
        words_api = self.words_api
        request_form_field = asposewordscloud.FormFieldTextInput(name='FullName', enabled=True, calculate_on_exit=True, status_text='', text_input_type='Regular', text_input_default='No name')
        update_request = asposewordscloud.models.requests.UpdateFormFieldRequest(name='Sample.docx', index=0, form_field=request_form_field)
        words_api.update_form_field(update_request)

    def test_update_form_field_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_form_field = asposewordscloud.FormFieldTextInput(name='FullName', enabled=True, calculate_on_exit=True, status_text='', text_input_type='Regular', text_input_default='No name')
        update_request = asposewordscloud.models.requests.UpdateFormFieldOnlineRequest(document=request_document, form_field=request_form_field, index=0, node_path='sections/0')
        words_api.update_form_field_online(update_request)

    def test_update_list(self):
        words_api = self.words_api
        request_list_update = asposewordscloud.ListUpdate(is_restart_at_each_section=True)
        update_request = asposewordscloud.models.requests.UpdateListRequest(name='TestGetLists.doc', list_id=1, list_update=request_list_update)
        words_api.update_list(update_request)

    def test_update_list_level(self):
        words_api = self.words_api
        request_list_update = asposewordscloud.ListLevelUpdate(alignment='Right')
        update_request = asposewordscloud.models.requests.UpdateListLevelRequest(name='TestGetLists.doc', list_id=1, list_level=1, list_update=request_list_update)
        words_api.update_list_level(update_request)

    def test_update_list_level_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        request_list_update = asposewordscloud.ListLevelUpdate(alignment='Right')
        update_request = asposewordscloud.models.requests.UpdateListLevelOnlineRequest(document=request_document, list_id=1, list_update=request_list_update, list_level=1)
        words_api.update_list_level_online(update_request)

    def test_update_list_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        request_list_update = asposewordscloud.ListUpdate(is_restart_at_each_section=True)
        update_request = asposewordscloud.models.requests.UpdateListOnlineRequest(document=request_document, list_id=1, list_update=request_list_update)
        words_api.update_list_online(update_request)

    def test_update_paragraph_format(self):
        words_api = self.words_api
        request_paragraph_format_dto = asposewordscloud.ParagraphFormatUpdate(alignment='Right')
        update_request = asposewordscloud.models.requests.UpdateParagraphFormatRequest(name='Sample.docx', index=0, paragraph_format_dto=request_paragraph_format_dto)
        words_api.update_paragraph_format(update_request)

    def test_update_paragraph_format_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_paragraph_format_dto = asposewordscloud.ParagraphFormatUpdate(alignment='Right')
        update_request = asposewordscloud.models.requests.UpdateParagraphFormatOnlineRequest(document=request_document, paragraph_format_dto=request_paragraph_format_dto, index=0)
        words_api.update_paragraph_format_online(update_request)

    def test_update_paragraph_list_format(self):
        words_api = self.words_api
        request_list_format_dto = asposewordscloud.ListFormatUpdate(list_id=2)
        update_request = asposewordscloud.models.requests.UpdateParagraphListFormatRequest(name='Sample.docx', index=0, list_format_dto=request_list_format_dto)
        words_api.update_paragraph_list_format(update_request)

    def test_update_paragraph_list_format_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        request_list_format_dto = asposewordscloud.ListFormatUpdate(list_id=2)
        update_request = asposewordscloud.models.requests.UpdateParagraphListFormatOnlineRequest(document=request_document, list_format_dto=request_list_format_dto, index=0)
        words_api.update_paragraph_list_format_online(update_request)

    def test_update_run(self):
        words_api = self.words_api
        request_run = asposewordscloud.RunUpdate(text='run with text')
        update_request = asposewordscloud.models.requests.UpdateRunRequest(name='Sample.docx', paragraph_path='paragraphs/1', index=0, run=request_run)
        words_api.update_run(update_request)

    def test_update_run_font(self):
        words_api = self.words_api
        request_font_dto = asposewordscloud.Font(bold=True)
        update_request = asposewordscloud.models.requests.UpdateRunFontRequest(name='Sample.docx', paragraph_path='paragraphs/0', index=0, font_dto=request_font_dto)
        words_api.update_run_font(update_request)

    def test_update_run_font_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_font_dto = asposewordscloud.Font(bold=True)
        update_request = asposewordscloud.models.requests.UpdateRunFontOnlineRequest(document=request_document, paragraph_path='paragraphs/0', font_dto=request_font_dto, index=0)
        words_api.update_run_font_online(update_request)

    def test_update_run_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb')
        request_run = asposewordscloud.RunUpdate(text='run with text')
        update_request = asposewordscloud.models.requests.UpdateRunOnlineRequest(document=request_document, paragraph_path='paragraphs/1', run=request_run, index=0)
        words_api.update_run_online(update_request)

    def test_update_section_page_setup(self):
        words_api = self.words_api
        request_page_setup = asposewordscloud.PageSetup(rtl_gutter=True, left_margin=10.0, orientation='Landscape', paper_size='A5')
        update_request = asposewordscloud.models.requests.UpdateSectionPageSetupRequest(name='Sample.docx', section_index=0, page_setup=request_page_setup)
        words_api.update_section_page_setup(update_request)

    def test_update_section_page_setup_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_page_setup = asposewordscloud.PageSetup(rtl_gutter=True, left_margin=10, orientation='Landscape', paper_size='A5')
        update_request = asposewordscloud.models.requests.UpdateSectionPageSetupOnlineRequest(document=request_document, section_index=0, page_setup=request_page_setup)
        words_api.update_section_page_setup_online(update_request)

    def test_update_style(self):
        words_api = self.words_api
        request_style_update = asposewordscloud.StyleUpdate(name='My Style')
        update_request = asposewordscloud.models.requests.UpdateStyleRequest(name='Sample.docx', style_name='Heading 1', style_update=request_style_update)
        words_api.update_style(update_request)

    def test_update_style_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_style_update = asposewordscloud.StyleUpdate(name='My Style')
        update_request = asposewordscloud.models.requests.UpdateStyleOnlineRequest(document=request_document, style_name='Heading 1', style_update=request_style_update)
        words_api.update_style_online(update_request)

    def test_update_table_cell_format(self):
        words_api = self.words_api
        request_format = asposewordscloud.TableCellFormat(bottom_padding=5.0, fit_text=True, horizontal_merge='First', wrap_text=True)
        update_request = asposewordscloud.models.requests.UpdateTableCellFormatRequest(name='Sample.docx', table_row_path='sections/0/tables/2/rows/0', index=0, format=request_format)
        words_api.update_table_cell_format(update_request)

    def test_update_table_cell_format_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_format = asposewordscloud.TableCellFormat(bottom_padding=5, fit_text=True, horizontal_merge='First', wrap_text=True)
        update_request = asposewordscloud.models.requests.UpdateTableCellFormatOnlineRequest(document=request_document, table_row_path='sections/0/tables/2/rows/0', format=request_format, index=0)
        words_api.update_table_cell_format_online(update_request)

    def test_update_table_properties(self):
        words_api = self.words_api
        request_properties = asposewordscloud.TableProperties(alignment='Right', allow_auto_fit=False, bidi=True, bottom_padding=1.0, cell_spacing=2.0, style_options='ColumnBands')
        update_request = asposewordscloud.models.requests.UpdateTablePropertiesRequest(name='Sample.docx', index=1, properties=request_properties)
        words_api.update_table_properties(update_request)

    def test_update_table_properties_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_properties = asposewordscloud.TableProperties(alignment='Right', allow_auto_fit=False, bidi=True, bottom_padding=1, cell_spacing=2, style_options='ColumnBands')
        update_request = asposewordscloud.models.requests.UpdateTablePropertiesOnlineRequest(document=request_document, properties=request_properties, index=1)
        words_api.update_table_properties_online(update_request)

    def test_update_table_row_format(self):
        words_api = self.words_api
        request_format = asposewordscloud.TableRowFormat(allow_break_across_pages=True, heading_format=True, height=10.0, height_rule='Exactly')
        update_request = asposewordscloud.models.requests.UpdateTableRowFormatRequest(name='Sample.docx', table_path='sections/0/tables/2', index=0, format=request_format)
        words_api.update_table_row_format(update_request)

    def test_update_table_row_format_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        request_format = asposewordscloud.TableRowFormat(allow_break_across_pages=True, heading_format=True, height=10, height_rule='Auto')
        update_request = asposewordscloud.models.requests.UpdateTableRowFormatOnlineRequest(document=request_document, table_path='sections/0/tables/2', format=request_format, index=0)
        words_api.update_table_row_format_online(update_request)

    def test_upload_file(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        request_file_content = open(os.path.join(documents_dir, 'Sample.docx'), 'rb')
        upload_request = asposewordscloud.models.requests.UploadFileRequest(file_content=request_file_content, path='Sample.docx')
        words_api.upload_file(upload_request)