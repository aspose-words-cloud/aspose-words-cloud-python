#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_lists.py">
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
import re
from test.base_test_context import BaseTestContext
from pathlib import Path

class TestReadme(BaseTestContext):

    def test_readme_code(self):
        creds = self.read_config()

        apiKey = creds["AppKey"]
        apiSid = creds["AppSid"]
        baseUrl = creds["BaseUrl"]

        local_folder = self.local_common_folder
        filename = "test_multi_pages.docx"

        remote_name = 'TestDeleteDocumentWatermark.docx'
        remote_folder = 'FolderWhereFileLocates'

        # Start README example

        words_api = asposewordscloud.WordsApi(apiSid, apiKey, baseUrl)

        upload_request = asposewordscloud.models.requests.UploadFileRequest(open(os.path.join(local_folder, filename), 'rb'), os.path.join(remote_folder, remote_name))
        self.words_api.upload_file(upload_request)

        request = asposewordscloud.models.requests.DeleteWatermarkRequest(remote_name, remote_folder)
        words_api.delete_watermark(request)

        # End README example

        self.write_to_readme()

    def write_to_readme(self):
        # set regex patterns
        startPatern = r"^\s*# Start README example\s*$"
        endPattern = r"^\s*# End README example\s*$"

        # set paths
        sourcePath = __file__
        readmePath =  os.path.dirname(__file__) + "/../README.md"

        # read code from the file
        with open(sourcePath) as f:
            codeLines = f.readlines()

        # extract readme code
        readmeCode = list()
        skipMode = True
        for line in codeLines:
            if skipMode:
        	    skipMode = (re.match(startPatern, line) is None)

            if  not skipMode:
                readmeCode.append(line)
                skipMode = not (re.match(endPattern, line) is None)

        self.assertGreater(len(readmeCode), 2)

        # read readme file
        with open(readmePath) as f:
            readmeLines = f.readlines()

        # replace code
        newReadmeLines = list()
        codeMode = False
        for line in readmeLines:
            if not codeMode:
    	        codeMode = not (re.match(startPatern, line) is None)

    	        if codeMode:
    	            newReadmeLines.extend(readmeCode)

            if codeMode:
                codeMode = re.match(endPattern, line) is None
                continue

            if not codeMode:
                newReadmeLines.append(line)

        # write to readm
        with open(readmePath, 'w') as f:
            for line in newReadmeLines:
                f.write(line)