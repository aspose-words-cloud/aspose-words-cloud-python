#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_sections.py">
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


class TestSections(BaseTestContext):
    test_folder = 'DocumentElements/Sections'

    #
    # Test for getting section
    #
    def test_get_section(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetSection.docx'
        index = 0

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetSectionRequest(remote_name, index,
                                                                     os.path.join(
                                                                         self.remote_test_folder,
                                                                         self.test_folder))
        result = self.words_api.get_section(request)
        self.assertIsNotNone(result, 'Error has occurred while get section')

    #
    # Test for getting section
    #
    def test_get_sections(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetSections.docx'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))
        request = asposewordscloud.models.requests.GetSectionsRequest(remote_name,
                                                                      os.path.join(
                                                                          self.remote_test_folder,
                                                                          self.test_folder))
        result = self.words_api.get_sections(request)
        self.assertIsNotNone(result, 'Error has occurred while get sections')

    def test_delete_section(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestDeleteSection.docx'

        self.upload_file(os.path.join(self.remote_test_folder, self.test_folder, remote_name), open(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb'))

        request = asposewordscloud.models.requests.DeleteSectionRequest(remote_name, 0, os.path.join(self.remote_test_folder, self.test_folder))
        result = self.words_api.delete_section(request)
