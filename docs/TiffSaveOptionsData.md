# TiffSaveOptionsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graphics_quality_options** | [**GraphicsQualityOptionsData**](GraphicsQualityOptionsData.md) |  | [optional] 
**horizontal_resolution** | **float** | Gets or sets the horizontal resolution for the generated images, in dots per inch.  This property has effect only when saving to raster image formats. The default value is 96. | [optional] 
**image_brightness** | **float** | Gets or sets brightness of image. | [optional] 
**image_color_mode** | **str** | Gets or sets color mode of image. | [optional] 
**image_contrast** | **float** | Gets or sets contrast of image. | [optional] 
**paper_color** | **str** | Gets or sets background (paper) color of image. | [optional] 
**pixel_format** | **str** | Gets or sets pixel format of image. | [optional] 
**resolution** | **float** | Gets or sets both horizontal and vertical resolution for the generated images, in dots per inch.  This property has effect only when saving to raster image formats. The default value is 96. | [optional] 
**scale** | **float** | Gets or sets zoom factor of image. | [optional] 
**use_anti_aliasing** | **bool** | Gets or sets determine whether or not to use anti-aliasing for rendering. | [optional] 
**use_gdi_emf_renderer** | **bool** | Gets or sets a value determining whether to use GDI+ or Aspose.Words metafile renderer when saving to EMF. | [optional] 
**use_high_quality_rendering** | **bool** | Gets or sets determine whether or not to use high quality (i.e. slow) rendering algorithms. | [optional] 
**vertical_resolution** | **float** | Gets or sets the vertical resolution for the generated images, in dots per inch.  This property has effect only when saving to raster image formats. The default value is 96. | [optional] 
**color_mode** | **str** | Gets or sets a value determining how colors are rendered. { Normal | Grayscale}. | [optional] 
**jpeg_quality** | **int** | Gets or sets determines the quality of the JPEG images inside PDF document. | [optional] 
**metafile_rendering_options** | [**MetafileRenderingOptionsData**](MetafileRenderingOptionsData.md) |  | [optional] 
**numeral_format** | **str** | Gets or sets indicates the symbol set that is used to represent numbers while rendering to fixed page formats. | [optional] 
**optimize_output** | **bool** | Gets or sets flag indicates whether it is required to optimize output of XPS. If this flag is set redundant nested canvases and empty canvases are removed, also neighbor glyphs with the same formatting are concatenated. Note: The accuracy of the content display may be affected if this property is set to true.  Default is false. | [optional] 
**page_count** | **int** | Gets or sets determines number of pages to render. | [optional] 
**page_index** | **int** | Gets or sets determines 0-based index of the first page to render. | [optional] 
**save_format** | **str** | Gets or sets format of save. | [optional] 
**file_name** | **str** | Gets or sets name of destination file. | [optional] 
**dml_rendering_mode** | **str** | Gets or sets a value determining how DrawingML shapes are rendered. { Fallback | DrawingML }. | [optional] 
**dml_effects_rendering_mode** | **str** | Gets or sets a value determining how DrawingML effects are rendered. { Simplified | None | Fine }. | [optional] 
**zip_output** | **bool** | Gets or sets controls zip output or not. Default value is false. | [optional] 
**update_last_saved_time_property** | **bool** | Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving. | [optional] 
**update_sdt_content** | **bool** | Gets or sets value determining whether content of StructuredDocumentTag is updated before saving. | [optional] 
**update_fields** | **bool** | Gets or sets a value determining if fields should be updated before saving the document to a fixed page format. Default value for this property is. true | [optional] 
**threshold_for_floyd_steinberg_dithering** | **int** | Gets or sets the threshold that determines the value of the binarization error in the Floyd-Steinberg method. when ImageBinarizationMethod is ImageBinarizationMethod.FloydSteinbergDithering. Default value is 128. | [optional] 
**tiff_binarization_method** | **str** | Gets or sets specifies method used while converting images to 1 bpp format. | [optional] 
**tiff_compression** | **str** | Gets or sets type of compression. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

