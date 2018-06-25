# PdfSaveOptionsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compliance** | **str** | Specifies the PDF standards compliance level for output documents | [optional] 
**create_note_hyperlinks** | **bool** | Specifies whether to convert footnote/endnote references in main text story into active hyperlinks. When clicked the hyperlink will lead to the corresponding footnote/endnote. Default is false. | [optional] 
**custom_properties_export** | **str** | Gets or sets a value determining the way  are exported to PDF file. Default value is . | [optional] 
**digital_signature_details** | [**PdfDigitalSignatureDetailsData**](PdfDigitalSignatureDetailsData.md) | Specifies the details for signing the output PDF document | [optional] 
**display_doc_title** | **bool** | A flag specifying whether the window’s title bar should display the document title taken from the Title entry of the document information dictionary. | [optional] 
**downsample_options** | [**DownsampleOptionsData**](DownsampleOptionsData.md) | Allows to specify downsample options. | [optional] 
**embed_full_fonts** | **bool** | Controls how fonts are embedded into the resulting PDF documents | [optional] 
**encryption_details** | [**PdfEncryptionDetailsData**](PdfEncryptionDetailsData.md) | Specifies the details for encrypting the output PDF document | [optional] 
**export_document_structure** | **bool** | Determines whether or not to export document structure | [optional] 
**font_embedding_mode** | **str** | Specifies the font embedding mode | [optional] 
**image_color_space_export_mode** | **str** | Specifies how the color space will be selected for the images in PDF document. | [optional] 
**image_compression** | **str** | Specifies compression type to be used for all images in the document | [optional] 
**open_hyperlinks_in_new_window** | **bool** | Determines whether hyperlinks in the output Pdf document are forced to be opened in a new window (or tab) of a browser | [optional] 
**outline_options** | [**OutlineOptionsData**](OutlineOptionsData.md) | Allows to specify outline options | [optional] 
**page_mode** | **str** | Specifies how the PDF document should be displayed when opened in the PDF reader | [optional] 
**preblend_images** | **bool** | Gets or sets a value determining whether or not to preblend transparent images with black background color. | [optional] 
**preserve_form_fields** | **bool** | Specifies whether to preserve Microsoft Word form fields as form fields in PDF or convert them to text | [optional] 
**text_compression** | **str** | Specifies compression type to be used for all textual content in the document | [optional] 
**use_book_fold_printing_settings** | **bool** | Determines whether the document should be saved using a booklet printing layout | [optional] 
**use_core_fonts** | **bool** | Determines whether or not to substitute TrueType fonts Arial, Times New Roman, Courier New and Symbol with core PDF Type 1 fonts | [optional] 
**zoom_behavior** | **str** | Determines what type of zoom should be applied when a document is opened with a PDF viewer | [optional] 
**zoom_factor** | **int** | Determines zoom factor (in percentages) for a document | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


