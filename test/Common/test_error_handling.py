#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_error_handling.py">
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
from asposewordscloud.rest import ApiException


class TestErrorHandling(BaseTestContext):

    #
    # Test for checking handle of server errors
    #
    def test_handle_server_errors(self):
        remote_name = 'noFileWithThisName.docx'
        request = asposewordscloud.models.requests.GetSectionRequest(remote_name, '')
        try:
            self.words_api.get_section(request)
            self.assertRaises(ApiException)
        except ApiException as e:
            self.assertTrue(e.status == 404, 'Error while testing handle server error')
            self.assertTrue(e.body.error.message.startswith("Error while loading file 'noFileWithThisName.docx' from storage:"), "Current message: " + e.body.error.message)
            self.assertNotEqual(e.body.error.inner_error, None, "Inner Error must be set")
