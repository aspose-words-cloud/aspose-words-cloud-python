# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_section.py">
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
import dateutil.parser
import asposewordscloud.models.requests
from test.base_test_context import BaseTestContext

#
# Example of how to work with sections.
#
class TestSection(BaseTestContext):
    #
    # Test for getting section by index.
    #
    def test_get_section(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Section'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetSection.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetSectionRequest(name = remoteFileName, section_index = 0, folder = remoteDataFolder)

        result = self.words_api.get_section(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.section, 'Validate GetSection response')
        self.assertIsNotNone(result.section.child_nodes, 'Validate GetSection response')
        self.assertEqual(13, len(result.section.child_nodes))
        self.assertEqual('0.3.0', result.section.child_nodes[0].node_id)

    #
    # Test for getting section by index online.
    #
    def test_get_section_online(self):
        localFile = 'Common/test_multi_pages.docx'

        request = asposewordscloud.models.requests.GetSectionOnlineRequest(document = open(os.path.join(self.local_test_folder, localFile), 'rb'), section_index = 0)

        result = self.words_api.get_section_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting sections.
    #
    def test_get_sections(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Section'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetSections.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetSectionsRequest(name = remoteFileName, folder = remoteDataFolder)

        result = self.words_api.get_sections(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.sections, 'Validate GetSections response')
        self.assertIsNotNone(result.sections.section_link_list, 'Validate GetSections response')
        self.assertEqual(1, len(result.sections.section_link_list))
        self.assertEqual('0', result.sections.section_link_list[0].node_id)

    #
    # Test for getting sections online.
    #
    def test_get_sections_online(self):
        localFile = 'Common/test_multi_pages.docx'

        request = asposewordscloud.models.requests.GetSectionsOnlineRequest(document = open(os.path.join(self.local_test_folder, localFile), 'rb'))

        result = self.words_api.get_sections_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for delete a section.
    #
    def test_delete_section(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Section'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestDeleteSection.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.DeleteSectionRequest(name = remoteFileName, section_index = 0, folder = remoteDataFolder)

        self.words_api.delete_section(request)


    #
    # Test for delete a section online.
    #
    def test_delete_section_online(self):
        localFile = 'Common/test_multi_pages.docx'

        request = asposewordscloud.models.requests.DeleteSectionOnlineRequest(document = open(os.path.join(self.local_test_folder, localFile), 'rb'), section_index = 0)

        result = self.words_api.delete_section_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

