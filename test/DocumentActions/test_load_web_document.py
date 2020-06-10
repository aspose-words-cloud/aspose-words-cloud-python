#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_load_web_document.py">
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

import asposewordscloud.models.requests
from test.base_test_context import BaseTestContext


class TestLoadWebDocument(BaseTestContext):
    test_folder = 'DocumentActions/LoadWebDocument'

    #
    # Test for loading web document
    #
    def test_load_web_document(self):
        save_options = asposewordscloud.SaveOptionsData(save_format='doc', file_name='google.doc', dml_rendering_mode='1', dml_effects_rendering_mode='1', zip_output=False, update_last_saved_time_property=False)
        body = asposewordscloud.LoadWebDocumentData(loading_document_url='http://google.com', save_options=save_options)
        request = asposewordscloud.models.requests.LoadWebDocumentRequest(body)
        result = self.words_api.load_web_document(request)
        self.assertIsNotNone(result, 'Error has occurred while load document')
