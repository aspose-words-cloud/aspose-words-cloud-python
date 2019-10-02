# --------------------------------------------------------------------------------
# <copyright company="Aspose" file="GetDocumentStatisticsRequest.py">
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
# --------------------------------------------------------------------------------


class GetDocumentStatisticsRequest(object):
    """
    Request model for get_document_statistics operation.
    Initializes a new instance.
    :param name The document name.
    :param folder Original document folder.
    :param storage Original document storage.
    :param load_encoding Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
    :param password Password for opening an encrypted document.
    :param include_comments Support including/excluding comments from the WordCount. Default value is \"false\".
    :param include_footnotes Support including/excluding footnotes from the WordCount. Default value is \"false\".
    :param include_text_in_shapes Support including/excluding shape's text from the WordCount. Default value is \"false\".
    """

    def __init__(self, name, folder=None, storage=None, load_encoding=None, password=None, include_comments=None, include_footnotes=None, include_text_in_shapes=None):
        self.name = name
        self.folder = folder
        self.storage = storage
        self.load_encoding = load_encoding
        self.password = password
        self.include_comments = include_comments
        self.include_footnotes = include_footnotes
        self.include_text_in_shapes = include_text_in_shapes
