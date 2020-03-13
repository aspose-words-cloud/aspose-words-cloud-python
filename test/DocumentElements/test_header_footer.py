#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_header_footer.py">
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


class TestHeaderFooter(BaseTestContext):
    test_folder = 'DocumentElements/HeaderFooters'

    #
    #  Test for inserting header or footer
    #
    def test_insert_header_footer(self):
        filename = 'HeadersFooters.doc'
        remote_name = 'TestPutHeaderFooter.doc'
        footer_type = "FooterEven"

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.InsertHeaderFooterRequest(remote_name, footer_type, "",
                                                                        os.path.join(
                                                                            self.remote_test_folder,
                                                                            self.test_folder))
        result = self.words_api.insert_header_footer(request)
        self.assertIsNotNone(result, 'Error has occurred while insert header footer')

    #
    #  Test for getting header or footer
    #
    def test_get_header_footer(self):
        filename = 'HeadersFooters.doc'
        remote_name = 'TestGetHeaderFooter.doc'
        index = 0

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetHeaderFooterRequest(remote_name, index,
                                                                          os.path.join(
                                                                              self.remote_test_folder,
                                                                              self.test_folder))
        result = self.words_api.get_header_footer(request)
        self.assertIsNotNone(result, 'Error has occurred while get header footer')

    #
    #  Test for getting headers or footers
    #
    def test_get_header_footers(self):
        filename = 'HeadersFooters.doc'
        remote_name = 'TestGetHeaderFooters.doc'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetHeaderFootersRequest(remote_name, '',
                                                                         os.path.join(
                                                                             self.remote_test_folder,
                                                                             self.test_folder))
        result = self.words_api.get_header_footers(request)
        self.assertIsNotNone(result, 'Error has occurred while get headers footers')

    #
    # Test for getting section headers/footers
    #
    def test_get_header_footer_of_section(self):
        filename = 'HeadersFooters.doc'
        remote_name = 'TestGetHeaderFooterOfSection.doc'
        index = 0
        section_index = 0

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetHeaderFooterOfSectionRequest(remote_name, index, section_index,
                                                                                   os.path.join(
                                                                                       self.remote_test_folder,
                                                                                       self.test_folder))
        result = self.words_api.get_header_footer_of_section(request)
        self.assertIsNotNone(result, 'Error has occurred while get header footer of section')

    #
    #  Test for removing header/footer
    #
    def test_delete_header_footer(self):
        filename = 'HeadersFooters.doc'
        remote_name = 'TestDeleteHeaderFooter.doc'
        index = 0
        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.DeleteHeaderFooterRequest(remote_name, '', index,
                                                                           os.path.join(
                                                                               self.remote_test_folder,
                                                                               self.test_folder))
        result = self.words_api.delete_header_footer(request)
        self.assertIsNotNone(result, 'Error has occurred while delete header footer')

    #
    #  Test for removing headers/footers
    #
    def test_delete_headers_footers(self):
        filename = 'HeadersFooters.doc'
        remote_name = 'TestDeleteHeadersFooters.doc'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.DeleteHeadersFootersRequest(remote_name, '',
                                                                             os.path.join(
                                                                                 self.remote_test_folder,
                                                                                 self.test_folder))
        result = self.words_api.delete_headers_footers(request)
        self.assertIsNotNone(result, 'Error has occurred while delete headers footers')
