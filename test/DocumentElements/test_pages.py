#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_pages.py">
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


class TestPages(BaseTestContext):
    test_folder = 'DocumentElements/Pages'

    #
    # Test for page rendering
    #
    def test_render_page(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestRenderPage.docx'
        page_number = 1
        format = 'png'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.RenderPageRequest(remote_name, page_number, format,
                                                                     os.path.join(
                                                                         self.remote_test_folder,
                                                                         self.test_folder))
        result = self.words_api.render_page(request)
        self.assertIsNotNone(result, 'Error has occurred while render page')

    #
    # Test for getting page setup
    #
    def test_get_section_page_setup(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetSectionPageSetup.docx'
        index = 0

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetSectionPageSetupRequest(remote_name, index,
                                                                              os.path.join(
                                                                                  self.remote_test_folder,
                                                                                  self.test_folder))
        result = self.words_api.get_section_page_setup(request)
        self.assertIsNotNone(result, 'Error has occurred while get section page setup')

    #
    # Test for updating page setup
    #
    def test_update_section_page_setup(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestUpdateSectionPageSetup.docx'
        index = 0
        body = asposewordscloud.PageSetup(rtl_gutter=True, left_margin=10, orientation='Landscape', paper_size='A5')

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.UpdateSectionPageSetupRequest(remote_name, index, body,
                                                                                 os.path.join(
                                                                                     self.remote_test_folder,
                                                                                     self.test_folder))
        result = self.words_api.update_section_page_setup(request)
        self.assertIsNotNone(result, 'Error has occurred while update section page setup')
