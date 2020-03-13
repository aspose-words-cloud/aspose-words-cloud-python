#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_range.py">
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


class TestRange(BaseTestContext):
    test_folder = 'DocumentElements/Range'

    def test_get_range_text(self):
        range_start = 'id0.0.0'
        range_end = 'id0.0.1'
        expected_text = 'This is HEADER '

        local_name = 'RangeGet.doc'
        remote_name = 'TestGetRangeText.doc'

        self.upload_file(os.path.join(self.remote_test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, local_name), 'rb'))

        request = asposewordscloud.models.requests.GetRangeTextRequest(remote_name, range_start, range_end, self.remote_test_folder)
        result = self.words_api.get_range_text(request)
        self.assertEqual(expected_text, result.text)

    def test_remove_range(self):
        range_start = 'id0.0.0'
        range_end = 'id0.0.1'

        local_name = 'RangeGet.doc'
        remote_name = 'TestRemoveRange.doc'

        self.upload_file(os.path.join(self.remote_test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, local_name), 'rb'))

        request = asposewordscloud.models.requests.RemoveRangeRequest(remote_name, range_start, range_end, self.remote_test_folder)
        result = self.words_api.remove_range(request)
        self.assertIsNotNone(result)

    def test_save_as_range(self):
        range_start = 'id0.0.0'
        range_end = 'id0.0.1'
        new_doc_name = os.path.join(self.remote_test_folder, 'NewDoc.docx')
        range_doc = asposewordscloud.models.RangeDocument(new_doc_name)

        local_name = 'RangeGet.doc'
        remote_name = 'TestSaveAsRange.doc'

        self.upload_file(os.path.join(self.remote_test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, local_name), 'rb'))

        request = asposewordscloud.models.requests.SaveAsRangeRequest(remote_name, range_start, range_doc, range_end, self.remote_test_folder)
        result = self.words_api.save_as_range(request)
        self.assertIsNotNone(result)

    def test_replace_with_text(self):
        range_start = 'id0.0.0'
        range_end = 'id0.0.1'
        new_text = 'Replace header'
        replacement = asposewordscloud.models.ReplaceRange(new_text)

        local_name = 'RangeGet.doc'
        remote_name = 'TestReplaceWithText.doc'

        self.upload_file(os.path.join(self.remote_test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, local_name), 'rb'))

        request = asposewordscloud.models.requests.ReplaceWithTextRequest(remote_name, range_start, replacement, range_end, self.remote_test_folder)
        result = self.words_api.replace_with_text(request)
        self.assertIsNotNone(result)
