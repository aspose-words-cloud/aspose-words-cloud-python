# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_font.py">
#   Copyright (c) 2025 Aspose.Words for Cloud
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
# Example of how to work with font.
#
class TestFont(BaseTestContext):
    #
    # Test for reseting cache.
    #
    def test_reset_cache(self):
        request = asposewordscloud.models.requests.ResetCacheRequest()

        self.words_api.reset_cache(request)


    #
    # Test for GetAvailableFonts resource.
    #
    def test_get_available_fonts(self):
        request = asposewordscloud.models.requests.GetAvailableFontsRequest()

        result = self.words_api.get_available_fonts(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.system_fonts, 'Validate GetAvailableFonts response')
