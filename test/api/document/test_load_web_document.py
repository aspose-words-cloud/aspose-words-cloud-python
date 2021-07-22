# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_load_web_document.py">
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
# Example of how to load web document.
#
class TestLoadWebDocument(BaseTestContext):
    #
    # Test for loading web document.
    #
    def test_load_web_document(self):
        data_save_options = asposewordscloud.SaveOptionsData(file_name = 'google.doc', save_format = 'doc', dml_effects_rendering_mode = '1', dml_rendering_mode = '1', update_sdt_content = False, zip_output = False)
        data = asposewordscloud.LoadWebDocumentData(loading_document_url = 'http://google.com', save_options = data_save_options)
        request = asposewordscloud.models.requests.LoadWebDocumentRequest(data = data)

        result = self.words_api.load_web_document(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.save_result, 'Validate LoadWebDocument response')
        self.assertIsNotNone(result.save_result.dest_document, 'Validate LoadWebDocument response')
        self.assertEqual('google.doc', result.save_result.dest_document.href)
