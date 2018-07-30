# XamlFixedSaveOptionsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color_mode** | **str** | Gets or sets a value determining how colors are rendered. { Normal | Grayscale} | [optional] 
**save_format** | **str** | format of save | [optional] 
**file_name** | **str** | name of destination file | [optional] 
**dml_rendering_mode** | **str** | Gets or sets a value determining how DrawingML shapes are rendered. { Fallback | DrawingML } | [optional] 
**dml_effects_rendering_mode** | **str** | Gets or sets a value determining how DrawingML effects are rendered. { Simplified | None | Fine } | [optional] 
**zip_output** | **bool** | Controls zip output or not. Default value is false. | [optional] 
**update_last_saved_time_property** | **bool** | Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving. | [optional] 
**update_sdt_content** | **bool** | Gets or sets value determining whether content of  is updated before saving. | [optional] 
**update_fields** | **bool** | Gets or sets a value determining if fields should be updated before saving the document to a fixed page format. Default value for this property is true | [optional] 
**jpeg_quality** | **int** | Determines the quality of the JPEG images inside PDF document. | [optional] 
**metafile_rendering_options** | [**MetafileRenderingOptionsData**](MetafileRenderingOptionsData.md) | Allows to specify metafile rendering options. | [optional] 
**numeral_format** | **str** | Indicates the symbol set that is used to represent numbers while rendering to fixed page formats | [optional] 
**optimize_output** | **bool** | Flag indicates whether it is required to optimize output of XPS.  If this flag is set redundant nested canvases and empty canvases are removed, also neighbor glyphs with the same formatting are concatenated.  Note: The accuracy of the content display may be affected if this property is set to true.  Default is false. | [optional] 
**page_count** | **int** | Determines number of pages to render | [optional] 
**page_index** | **int** | Determines 0-based index of the first page to render | [optional] 
**resources_folder** | **str** | Specifies the physical folder where resources (images and fonts) are saved when exporting a document to fixed page Xaml format. Default is null. | [optional] 
**resources_folder_alias** | **str** | Specifies the name of the folder used to construct image URIs written into an fixed page Xaml document. Default is null. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


