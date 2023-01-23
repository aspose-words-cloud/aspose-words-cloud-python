# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_readme.py">
#   Copyright (c) 2023 Aspose.Words for Cloud
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
import re

import asposewordscloud.models.requests
from test.base_test_context import BaseTestContext


class TestReadme(BaseTestContext):

    def test_readme_code(self):
        creds = self.read_config()

        client_secret = creds["ClientSecret"]
        client_id = creds["ClientId"]
        base_url = creds["BaseUrl"]

        local_folder = self.local_common_folder
        filename = "test_multi_pages.docx"

        remote_name = 'TestDeleteDocumentWatermark.docx'
        remote_folder = 'FolderWhereFileLocates'

        # Start README example

        self.words_api = asposewordscloud.WordsApi(client_id, client_secret, base_url)

        upload_request = asposewordscloud.models.requests.UploadFileRequest(
            open(os.path.join(local_folder, filename), 'rb'), os.path.join(remote_folder, remote_name))
        self.words_api.upload_file(upload_request)

        request = asposewordscloud.models.requests.DeleteWatermarkRequest(remote_name, remote_folder)
        self.words_api.delete_watermark(request)

        # End README example

        self.write_to_readme()

    def write_to_readme(self):
        # set regex patterns
        start_pattern = r"^\s*# Start README example\s*$"
        end_pattern = r"^\s*# End README example\s*$"

        # set paths
        source_path = __file__
        readme_path = os.path.dirname(__file__) + "/../README.md"

        # read code from the file
        with open(source_path) as f:
            code_lines = f.readlines()

        # extract readme code
        readme_code = list()
        skip_mode = True
        for line in code_lines:
            if skip_mode:
                skip_mode = (re.match(start_pattern, line) is None)

            if not skip_mode:
                readme_code.append(line)
                skip_mode = not (re.match(end_pattern, line) is None)

        self.assertGreater(len(readme_code), 2)

        # read readme file
        with open(readme_path) as f:
            readme_lines = f.readlines()

        # replace code
        new_readme_lines = list()
        code_mode = False
        for line in readme_lines:
            if not code_mode:
                code_mode = not (re.match(start_pattern, line) is None)

                if code_mode:
                    new_readme_lines.extend(readme_code)

            if code_mode:
                code_mode = re.match(end_pattern, line) is None
                continue

            if not code_mode:
                new_readme_lines.append(line)

        # write to readm
        with open(readme_path, 'w') as f:
            for line in new_readme_lines:
                f.write(line)
