# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_page_setup.py">
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
# Example of how to work with macros.
#
class TestPageSetup(BaseTestContext):
    #
    # Test for getting page settings.
    #
    def test_get_section_page_setup(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/PageSetup'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetSectionPageSetup.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetSectionPageSetupRequest(name=remoteFileName, section_index=0, folder=remoteDataFolder)

        result = self.words_api.get_section_page_setup(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating page settings.
    #
    def test_update_section_page_setup(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/PageSetup'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestUpdateSectionPageSetup.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestPageSetup = asposewordscloud.PageSetup(rtl_gutter=True, left_margin=10, orientation='Landscape', paper_size='A5')
        request = asposewordscloud.models.requests.UpdateSectionPageSetupRequest(name=remoteFileName, section_index=0, page_setup=requestPageSetup, folder=remoteDataFolder)

        result = self.words_api.update_section_page_setup(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for page rendering.
    #
    def test_get_render_page(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/PageSetup'
        localTextFile = 'DocumentElements/Text/SampleWordDocument.docx'
        remoteFileName = 'TestGetRenderPage.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localTextFile), 'rb'))

        request = asposewordscloud.models.requests.RenderPageRequest(name=remoteFileName, page_index=1, format='bmp', folder=remoteDataFolder)

        result = self.words_api.render_page(request)
        self.assertIsNotNone(result, 'Error has occurred.')

