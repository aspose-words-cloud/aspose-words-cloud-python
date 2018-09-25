# HtmlFixedSaveOptionsData

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
**css_class_names_prefix** | **str** | Specifies prefix which is added to all class names in style.css file. Default value is \&quot;aw\&quot;. | [optional] 
**encoding** | **str** | Encoding. | [optional] 
**export_embedded_css** | **bool** | Specifies whether the CSS (Cascading Style Sheet) should be embedded into Html document. | [optional] 
**export_embedded_fonts** | **bool** | Specifies whether fonts should be embedded into Html document in Base64 format. | [optional] 
**export_embedded_images** | **bool** | Specifies whether images should be embedded into Html document in Base64 format. | [optional] 
**export_form_fields** | **bool** | Gets or sets indication of whether form fields are exported as interactive items (as &#39;input&#39; tag) rather than converted to text or graphics. | [optional] 
**font_format** | **str** | Specifies export format of fonts | [optional] 
**page_horizontal_alignment** | **str** | Specifies the horizontal alignment of pages in an HTML document. Default value is HtmlFixedHorizontalPageAlignment.Center. | [optional] 
**page_margins** | **float** | Specifies the margins around pages in an HTML document. The margins value is measured in points and should be equal to or greater than 0. Default value is 10 points. | [optional] 
**resources_folder** | **str** | Specifies the physical folder where resources are saved when exporting a document | [optional] 
**resources_folder_alias** | **str** | Specifies the name of the folder used to construct resource URIs | [optional] 
**save_font_face_css_separately** | **bool** | Flag indicates whether \&quot;@font-face\&quot; CSS rules should be placed into a separate file \&quot;fontFaces.css\&quot; when a document is being saved with external stylesheet (that is, when Aspose.Words.Saving.HtmlFixedSaveOptions.ExportEmbeddedCss is false). Default value is false, all CSS rules are written into single file \&quot;styles.css\&quot;. | [optional] 
**show_page_border** | **bool** | Specifies whether border around pages should be shown. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


