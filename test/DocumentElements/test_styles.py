#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_styles.py">
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


class TestStyles(BaseTestContext):
    test_folder = 'DocumentElements/Styles'
    local_name = 'GetStyles.docx'

    def test_get_styles(self):
        remote_name = 'TestGetStyles.docx'
        self.upload_file(os.path.join(self.remote_test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, self.local_name), 'rb'))
        request = asposewordscloud.models.requests.GetStylesRequest(remote_name, self.remote_test_folder)
        _ = self.words_api.get_styles(request)

    def test_get_style(self):
        remote_name = 'TestGetStyle.docx'
        self.upload_file(os.path.join(self.remote_test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, self.local_name), 'rb'))
        request = asposewordscloud.models.requests.GetStyleRequest(remote_name, "Heading 1", self.remote_test_folder)
        _ = self.words_api.get_style(request)

    def test_update_style(self):
        remote_name = 'TestUpdateStyle.docx'
        self.upload_file(os.path.join(self.remote_test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, self.local_name), 'rb'))
        data = asposewordscloud.models.StyleUpdate()
        data.name = "My Style"
        request = asposewordscloud.models.requests.UpdateStyleRequest(remote_name, data, "Heading 1", self.remote_test_folder)
        _ = self.words_api.update_style(request)

    def test_insert_style(self):
        remote_name = 'TestInsertStyle.docx'
        self.upload_file(os.path.join(self.remote_test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, self.local_name), 'rb'))
        data = asposewordscloud.models.StyleInsert("My Style", "Paragraph")
        request = asposewordscloud.models.requests.InsertStyleRequest(remote_name, data, self.remote_test_folder)
        _ = self.words_api.insert_style(request)

    def test_copy_style(self):
        remote_name = 'TestCopyStyle.docx'
        self.upload_file(os.path.join(self.remote_test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, self.local_name), 'rb'))
        data = asposewordscloud.models.StyleCopy("Heading 1")
        request = asposewordscloud.models.requests.CopyStyleRequest(remote_name, data, self.remote_test_folder)
        _ = self.words_api.copy_style(request)

    def test_get_style_from_document_element(self):
        remote_name = 'TestGetStyleFromDocumentElement.docx'
        self.upload_file(os.path.join(self.remote_test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, self.local_name), 'rb'))
        request = asposewordscloud.models.requests.GetStyleFromDocumentElementRequest(remote_name, "paragraphs/1/paragraphFormat", self.remote_test_folder)
        _ = self.words_api.get_style_from_document_element(request)

    def test_apply_style_to_document_element(self):
        remote_name = 'TestApplyStyleToDocumentElement.docx'
        self.upload_file(os.path.join(self.remote_test_folder, remote_name), open(os.path.join(self.local_test_folder, self.test_folder, self.local_name), 'rb'))
        data = asposewordscloud.models.StyleApply("Heading 1")
        request = asposewordscloud.models.requests.ApplyStyleToDocumentElementRequest(remote_name, data, "paragraphs/1/paragraphFormat", self.remote_test_folder)
        _ = self.words_api.apply_style_to_document_element(request)

