# --------------------------------------------------------------------------------
# <copyright company="Aspose" file="RemoveRangeRequest.py">
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


class RemoveRangeRequest(object):
    """
    Request model for remove_range operation.
    Initializes a new instance.
    :param name The document.
    :param range_start_identifier The range start identifier. Identifier is the value of the \"nodeId\" field, which every document node has, extended with the prefix \"id\". It looks like \"id0.0.7\". Also values like \"image5\" and \"table3\" can be used as an identifier for images and tables, where the number is an index of the image/table.
    :param range_end_identifier The range end identifier.
    :param folder Original document folder.
    :param storage Original document storage.
    :param load_encoding Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
    :param password Password for opening an encrypted document.
    :param dest_file_name Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
    """

    def __init__(self, name, range_start_identifier, range_end_identifier, folder=None, storage=None, load_encoding=None, password=None, dest_file_name=None):
        self.name = name
        self.range_start_identifier = range_start_identifier
        self.range_end_identifier = range_end_identifier
        self.folder = folder
        self.storage = storage
        self.load_encoding = load_encoding
        self.password = password
        self.dest_file_name = dest_file_name
