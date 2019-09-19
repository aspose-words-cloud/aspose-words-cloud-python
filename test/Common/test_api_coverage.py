#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_api_coverage.py">
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

import test
import asposewordscloud
from test.base_test_context import BaseTestContext


class TestApiCoverage(BaseTestContext):

    def test_api_coverage(self):
        arr = [test.TestBookmarks, test.TestAppendDocument, test.TestComments, test.TestCompareDocument,
               test.TestConvertDocument,
               test.TestDocumentStatistics, test.TestDocument, test.TestLoadWebDocument, test.TestRevisions,
               test.TestSplitDocument, test.TestDocumentProperties, test.TestDocumentProtection,
               test.TestDrawingObjects, test.TestFields,
               test.TestFormField, test.TestMailMergeFields, test.TestFootnote, test.TestHeaderFooter,
               test.TestHyperlinks, test.TestMacros,
               test.TestExecuteMailMerge, test.TestMathObjects, test.TestPages,
               test.TestParagraphs, test.TestRuns,
               test.TestSections, test.TestTables, test.TestText, test.TestWatermarks, test.TestFont,
               test.TestClassification, test.TestFile, test.TestFolder, test.TestRange]
        test_methods = []
        uncovered_methods = []
        for ar in arr:
            test_methods += list(filter(lambda x: not (x.startswith('__') and x.endswith('__')) and x != 'test_folder',
                                        ar.__dict__.keys()))
        api_methods = list(filter(lambda x: not (x.startswith('__') and x.endswith('__'))
                                            and not x.endswith('with_http_info')
                                            and not x.endswith('letter')
                                            and not x.endswith('token'),
                                  asposewordscloud.WordsApi.__dict__.keys()))
        for api_method in api_methods:
            if not 'test_' + api_method in test_methods:
                uncovered_methods += api_method
        self.assertTrue(len(uncovered_methods) == 0,
                        "There are methods you have to cover with tests " + ''.join(uncovered_methods))
