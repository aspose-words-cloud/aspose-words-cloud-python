# --------------------------------------------------------------------------------
# <copyright company="Aspose" file="SaveAsTiffRequest.py">
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


class SaveAsTiffRequest(object):
    """
    Request model for save_as_tiff operation.
    Initializes a new instance.
    :param name The document name.
    :param save_options Tiff save options.
    :param folder Original document folder.
    :param storage Original document storage.
    :param load_encoding Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
    :param password Password for opening an encrypted document.
    :param use_anti_aliasing Use antialiasing flag.
    :param use_high_quality_rendering Use high quality flag.
    :param image_brightness Brightness for the generated images.
    :param image_color_mode Color mode for the generated images.
    :param image_contrast The contrast for the generated images.
    :param numeral_format The images numeral format.
    :param page_count Number of pages to render.
    :param page_index Page index to start rendering.
    :param paper_color Background image color.
    :param pixel_format The pixel format of generated images.
    :param resolution The resolution of generated images.
    :param scale Zoom factor for generated images.
    :param tiff_compression The compression tipe.
    :param dml_rendering_mode Optional, default is Fallback.
    :param dml_effects_rendering_mode Optional, default is Simplified.
    :param tiff_binarization_method Optional, Tiff binarization method, possible values are: FloydSteinbergDithering, Threshold.
    :param zip_output Optional. A value determining zip output or not.
    :param fonts_location Folder in filestorage with custom fonts.
    """

    def __init__(self, name, save_options, folder=None, storage=None, load_encoding=None, password=None, use_anti_aliasing=None, use_high_quality_rendering=None, image_brightness=None, image_color_mode=None, image_contrast=None, numeral_format=None, page_count=None, page_index=None, paper_color=None, pixel_format=None, resolution=None, scale=None, tiff_compression=None, dml_rendering_mode=None, dml_effects_rendering_mode=None, tiff_binarization_method=None, zip_output=None, fonts_location=None):
        self.name = name
        self.save_options = save_options
        self.folder = folder
        self.storage = storage
        self.load_encoding = load_encoding
        self.password = password
        self.use_anti_aliasing = use_anti_aliasing
        self.use_high_quality_rendering = use_high_quality_rendering
        self.image_brightness = image_brightness
        self.image_color_mode = image_color_mode
        self.image_contrast = image_contrast
        self.numeral_format = numeral_format
        self.page_count = page_count
        self.page_index = page_index
        self.paper_color = paper_color
        self.pixel_format = pixel_format
        self.resolution = resolution
        self.scale = scale
        self.tiff_compression = tiff_compression
        self.dml_rendering_mode = dml_rendering_mode
        self.dml_effects_rendering_mode = dml_effects_rendering_mode
        self.tiff_binarization_method = tiff_binarization_method
        self.zip_output = zip_output
        self.fonts_location = fonts_location
