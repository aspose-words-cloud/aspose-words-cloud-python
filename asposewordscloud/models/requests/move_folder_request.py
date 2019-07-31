# --------------------------------------------------------------------------------
# <copyright company="Aspose" file="MoveFolderRequest.py">
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


class MoveFolderRequest(object):
    """
    Request model for move_folder operation.
    Initializes a new instance.
    :param dest_path Destination folder path to move to e.g '/dst'
    :param src_path Source folder path e.g. /Folder1
    :param src_storage_name Source storage name
    :param dest_storage_name Destination storage name
    """

    def __init__(self, dest_path, src_path, src_storage_name=None, dest_storage_name=None):
        self.dest_path = dest_path
        self.src_path = src_path
        self.src_storage_name = src_storage_name
        self.dest_storage_name = dest_storage_name
