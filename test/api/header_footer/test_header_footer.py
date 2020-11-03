# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_header_footer.py">
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
# Example of how to work with headers and footers.
#
class TestHeaderFooter(BaseTestContext):
    #
    # Test for getting headers and footers.
    #
    def test_get_header_footers(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/HeaderFooters'
        localFile = 'DocumentElements/HeaderFooters/HeadersFooters.doc'
        remoteFileName = 'TestGetHeadersFooters.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetHeaderFootersRequest(name=remoteFileName, section_path='', folder=remoteDataFolder)

        result = self.words_api.get_header_footers(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.header_footers, 'Validate GetHeaderFooters response')
        self.assertIsNotNone(result.header_footers.list, 'Validate GetHeaderFooters response')
        self.assertEqual(6, len(result.header_footers.list))

    #
    # Test for getting headerfooter.
    #
    def test_get_header_footer(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/HeaderFooters'
        localFile = 'DocumentElements/HeaderFooters/HeadersFooters.doc'
        remoteFileName = 'TestGetHeaderFooter.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetHeaderFooterRequest(name=remoteFileName, header_footer_index=0, folder=remoteDataFolder)

        result = self.words_api.get_header_footer(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.header_footer, 'Validate GetHeaderFooter response')
        self.assertIsNotNone(result.header_footer.child_nodes, 'Validate GetHeaderFooter response')
        self.assertEqual(1, len(result.header_footer.child_nodes))
        self.assertEqual('0.0.0', result.header_footer.child_nodes[0].node_id)

    #
    # Test for getting headerfooter of section.
    #
    def test_get_header_footer_of_section(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/HeaderFooters'
        localFile = 'DocumentElements/HeaderFooters/HeadersFooters.doc'
        remoteFileName = 'TestGetHeaderFooterOfSection.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetHeaderFooterOfSectionRequest(name=remoteFileName, header_footer_index=0, section_index=0, folder=remoteDataFolder)

        result = self.words_api.get_header_footer_of_section(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.header_footer, 'Validate GetHeaderFooterOfSection response')
        self.assertIsNotNone(result.header_footer.child_nodes, 'Validate GetHeaderFooterOfSection response')
        self.assertEqual(1, len(result.header_footer.child_nodes))
        self.assertEqual('0.0.0', result.header_footer.child_nodes[0].node_id)

    #
    # Test for deleting headerfooter.
    #
    def test_delete_header_footer(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/HeaderFooters'
        localFile = 'DocumentElements/HeaderFooters/HeadersFooters.doc'
        remoteFileName = 'TestDeleteHeaderFooter.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteHeaderFooterRequest(name=remoteFileName, section_path='', index=0, folder=remoteDataFolder)

        self.words_api.delete_header_footer(request)


    #
    # Test for deleting headerfooters.
    #
    def test_delete_headers_footers(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/HeaderFooters'
        localFile = 'DocumentElements/HeaderFooters/HeadersFooters.doc'
        remoteFileName = 'TestDeleteHeadersFooters.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteHeadersFootersRequest(name=remoteFileName, section_path='', folder=remoteDataFolder)

        self.words_api.delete_headers_footers(request)


    #
    # Test for adding headerfooters.
    #
    def test_insert_header_footer(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/HeaderFooters'
        localFile = 'DocumentElements/HeaderFooters/HeadersFooters.doc'
        remoteFileName = 'TestInsertHeaderFooter.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.InsertHeaderFooterRequest(name=remoteFileName, header_footer_type='FooterEven', section_path='', folder=remoteDataFolder)

        result = self.words_api.insert_header_footer(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.header_footer, 'Validate InsertHeaderFooter response')
        self.assertIsNotNone(result.header_footer.child_nodes, 'Validate InsertHeaderFooter response')
        self.assertEqual(1, len(result.header_footer.child_nodes))
        self.assertEqual('0.2.0', result.header_footer.child_nodes[0].node_id)
