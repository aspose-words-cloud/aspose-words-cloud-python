# aspose-words-cloud.WordsApi

All URIs are relative to *https://localhost/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_all_revisions**](WordsApi.md#accept_all_revisions) | **POST** /words/{name}/revisions/acceptAll | Accept all revisions in document
[**classify**](WordsApi.md#classify) | **PUT** /words/classify | Classify raw text.
[**classify_document**](WordsApi.md#classify_document) | **GET** /words/{documentName}/classify | Classify document.
[**create_or_update_document_property**](WordsApi.md#create_or_update_document_property) | **POST** /words/{name}/documentProperties/{propertyName} | Add new or update existing document property.
[**delete_border**](WordsApi.md#delete_border) | **DELETE** /words/{name}/{nodePath}/borders/{index} | Resets border properties to default values.             
[**delete_borders**](WordsApi.md#delete_borders) | **DELETE** /words/{name}/{nodePath}/borders | Resets borders properties to default values.             
[**delete_comment**](WordsApi.md#delete_comment) | **DELETE** /words/{name}/comments/{commentIndex} | Remove comment from document.
[**delete_document_macros**](WordsApi.md#delete_document_macros) | **DELETE** /words/{name}/macros | Remove macros from document.
[**delete_document_property**](WordsApi.md#delete_document_property) | **DELETE** /words/{name}/documentProperties/{propertyName} | Delete document property.
[**delete_document_watermark**](WordsApi.md#delete_document_watermark) | **DELETE** /words/{name}/watermark | Delete watermark (for deleting last watermark from the document).
[**delete_drawing_object**](WordsApi.md#delete_drawing_object) | **DELETE** /words/{name}/{nodePath}/drawingObjects/{index} | Removes drawing object from document.
[**delete_field**](WordsApi.md#delete_field) | **DELETE** /words/{name}/{nodePath}/fields/{index} | Delete field from document.
[**delete_fields**](WordsApi.md#delete_fields) | **DELETE** /words/{name}/{nodePath}/fields | Remove fields from section paragraph.
[**delete_footnote**](WordsApi.md#delete_footnote) | **DELETE** /words/{name}/{nodePath}/footnotes/{index} | Removes footnote from document.
[**delete_form_field**](WordsApi.md#delete_form_field) | **DELETE** /words/{name}/{nodePath}/formfields/{index} | Removes form field from document.
[**delete_header_footer**](WordsApi.md#delete_header_footer) | **DELETE** /words/{name}/{sectionPath}/headersfooters/{index} | Delete header/footer from document.
[**delete_headers_footers**](WordsApi.md#delete_headers_footers) | **DELETE** /words/{name}/{sectionPath}/headersfooters | Delete document headers and footers.
[**delete_office_math_object**](WordsApi.md#delete_office_math_object) | **DELETE** /words/{name}/{nodePath}/OfficeMathObjects/{index} | Removes OfficeMath object from document.
[**delete_paragraph**](WordsApi.md#delete_paragraph) | **DELETE** /words/{name}/{nodePath}/paragraphs/{index} | Remove paragraph from section.
[**delete_run**](WordsApi.md#delete_run) | **DELETE** /words/{name}/{paragraphPath}/runs/{index} | Removes run from document.
[**delete_table**](WordsApi.md#delete_table) | **DELETE** /words/{name}/{nodePath}/tables/{index} | Delete a table.
[**delete_table_cell**](WordsApi.md#delete_table_cell) | **DELETE** /words/{name}/{tableRowPath}/cells/{index} | Delete a table cell.
[**delete_table_row**](WordsApi.md#delete_table_row) | **DELETE** /words/{name}/{tablePath}/rows/{index} | Delete a table row.
[**delete_unprotect_document**](WordsApi.md#delete_unprotect_document) | **DELETE** /words/{name}/protection | Unprotect document.
[**get_available_fonts**](WordsApi.md#get_available_fonts) | **GET** /words/fonts/available | Gets the list of fonts, available for document processing
[**get_border**](WordsApi.md#get_border) | **GET** /words/{name}/{nodePath}/borders/{index} | Return a border.
[**get_borders**](WordsApi.md#get_borders) | **GET** /words/{name}/{nodePath}/borders | Return a collection of borders.
[**get_comment**](WordsApi.md#get_comment) | **GET** /words/{name}/comments/{commentIndex} | Get comment from document.
[**get_comments**](WordsApi.md#get_comments) | **GET** /words/{name}/comments | Get comments from document.
[**get_document**](WordsApi.md#get_document) | **GET** /words/{documentName} | Read document common info.
[**get_document_bookmark_by_name**](WordsApi.md#get_document_bookmark_by_name) | **GET** /words/{name}/bookmarks/{bookmarkName} | Read document bookmark data by its name.
[**get_document_bookmarks**](WordsApi.md#get_document_bookmarks) | **GET** /words/{name}/bookmarks | Read document bookmarks common info.
[**get_document_drawing_object_by_index**](WordsApi.md#get_document_drawing_object_by_index) | **GET** /words/{name}/{nodePath}/drawingObjects/{index} | Read document drawing object common info by its index or convert to format specified.
[**get_document_drawing_object_image_data**](WordsApi.md#get_document_drawing_object_image_data) | **GET** /words/{name}/{nodePath}/drawingObjects/{index}/imageData | Read drawing object image data.
[**get_document_drawing_object_ole_data**](WordsApi.md#get_document_drawing_object_ole_data) | **GET** /words/{name}/{nodePath}/drawingObjects/{index}/oleData | Get drawing object OLE data.
[**get_document_drawing_objects**](WordsApi.md#get_document_drawing_objects) | **GET** /words/{name}/{nodePath}/drawingObjects | Read document drawing objects common info.
[**get_document_field_names**](WordsApi.md#get_document_field_names) | **GET** /words/{name}/mailMergeFieldNames | Read document field names.
[**get_document_hyperlink_by_index**](WordsApi.md#get_document_hyperlink_by_index) | **GET** /words/{name}/hyperlinks/{hyperlinkIndex} | Read document hyperlink by its index.
[**get_document_hyperlinks**](WordsApi.md#get_document_hyperlinks) | **GET** /words/{name}/hyperlinks | Read document hyperlinks common info.
[**get_document_paragraph**](WordsApi.md#get_document_paragraph) | **GET** /words/{name}/{nodePath}/paragraphs/{index} | This resource represents one of the paragraphs contained in the document.
[**get_document_paragraph_format**](WordsApi.md#get_document_paragraph_format) | **GET** /words/{name}/{nodePath}/paragraphs/{index}/format | Represents all the formatting for a paragraph.
[**get_document_paragraph_run**](WordsApi.md#get_document_paragraph_run) | **GET** /words/{name}/{paragraphPath}/runs/{index} | This resource represents run of text contained in the document.
[**get_document_paragraph_run_font**](WordsApi.md#get_document_paragraph_run_font) | **GET** /words/{name}/{paragraphPath}/runs/{index}/font | This resource represents font of run.
[**get_document_paragraph_runs**](WordsApi.md#get_document_paragraph_runs) | **GET** /words/{name}/{paragraphPath}/runs | This resource represents collection of runs in the paragraph.
[**get_document_paragraphs**](WordsApi.md#get_document_paragraphs) | **GET** /words/{name}/{nodePath}/paragraphs | Return a list of paragraphs that are contained in the document.
[**get_document_properties**](WordsApi.md#get_document_properties) | **GET** /words/{name}/documentProperties | Read document properties info.
[**get_document_property**](WordsApi.md#get_document_property) | **GET** /words/{name}/documentProperties/{propertyName} | Read document property info by the property name.
[**get_document_protection**](WordsApi.md#get_document_protection) | **GET** /words/{name}/protection | Read document protection common info.
[**get_document_statistics**](WordsApi.md#get_document_statistics) | **GET** /words/{name}/statistics | Read document statistics.
[**get_document_text_items**](WordsApi.md#get_document_text_items) | **GET** /words/{name}/textItems | Read document text items.
[**get_document_with_format**](WordsApi.md#get_document_with_format) | **GET** /words/{name} | Export the document into the specified format.
[**get_field**](WordsApi.md#get_field) | **GET** /words/{name}/{nodePath}/fields/{index} | Get field from document.
[**get_fields**](WordsApi.md#get_fields) | **GET** /words/{name}/{nodePath}/fields | Get fields from document.
[**get_footnote**](WordsApi.md#get_footnote) | **GET** /words/{name}/{nodePath}/footnotes/{index} | Read footnote by index.
[**get_footnotes**](WordsApi.md#get_footnotes) | **GET** /words/{name}/{nodePath}/footnotes | Get footnotes from document.
[**get_form_field**](WordsApi.md#get_form_field) | **GET** /words/{name}/{nodePath}/formfields/{index} | Returns representation of an one of the form field.
[**get_form_fields**](WordsApi.md#get_form_fields) | **GET** /words/{name}/{nodePath}/formfields | Get form fields from document.
[**get_header_footer**](WordsApi.md#get_header_footer) | **GET** /words/{name}/headersfooters/{headerFooterIndex} | Return a header/footer that is contained in the document.
[**get_header_footer_of_section**](WordsApi.md#get_header_footer_of_section) | **GET** /words/{name}/sections/{sectionIndex}/headersfooters/{headerFooterIndex} | Return a header/footer that is contained in the document.
[**get_header_footers**](WordsApi.md#get_header_footers) | **GET** /words/{name}/{sectionPath}/headersfooters | Return a list of header/footers that are contained in the document.
[**get_office_math_object**](WordsApi.md#get_office_math_object) | **GET** /words/{name}/{nodePath}/OfficeMathObjects/{index} | Read OfficeMath object by index.
[**get_office_math_objects**](WordsApi.md#get_office_math_objects) | **GET** /words/{name}/{nodePath}/OfficeMathObjects | Get OfficeMath objects from document.
[**get_section**](WordsApi.md#get_section) | **GET** /words/{name}/sections/{sectionIndex} | Get document section by index.
[**get_section_page_setup**](WordsApi.md#get_section_page_setup) | **GET** /words/{name}/sections/{sectionIndex}/pageSetup | Get page setup of section.
[**get_sections**](WordsApi.md#get_sections) | **GET** /words/{name}/sections | Return a list of sections that are contained in the document.
[**get_table**](WordsApi.md#get_table) | **GET** /words/{name}/{nodePath}/tables/{index} | Return a table.
[**get_table_cell**](WordsApi.md#get_table_cell) | **GET** /words/{name}/{tableRowPath}/cells/{index} | Return a table cell.
[**get_table_cell_format**](WordsApi.md#get_table_cell_format) | **GET** /words/{name}/{tableRowPath}/cells/{index}/cellformat | Return a table cell format.
[**get_table_properties**](WordsApi.md#get_table_properties) | **GET** /words/{name}/{nodePath}/tables/{index}/properties | Return a table properties.
[**get_table_row**](WordsApi.md#get_table_row) | **GET** /words/{name}/{tablePath}/rows/{index} | Return a table row.
[**get_table_row_format**](WordsApi.md#get_table_row_format) | **GET** /words/{name}/{tablePath}/rows/{index}/rowformat | Return a table row format.
[**get_tables**](WordsApi.md#get_tables) | **GET** /words/{name}/{nodePath}/tables | Return a list of tables that are contained in the document.
[**insert_table**](WordsApi.md#insert_table) | **PUT** /words/{name}/{nodePath}/tables | Adds table to document, returns added table&#39;s data.             
[**insert_table_cell**](WordsApi.md#insert_table_cell) | **PUT** /words/{name}/{tableRowPath}/cells | Adds table cell to table, returns added cell&#39;s data.             
[**insert_table_row**](WordsApi.md#insert_table_row) | **PUT** /words/{name}/{tablePath}/rows | Adds table row to table, returns added row&#39;s data.             
[**post_append_document**](WordsApi.md#post_append_document) | **POST** /words/{name}/appendDocument | Append documents to original document.
[**post_change_document_protection**](WordsApi.md#post_change_document_protection) | **POST** /words/{name}/protection | Change document protection.
[**post_comment**](WordsApi.md#post_comment) | **POST** /words/{name}/comments/{commentIndex} | Updates the comment, returns updated comment&#39;s data.
[**post_compare_document**](WordsApi.md#post_compare_document) | **POST** /words/{name}/compareDocument | Compare document with original document.
[**post_document_execute_mail_merge**](WordsApi.md#post_document_execute_mail_merge) | **POST** /words/{name}/executeMailMerge | Execute document mail merge operation.
[**post_document_paragraph_format**](WordsApi.md#post_document_paragraph_format) | **POST** /words/{name}/{nodePath}/paragraphs/{index}/format | Updates paragrpaph format properties, returns updated format properties.
[**post_document_paragraph_run_font**](WordsApi.md#post_document_paragraph_run_font) | **POST** /words/{name}/{paragraphPath}/runs/{index}/font | Updates font properties, returns updated font data.
[**post_document_save_as**](WordsApi.md#post_document_save_as) | **POST** /words/{name}/saveAs | Convert document to destination format with detailed settings and save result to storage.
[**post_drawing_object**](WordsApi.md#post_drawing_object) | **POST** /words/{name}/{nodePath}/drawingObjects/{index} | Updates drawing object, returns updated  drawing object&#39;s data.
[**post_execute_template**](WordsApi.md#post_execute_template) | **POST** /words/{name}/executeTemplate | Populate document template with data.
[**post_field**](WordsApi.md#post_field) | **POST** /words/{name}/{nodePath}/fields/{index} | Updates field&#39;s properties, returns updated field&#39;s data.
[**post_footnote**](WordsApi.md#post_footnote) | **POST** /words/{name}/{nodePath}/footnotes/{index} | Updates footnote&#39;s properties, returns updated run&#39;s data.
[**post_form_field**](WordsApi.md#post_form_field) | **POST** /words/{name}/{nodePath}/formfields/{index} | Updates properties of form field, returns updated form field.
[**post_insert_document_watermark_image**](WordsApi.md#post_insert_document_watermark_image) | **POST** /words/{name}/watermark/insertImage | Insert document watermark image.
[**post_insert_document_watermark_text**](WordsApi.md#post_insert_document_watermark_text) | **POST** /words/{name}/watermark/insertText | Insert document watermark text.
[**post_insert_page_numbers**](WordsApi.md#post_insert_page_numbers) | **POST** /words/{name}/insertPageNumbers | Insert document page numbers.
[**post_load_web_document**](WordsApi.md#post_load_web_document) | **POST** /words/loadWebDocument | Loads new document from web into the file with any supported format of data.
[**post_replace_text**](WordsApi.md#post_replace_text) | **POST** /words/{name}/replaceText | Replace document text.
[**post_run**](WordsApi.md#post_run) | **POST** /words/{name}/{paragraphPath}/runs/{index} | Updates run&#39;s properties, returns updated run&#39;s data.
[**post_split_document**](WordsApi.md#post_split_document) | **POST** /words/{name}/split | Split document.
[**post_update_document_bookmark**](WordsApi.md#post_update_document_bookmark) | **POST** /words/{name}/bookmarks/{bookmarkName} | Update document bookmark.
[**post_update_document_fields**](WordsApi.md#post_update_document_fields) | **POST** /words/{name}/updateFields | Update (reevaluate) fields in document.
[**put_comment**](WordsApi.md#put_comment) | **PUT** /words/{name}/comments | Adds comment to document, returns inserted comment&#39;s data.
[**put_convert_document**](WordsApi.md#put_convert_document) | **PUT** /words/convert | Convert document from request content to format specified.
[**put_create_document**](WordsApi.md#put_create_document) | **PUT** /words/create | Creates new document. Document is created with format which is recognized from file extensions.  Supported extentions: \&quot;.doc\&quot;, \&quot;.docx\&quot;, \&quot;.docm\&quot;, \&quot;.dot\&quot;, \&quot;.dotm\&quot;, \&quot;.dotx\&quot;, \&quot;.flatopc\&quot;, \&quot;.fopc\&quot;, \&quot;.flatopc_macro\&quot;, \&quot;.fopc_macro\&quot;, \&quot;.flatopc_template\&quot;, \&quot;.fopc_template\&quot;, \&quot;.flatopc_template_macro\&quot;, \&quot;.fopc_template_macro\&quot;, \&quot;.wordml\&quot;, \&quot;.wml\&quot;, \&quot;.rtf\&quot;
[**put_document_field_names**](WordsApi.md#put_document_field_names) | **PUT** /words/mailMergeFieldNames | Read document field names.
[**put_document_save_as_tiff**](WordsApi.md#put_document_save_as_tiff) | **PUT** /words/{name}/saveAs/tiff | Convert document to tiff with detailed settings and save result to storage.
[**put_drawing_object**](WordsApi.md#put_drawing_object) | **PUT** /words/{name}/{nodePath}/drawingObjects | Adds  drawing object to document, returns added  drawing object&#39;s data.
[**put_execute_mail_merge_online**](WordsApi.md#put_execute_mail_merge_online) | **PUT** /words/executeMailMerge | Execute document mail merge online.
[**put_execute_template_online**](WordsApi.md#put_execute_template_online) | **PUT** /words/executeTemplate | Populate document template with data online.
[**put_field**](WordsApi.md#put_field) | **PUT** /words/{name}/{nodePath}/fields | Adds field to document, returns inserted field&#39;s data.
[**put_footnote**](WordsApi.md#put_footnote) | **PUT** /words/{name}/{nodePath}/footnotes | Adds footnote to document, returns added footnote&#39;s data.
[**put_form_field**](WordsApi.md#put_form_field) | **PUT** /words/{name}/{nodePath}/formfields | Adds form field to paragraph, returns added form field&#39;s data.
[**put_header_footer**](WordsApi.md#put_header_footer) | **PUT** /words/{name}/{sectionPath}/headersfooters | Insert to document header or footer.
[**put_paragraph**](WordsApi.md#put_paragraph) | **PUT** /words/{name}/{nodePath}/paragraphs | Adds paragraph to document, returns added paragraph&#39;s data.
[**put_protect_document**](WordsApi.md#put_protect_document) | **PUT** /words/{name}/protection | Protect document.
[**put_run**](WordsApi.md#put_run) | **PUT** /words/{name}/{paragraphPath}/runs | Adds run to document, returns added paragraph&#39;s data.
[**reject_all_revisions**](WordsApi.md#reject_all_revisions) | **POST** /words/{name}/revisions/rejectAll | Reject all revisions in document
[**render_drawing_object**](WordsApi.md#render_drawing_object) | **GET** /words/{name}/{nodePath}/drawingObjects/{index}/render | Renders drawing object to specified format.
[**render_math_object**](WordsApi.md#render_math_object) | **GET** /words/{name}/{nodePath}/OfficeMathObjects/{index}/render | Renders math object to specified format.
[**render_page**](WordsApi.md#render_page) | **GET** /words/{name}/pages/{pageIndex}/render | Renders page to specified format.
[**render_paragraph**](WordsApi.md#render_paragraph) | **GET** /words/{name}/{nodePath}/paragraphs/{index}/render | Renders paragraph to specified format.
[**render_table**](WordsApi.md#render_table) | **GET** /words/{name}/{nodePath}/tables/{index}/render | Renders table to specified format.
[**reset_cache**](WordsApi.md#reset_cache) | **DELETE** /words/fonts/cache | Resets font&#39;s cache.
[**search**](WordsApi.md#search) | **GET** /words/{name}/search | Search text in document.
[**update_border**](WordsApi.md#update_border) | **POST** /words/{name}/{nodePath}/borders/{index} | Updates border properties.             
[**update_section_page_setup**](WordsApi.md#update_section_page_setup) | **POST** /words/{name}/sections/{sectionIndex}/pageSetup | Update page setup of section.
[**update_table_cell_format**](WordsApi.md#update_table_cell_format) | **POST** /words/{name}/{tableRowPath}/cells/{index}/cellformat | Updates a table cell format.
[**update_table_properties**](WordsApi.md#update_table_properties) | **POST** /words/{name}/{nodePath}/tables/{index}/properties | Updates a table properties.
[**update_table_row_format**](WordsApi.md#update_table_row_format) | **POST** /words/{name}/{tablePath}/rows/{index}/rowformat | Updates a table row format.


# **accept_all_revisions**
> RevisionsModificationResponse accept_all_revisions(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)

Accept all revisions in document

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)

try:
    # Accept all revisions in document
    api_response = api_instance.accept_all_revisions(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->accept_all_revisions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 

### Return type

[**RevisionsModificationResponse**](RevisionsModificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **classify**
> ClassificationResponse classify(text, best_classes_count=best_classes_count)

Classify raw text.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
text = 'text_example' # str | Text to classify.
best_classes_count = '1' # str | Count of the best classes to return. (optional) (default to 1)

try:
    # Classify raw text.
    api_response = api_instance.classify(text, best_classes_count=best_classes_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->classify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Text to classify. | 
 **best_classes_count** | **str**| Count of the best classes to return. | [optional] [default to 1]

### Return type

[**ClassificationResponse**](ClassificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **classify_document**
> ClassificationResponse classify_document(document_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, best_classes_count=best_classes_count, taxonomy=taxonomy)

Classify document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
document_name = 'document_name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
best_classes_count = '1' # str | Count of the best classes to return. (optional) (default to 1)
taxonomy = 'default' # str | Taxonomy to use for classification return. (optional) (default to default)

try:
    # Classify document.
    api_response = api_instance.classify_document(document_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, best_classes_count=best_classes_count, taxonomy=taxonomy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->classify_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **best_classes_count** | **str**| Count of the best classes to return. | [optional] [default to 1]
 **taxonomy** | **str**| Taxonomy to use for classification return. | [optional] [default to default]

### Return type

[**ClassificationResponse**](ClassificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_document_property**
> DocumentPropertyResponse create_or_update_document_property(name, property_name, _property, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Add new or update existing document property.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
property_name = 'property_name_example' # str | The property name.
_property = aspose-words-cloud.DocumentProperty() # DocumentProperty | The property with new value.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Add new or update existing document property.
    api_response = api_instance.create_or_update_document_property(name, property_name, _property, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->create_or_update_document_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **property_name** | **str**| The property name. | 
 **_property** | [**DocumentProperty**](DocumentProperty.md)| The property with new value. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**DocumentPropertyResponse**](DocumentPropertyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_border**
> BorderResponse delete_border(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Resets border properties to default values.             

'nodePath' should refer to node with cell or row

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to node with border(node should be cell or row).
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Resets border properties to default values.             
    api_response = api_instance.delete_border(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_border: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to node with border(node should be cell or row). | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**BorderResponse**](BorderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_borders**
> BordersResponse delete_borders(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Resets borders properties to default values.             

'nodePath' should refer to node with cell or row

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to node with borders(node should be cell or row).
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Resets borders properties to default values.             
    api_response = api_instance.delete_borders(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_borders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to node with borders(node should be cell or row). | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**BordersResponse**](BordersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment**
> AsposeResponse delete_comment(name, comment_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Remove comment from document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The file name.
comment_index = 56 # int | Comment index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Remove comment from document.
    api_response = api_instance.delete_comment(name, comment_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **comment_index** | **int**| Comment index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_macros**
> AsposeResponse delete_document_macros(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Remove macros from document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The file name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Remove macros from document.
    api_response = api_instance.delete_document_macros(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_document_macros: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_property**
> AsposeResponse delete_document_property(name, property_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Delete document property.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
property_name = 'property_name_example' # str | The property name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Delete document property.
    api_response = api_instance.delete_document_property(name, property_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_document_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **property_name** | **str**| The property name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_watermark**
> DocumentResponse delete_document_watermark(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Delete watermark (for deleting last watermark from the document).

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Delete watermark (for deleting last watermark from the document).
    api_response = api_instance.delete_document_watermark(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_document_watermark: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_drawing_object**
> AsposeResponse delete_drawing_object(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)

Removes drawing object from document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The file name.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
node_path = 'node_path_example' # str | Path to node, which contains collection of drawing objects. (optional)

try:
    # Removes drawing object from document.
    api_response = api_instance.delete_drawing_object(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_drawing_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **node_path** | **str**| Path to node, which contains collection of drawing objects. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_field**
> AsposeResponse delete_field(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)

Delete field from document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The file name.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
node_path = 'node_path_example' # str | Path to node, which contains collection of fields. (optional)

try:
    # Delete field from document.
    api_response = api_instance.delete_field(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **node_path** | **str**| Path to node, which contains collection of fields. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fields**
> AsposeResponse delete_fields(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)

Remove fields from section paragraph.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The file name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
node_path = 'node_path_example' # str | Path to node, which contains collection of fields. (optional)

try:
    # Remove fields from section paragraph.
    api_response = api_instance.delete_fields(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **node_path** | **str**| Path to node, which contains collection of fields. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_footnote**
> AsposeResponse delete_footnote(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)

Removes footnote from document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The file name.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
node_path = 'node_path_example' # str | Path to node, which contains collection of footnotes. (optional)

try:
    # Removes footnote from document.
    api_response = api_instance.delete_footnote(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_footnote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **node_path** | **str**| Path to node, which contains collection of footnotes. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_form_field**
> AsposeResponse delete_form_field(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)

Removes form field from document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
node_path = 'node_path_example' # str | Path to node that contains collection of formfields. (optional)

try:
    # Removes form field from document.
    api_response = api_instance.delete_form_field(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_form_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **node_path** | **str**| Path to node that contains collection of formfields. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_header_footer**
> AsposeResponse delete_header_footer(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, section_path=section_path)

Delete header/footer from document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
section_path = 'section_path_example' # str | Path to parent section. (optional)

try:
    # Delete header/footer from document.
    api_response = api_instance.delete_header_footer(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, section_path=section_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_header_footer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **section_path** | **str**| Path to parent section. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_headers_footers**
> AsposeResponse delete_headers_footers(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, section_path=section_path, headers_footers_types=headers_footers_types)

Delete document headers and footers.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
section_path = 'section_path_example' # str | Path to parent section. (optional)
headers_footers_types = 'headers_footers_types_example' # str | List of types of headers and footers. (optional)

try:
    # Delete document headers and footers.
    api_response = api_instance.delete_headers_footers(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, section_path=section_path, headers_footers_types=headers_footers_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_headers_footers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **section_path** | **str**| Path to parent section. | [optional] 
 **headers_footers_types** | **str**| List of types of headers and footers. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_office_math_object**
> AsposeResponse delete_office_math_object(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)

Removes OfficeMath object from document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The file name.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
node_path = 'node_path_example' # str | Path to node, which contains collection of OfficeMath objects. (optional)

try:
    # Removes OfficeMath object from document.
    api_response = api_instance.delete_office_math_object(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_office_math_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **node_path** | **str**| Path to node, which contains collection of OfficeMath objects. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_paragraph**
> AsposeResponse delete_paragraph(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)

Remove paragraph from section.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The file name.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
node_path = 'node_path_example' # str | Path to node which contains paragraphs. (optional)

try:
    # Remove paragraph from section.
    api_response = api_instance.delete_paragraph(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_paragraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **node_path** | **str**| Path to node which contains paragraphs. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_run**
> AsposeResponse delete_run(name, paragraph_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Removes run from document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The file name.
paragraph_path = 'paragraph_path_example' # str | Path to parent paragraph.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Removes run from document.
    api_response = api_instance.delete_run(name, paragraph_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **paragraph_path** | **str**| Path to parent paragraph. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_table**
> AsposeResponse delete_table(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)

Delete a table.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
node_path = 'node_path_example' # str | Path to node, which contains tables. (optional)

try:
    # Delete a table.
    api_response = api_instance.delete_table(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **node_path** | **str**| Path to node, which contains tables. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_table_cell**
> AsposeResponse delete_table_cell(name, table_row_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Delete a table cell.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
table_row_path = 'table_row_path_example' # str | Path to table row.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Delete a table cell.
    api_response = api_instance.delete_table_cell(name, table_row_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_table_cell: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **table_row_path** | **str**| Path to table row. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_table_row**
> AsposeResponse delete_table_row(name, table_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Delete a table row.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
table_path = 'table_path_example' # str | Path to table.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Delete a table row.
    api_response = api_instance.delete_table_row(name, table_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_table_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **table_path** | **str**| Path to table. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_unprotect_document**
> ProtectionDataResponse delete_unprotect_document(name, protection_request, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)

Unprotect document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
protection_request = aspose-words-cloud.ProtectionRequest() # ProtectionRequest | with protection settings.            
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)

try:
    # Unprotect document.
    api_response = api_instance.delete_unprotect_document(name, protection_request, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_unprotect_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **protection_request** | [**ProtectionRequest**](ProtectionRequest.md)| with protection settings.             | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 

### Return type

[**ProtectionDataResponse**](ProtectionDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_fonts**
> AvailableFontsResponse get_available_fonts(fonts_location=fonts_location)

Gets the list of fonts, available for document processing

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Gets the list of fonts, available for document processing
    api_response = api_instance.get_available_fonts(fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_available_fonts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

[**AvailableFontsResponse**](AvailableFontsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_border**
> BorderResponse get_border(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Return a border.

'nodePath' should refer to node with cell or row

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to node with border(node should be cell or row).
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Return a border.
    api_response = api_instance.get_border(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_border: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to node with border(node should be cell or row). | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**BorderResponse**](BorderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_borders**
> BordersResponse get_borders(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Return a collection of borders.

'nodePath' should refer to node with cell or row

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to node with borders(node should be cell or row).
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Return a collection of borders.
    api_response = api_instance.get_borders(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_borders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to node with borders(node should be cell or row). | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**BordersResponse**](BordersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment**
> CommentResponse get_comment(name, comment_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Get comment from document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The file name.
comment_index = 56 # int | Comment index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Get comment from document.
    api_response = api_instance.get_comment(name, comment_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **comment_index** | **int**| Comment index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**CommentResponse**](CommentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comments**
> CommentsResponse get_comments(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Get comments from document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The file name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Get comments from document.
    api_response = api_instance.get_comments(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**CommentsResponse**](CommentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> DocumentResponse get_document(document_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Read document common info.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
document_name = 'document_name_example' # str | The file name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Read document common info.
    api_response = api_instance.get_document(document_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_name** | **str**| The file name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_bookmark_by_name**
> BookmarkResponse get_document_bookmark_by_name(name, bookmark_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Read document bookmark data by its name.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
bookmark_name = 'bookmark_name_example' # str | The bookmark name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Read document bookmark data by its name.
    api_response = api_instance.get_document_bookmark_by_name(name, bookmark_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_bookmark_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **bookmark_name** | **str**| The bookmark name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**BookmarkResponse**](BookmarkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_bookmarks**
> BookmarksResponse get_document_bookmarks(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Read document bookmarks common info.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Read document bookmarks common info.
    api_response = api_instance.get_document_bookmarks(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_bookmarks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**BookmarksResponse**](BookmarksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_drawing_object_by_index**
> DrawingObjectResponse get_document_drawing_object_by_index(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)

Read document drawing object common info by its index or convert to format specified.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
node_path = 'node_path_example' # str | Path to node, which contains collection of drawing objects. (optional)

try:
    # Read document drawing object common info by its index or convert to format specified.
    api_response = api_instance.get_document_drawing_object_by_index(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_drawing_object_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **node_path** | **str**| Path to node, which contains collection of drawing objects. | [optional] 

### Return type

[**DrawingObjectResponse**](DrawingObjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_drawing_object_image_data**
> file get_document_drawing_object_image_data(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)

Read drawing object image data.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
node_path = 'node_path_example' # str | Path to node, which contains collection of drawing objects. (optional)

try:
    # Read drawing object image data.
    api_response = api_instance.get_document_drawing_object_image_data(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_drawing_object_image_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **node_path** | **str**| Path to node, which contains collection of drawing objects. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_drawing_object_ole_data**
> file get_document_drawing_object_ole_data(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)

Get drawing object OLE data.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
node_path = 'node_path_example' # str | Path to node, which contains collection of drawing objects. (optional)

try:
    # Get drawing object OLE data.
    api_response = api_instance.get_document_drawing_object_ole_data(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_drawing_object_ole_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **node_path** | **str**| Path to node, which contains collection of drawing objects. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_drawing_objects**
> DrawingObjectsResponse get_document_drawing_objects(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)

Read document drawing objects common info.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
node_path = 'node_path_example' # str | Path to node, which contains collection of drawing objects. (optional)

try:
    # Read document drawing objects common info.
    api_response = api_instance.get_document_drawing_objects(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_drawing_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **node_path** | **str**| Path to node, which contains collection of drawing objects. | [optional] 

### Return type

[**DrawingObjectsResponse**](DrawingObjectsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_field_names**
> FieldNamesResponse get_document_field_names(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, use_non_merge_fields=use_non_merge_fields)

Read document field names.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
use_non_merge_fields = false # bool | If true, result includes \"mustache\" field names. (optional) (default to false)

try:
    # Read document field names.
    api_response = api_instance.get_document_field_names(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, use_non_merge_fields=use_non_merge_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_field_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **use_non_merge_fields** | **bool**| If true, result includes \&quot;mustache\&quot; field names. | [optional] [default to false]

### Return type

[**FieldNamesResponse**](FieldNamesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_hyperlink_by_index**
> HyperlinkResponse get_document_hyperlink_by_index(name, hyperlink_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Read document hyperlink by its index.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
hyperlink_index = 56 # int | The hyperlink index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Read document hyperlink by its index.
    api_response = api_instance.get_document_hyperlink_by_index(name, hyperlink_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_hyperlink_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **hyperlink_index** | **int**| The hyperlink index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**HyperlinkResponse**](HyperlinkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_hyperlinks**
> HyperlinksResponse get_document_hyperlinks(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Read document hyperlinks common info.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Read document hyperlinks common info.
    api_response = api_instance.get_document_hyperlinks(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_hyperlinks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**HyperlinksResponse**](HyperlinksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_paragraph**
> ParagraphResponse get_document_paragraph(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)

This resource represents one of the paragraphs contained in the document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
node_path = 'node_path_example' # str | Path to node which contains paragraphs. (optional)

try:
    # This resource represents one of the paragraphs contained in the document.
    api_response = api_instance.get_document_paragraph(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_paragraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **node_path** | **str**| Path to node which contains paragraphs. | [optional] 

### Return type

[**ParagraphResponse**](ParagraphResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_paragraph_format**
> ParagraphFormatResponse get_document_paragraph_format(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)

Represents all the formatting for a paragraph.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
node_path = 'node_path_example' # str | Path to node which contains paragraphs. (optional)

try:
    # Represents all the formatting for a paragraph.
    api_response = api_instance.get_document_paragraph_format(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_paragraph_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **node_path** | **str**| Path to node which contains paragraphs. | [optional] 

### Return type

[**ParagraphFormatResponse**](ParagraphFormatResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_paragraph_run**
> RunResponse get_document_paragraph_run(name, paragraph_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

This resource represents run of text contained in the document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
paragraph_path = 'paragraph_path_example' # str | Path to parent paragraph.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # This resource represents run of text contained in the document.
    api_response = api_instance.get_document_paragraph_run(name, paragraph_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_paragraph_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **paragraph_path** | **str**| Path to parent paragraph. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**RunResponse**](RunResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_paragraph_run_font**
> FontResponse get_document_paragraph_run_font(name, paragraph_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

This resource represents font of run.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
paragraph_path = 'paragraph_path_example' # str | Path to parent paragraph.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # This resource represents font of run.
    api_response = api_instance.get_document_paragraph_run_font(name, paragraph_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_paragraph_run_font: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **paragraph_path** | **str**| Path to parent paragraph. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**FontResponse**](FontResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_paragraph_runs**
> RunsResponse get_document_paragraph_runs(name, paragraph_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

This resource represents collection of runs in the paragraph.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
paragraph_path = 'paragraph_path_example' # str | Path to parent paragraph.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # This resource represents collection of runs in the paragraph.
    api_response = api_instance.get_document_paragraph_runs(name, paragraph_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_paragraph_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **paragraph_path** | **str**| Path to parent paragraph. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**RunsResponse**](RunsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_paragraphs**
> ParagraphLinkCollectionResponse get_document_paragraphs(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)

Return a list of paragraphs that are contained in the document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
node_path = 'node_path_example' # str | Path to node which contains paragraphs. (optional)

try:
    # Return a list of paragraphs that are contained in the document.
    api_response = api_instance.get_document_paragraphs(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_paragraphs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **node_path** | **str**| Path to node which contains paragraphs. | [optional] 

### Return type

[**ParagraphLinkCollectionResponse**](ParagraphLinkCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_properties**
> DocumentPropertiesResponse get_document_properties(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Read document properties info.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document's name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Read document properties info.
    api_response = api_instance.get_document_properties(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document&#39;s name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**DocumentPropertiesResponse**](DocumentPropertiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_property**
> DocumentPropertyResponse get_document_property(name, property_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Read document property info by the property name.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
property_name = 'property_name_example' # str | The property name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Read document property info by the property name.
    api_response = api_instance.get_document_property(name, property_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **property_name** | **str**| The property name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**DocumentPropertyResponse**](DocumentPropertyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_protection**
> ProtectionDataResponse get_document_protection(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Read document protection common info.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Read document protection common info.
    api_response = api_instance.get_document_protection(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_protection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**ProtectionDataResponse**](ProtectionDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_statistics**
> StatDataResponse get_document_statistics(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, include_comments=include_comments, include_footnotes=include_footnotes, include_text_in_shapes=include_text_in_shapes)

Read document statistics.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
include_comments = false # bool | Support including/excluding comments from the WordCount. Default value is \"true\". (optional) (default to false)
include_footnotes = false # bool | Support including/excluding footnotes from the WordCount. Default value is \"false\". (optional) (default to false)
include_text_in_shapes = false # bool | Support including/excluding shape's text from the WordCount. Default value is \"false\" (optional) (default to false)

try:
    # Read document statistics.
    api_response = api_instance.get_document_statistics(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, include_comments=include_comments, include_footnotes=include_footnotes, include_text_in_shapes=include_text_in_shapes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **include_comments** | **bool**| Support including/excluding comments from the WordCount. Default value is \&quot;true\&quot;. | [optional] [default to false]
 **include_footnotes** | **bool**| Support including/excluding footnotes from the WordCount. Default value is \&quot;false\&quot;. | [optional] [default to false]
 **include_text_in_shapes** | **bool**| Support including/excluding shape&#39;s text from the WordCount. Default value is \&quot;false\&quot; | [optional] [default to false]

### Return type

[**StatDataResponse**](StatDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_text_items**
> TextItemsResponse get_document_text_items(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Read document text items.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Read document text items.
    api_response = api_instance.get_document_text_items(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_text_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**TextItemsResponse**](TextItemsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_with_format**
> file get_document_with_format(name, format, folder=folder, storage=storage, load_encoding=load_encoding, password=password, out_path=out_path, fonts_location=fonts_location)

Export the document into the specified format.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The file name.
format = 'format_example' # str | The destination format.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
out_path = 'out_path_example' # str | Path to save result (optional)
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Export the document into the specified format.
    api_response = api_instance.get_document_with_format(name, format, folder=folder, storage=storage, load_encoding=load_encoding, password=password, out_path=out_path, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_with_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **format** | **str**| The destination format. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **out_path** | **str**| Path to save result | [optional] 
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_field**
> FieldResponse get_field(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)

Get field from document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The file name.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
node_path = 'node_path_example' # str | Path to node, which contains collection of fields. (optional)

try:
    # Get field from document.
    api_response = api_instance.get_field(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **node_path** | **str**| Path to node, which contains collection of fields. | [optional] 

### Return type

[**FieldResponse**](FieldResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fields**
> FieldsResponse get_fields(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)

Get fields from document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The file name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
node_path = 'node_path_example' # str | Path to node, which contains collection of fields. (optional)

try:
    # Get fields from document.
    api_response = api_instance.get_fields(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **node_path** | **str**| Path to node, which contains collection of fields. | [optional] 

### Return type

[**FieldsResponse**](FieldsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footnote**
> FootnoteResponse get_footnote(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)

Read footnote by index.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
node_path = 'node_path_example' # str | Path to node, which contains collection of footnotes. (optional)

try:
    # Read footnote by index.
    api_response = api_instance.get_footnote(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_footnote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **node_path** | **str**| Path to node, which contains collection of footnotes. | [optional] 

### Return type

[**FootnoteResponse**](FootnoteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footnotes**
> FootnotesResponse get_footnotes(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)

Get footnotes from document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The file name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
node_path = 'node_path_example' # str | Path to node, which contains collection of footnotes. (optional)

try:
    # Get footnotes from document.
    api_response = api_instance.get_footnotes(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_footnotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **node_path** | **str**| Path to node, which contains collection of footnotes. | [optional] 

### Return type

[**FootnotesResponse**](FootnotesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_form_field**
> FormFieldResponse get_form_field(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)

Returns representation of an one of the form field.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
node_path = 'node_path_example' # str | Path to node that contains collection of formfields. (optional)

try:
    # Returns representation of an one of the form field.
    api_response = api_instance.get_form_field(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_form_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **node_path** | **str**| Path to node that contains collection of formfields. | [optional] 

### Return type

[**FormFieldResponse**](FormFieldResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_form_fields**
> FormFieldsResponse get_form_fields(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)

Get form fields from document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The file name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
node_path = 'node_path_example' # str | Path to node containing collection of form fields. (optional)

try:
    # Get form fields from document.
    api_response = api_instance.get_form_fields(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_form_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **node_path** | **str**| Path to node containing collection of form fields. | [optional] 

### Return type

[**FormFieldsResponse**](FormFieldsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_header_footer**
> HeaderFooterResponse get_header_footer(name, header_footer_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, filter_by_type=filter_by_type)

Return a header/footer that is contained in the document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
header_footer_index = 56 # int | Header/footer index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
filter_by_type = 'filter_by_type_example' # str | List of types of headers and footers. (optional)

try:
    # Return a header/footer that is contained in the document.
    api_response = api_instance.get_header_footer(name, header_footer_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, filter_by_type=filter_by_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_header_footer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **header_footer_index** | **int**| Header/footer index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **filter_by_type** | **str**| List of types of headers and footers. | [optional] 

### Return type

[**HeaderFooterResponse**](HeaderFooterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_header_footer_of_section**
> HeaderFooterResponse get_header_footer_of_section(name, header_footer_index, section_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, filter_by_type=filter_by_type)

Return a header/footer that is contained in the document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
header_footer_index = 56 # int | Header/footer index.
section_index = 56 # int | Section index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
filter_by_type = 'filter_by_type_example' # str | List of types of headers and footers. (optional)

try:
    # Return a header/footer that is contained in the document.
    api_response = api_instance.get_header_footer_of_section(name, header_footer_index, section_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, filter_by_type=filter_by_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_header_footer_of_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **header_footer_index** | **int**| Header/footer index. | 
 **section_index** | **int**| Section index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **filter_by_type** | **str**| List of types of headers and footers. | [optional] 

### Return type

[**HeaderFooterResponse**](HeaderFooterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_header_footers**
> HeaderFootersResponse get_header_footers(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, section_path=section_path, filter_by_type=filter_by_type)

Return a list of header/footers that are contained in the document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
section_path = 'section_path_example' # str | Path to parent section. (optional)
filter_by_type = 'filter_by_type_example' # str | List of types of headers and footers. (optional)

try:
    # Return a list of header/footers that are contained in the document.
    api_response = api_instance.get_header_footers(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, section_path=section_path, filter_by_type=filter_by_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_header_footers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **section_path** | **str**| Path to parent section. | [optional] 
 **filter_by_type** | **str**| List of types of headers and footers. | [optional] 

### Return type

[**HeaderFootersResponse**](HeaderFootersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_office_math_object**
> OfficeMathObjectResponse get_office_math_object(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)

Read OfficeMath object by index.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
node_path = 'node_path_example' # str | Path to node, which contains collection of OfficeMath objects. (optional)

try:
    # Read OfficeMath object by index.
    api_response = api_instance.get_office_math_object(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_office_math_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **node_path** | **str**| Path to node, which contains collection of OfficeMath objects. | [optional] 

### Return type

[**OfficeMathObjectResponse**](OfficeMathObjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_office_math_objects**
> OfficeMathObjectsResponse get_office_math_objects(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)

Get OfficeMath objects from document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The file name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
node_path = 'node_path_example' # str | Path to node, which contains collection of OfficeMath objects. (optional)

try:
    # Get OfficeMath objects from document.
    api_response = api_instance.get_office_math_objects(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_office_math_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **node_path** | **str**| Path to node, which contains collection of OfficeMath objects. | [optional] 

### Return type

[**OfficeMathObjectsResponse**](OfficeMathObjectsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section**
> SectionResponse get_section(name, section_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Get document section by index.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
section_index = 56 # int | Section index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Get document section by index.
    api_response = api_instance.get_section(name, section_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **section_index** | **int**| Section index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**SectionResponse**](SectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section_page_setup**
> SectionPageSetupResponse get_section_page_setup(name, section_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Get page setup of section.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
section_index = 56 # int | Section index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Get page setup of section.
    api_response = api_instance.get_section_page_setup(name, section_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_section_page_setup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **section_index** | **int**| Section index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**SectionPageSetupResponse**](SectionPageSetupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sections**
> SectionLinkCollectionResponse get_sections(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Return a list of sections that are contained in the document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Return a list of sections that are contained in the document.
    api_response = api_instance.get_sections(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_sections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**SectionLinkCollectionResponse**](SectionLinkCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table**
> TableResponse get_table(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)

Return a table.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
node_path = 'node_path_example' # str | Path to node, which contains tables. (optional)

try:
    # Return a table.
    api_response = api_instance.get_table(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **node_path** | **str**| Path to node, which contains tables. | [optional] 

### Return type

[**TableResponse**](TableResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table_cell**
> TableCellResponse get_table_cell(name, table_row_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Return a table cell.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
table_row_path = 'table_row_path_example' # str | Path to table row.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Return a table cell.
    api_response = api_instance.get_table_cell(name, table_row_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_table_cell: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **table_row_path** | **str**| Path to table row. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**TableCellResponse**](TableCellResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table_cell_format**
> TableCellFormatResponse get_table_cell_format(name, table_row_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Return a table cell format.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
table_row_path = 'table_row_path_example' # str | Path to table row.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Return a table cell format.
    api_response = api_instance.get_table_cell_format(name, table_row_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_table_cell_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **table_row_path** | **str**| Path to table row. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**TableCellFormatResponse**](TableCellFormatResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table_properties**
> TablePropertiesResponse get_table_properties(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)

Return a table properties.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
node_path = 'node_path_example' # str | Path to node, which contains tables. (optional)

try:
    # Return a table properties.
    api_response = api_instance.get_table_properties(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_table_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **node_path** | **str**| Path to node, which contains tables. | [optional] 

### Return type

[**TablePropertiesResponse**](TablePropertiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table_row**
> TableRowResponse get_table_row(name, table_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Return a table row.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
table_path = 'table_path_example' # str | Path to table.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Return a table row.
    api_response = api_instance.get_table_row(name, table_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_table_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **table_path** | **str**| Path to table. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**TableRowResponse**](TableRowResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table_row_format**
> TableRowFormatResponse get_table_row_format(name, table_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Return a table row format.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
table_path = 'table_path_example' # str | Path to table.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Return a table row format.
    api_response = api_instance.get_table_row_format(name, table_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_table_row_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **table_path** | **str**| Path to table. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**TableRowFormatResponse**](TableRowFormatResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tables**
> TableLinkCollectionResponse get_tables(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)

Return a list of tables that are contained in the document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
node_path = 'node_path_example' # str | Path to node, which contains tables. (optional)

try:
    # Return a list of tables that are contained in the document.
    api_response = api_instance.get_tables(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_tables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **node_path** | **str**| Path to node, which contains tables. | [optional] 

### Return type

[**TableLinkCollectionResponse**](TableLinkCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_table**
> TableResponse insert_table(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, table=table, node_path=node_path)

Adds table to document, returns added table's data.             

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
table = aspose-words-cloud.TableInsert() # TableInsert | Table parameters/ (optional)
node_path = 'node_path_example' # str | Path to node, which contains tables. (optional)

try:
    # Adds table to document, returns added table's data.             
    api_response = api_instance.insert_table(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, table=table, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **table** | [**TableInsert**](TableInsert.md)| Table parameters/ | [optional] 
 **node_path** | **str**| Path to node, which contains tables. | [optional] 

### Return type

[**TableResponse**](TableResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_table_cell**
> TableCellResponse insert_table_cell(name, table_row_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, cell=cell)

Adds table cell to table, returns added cell's data.             

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
table_row_path = 'table_row_path_example' # str | Path to table row.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
cell = aspose-words-cloud.TableCellInsert() # TableCellInsert | Table cell parameters/ (optional)

try:
    # Adds table cell to table, returns added cell's data.             
    api_response = api_instance.insert_table_cell(name, table_row_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, cell=cell)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_table_cell: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **table_row_path** | **str**| Path to table row. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **cell** | [**TableCellInsert**](TableCellInsert.md)| Table cell parameters/ | [optional] 

### Return type

[**TableCellResponse**](TableCellResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_table_row**
> TableRowResponse insert_table_row(name, table_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, row=row)

Adds table row to table, returns added row's data.             

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
table_path = 'table_path_example' # str | Path to table.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
row = aspose-words-cloud.TableRowInsert() # TableRowInsert | Table row parameters/ (optional)

try:
    # Adds table row to table, returns added row's data.             
    api_response = api_instance.insert_table_row(name, table_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, row=row)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_table_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **table_path** | **str**| Path to table. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **row** | [**TableRowInsert**](TableRowInsert.md)| Table row parameters/ | [optional] 

### Return type

[**TableRowResponse**](TableRowResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_append_document**
> DocumentResponse post_append_document(name, document_list, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Append documents to original document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | Original document name.
document_list = aspose-words-cloud.DocumentEntryList() # DocumentEntryList | with a list of documents to append.            
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Append documents to original document.
    api_response = api_instance.post_append_document(name, document_list, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->post_append_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Original document name. | 
 **document_list** | [**DocumentEntryList**](DocumentEntryList.md)| with a list of documents to append.             | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_change_document_protection**
> ProtectionDataResponse post_change_document_protection(name, protection_request, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)

Change document protection.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
protection_request = aspose-words-cloud.ProtectionRequest() # ProtectionRequest | with protection settings.            
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)

try:
    # Change document protection.
    api_response = api_instance.post_change_document_protection(name, protection_request, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->post_change_document_protection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **protection_request** | [**ProtectionRequest**](ProtectionRequest.md)| with protection settings.             | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 

### Return type

[**ProtectionDataResponse**](ProtectionDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_comment**
> CommentResponse post_comment(name, comment_index, comment, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates the comment, returns updated comment's data.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
comment_index = 56 # int | Comment index
comment = aspose-words-cloud.Comment() # Comment | Comment data.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates the comment, returns updated comment's data.
    api_response = api_instance.post_comment(name, comment_index, comment, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->post_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **comment_index** | **int**| Comment index | 
 **comment** | [**Comment**](Comment.md)| Comment data. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**CommentResponse**](CommentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_compare_document**
> DocumentResponse post_compare_document(name, compare_data, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)

Compare document with original document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | Original document name.
compare_data = aspose-words-cloud.CompareData() # CompareData | with a document to compare.            
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)

try:
    # Compare document with original document.
    api_response = api_instance.post_compare_document(name, compare_data, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->post_compare_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Original document name. | 
 **compare_data** | [**CompareData**](CompareData.md)| with a document to compare.             | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_document_execute_mail_merge**
> DocumentResponse post_document_execute_mail_merge(name, data=data, folder=folder, storage=storage, load_encoding=load_encoding, password=password, with_regions=with_regions, mail_merge_data_file=mail_merge_data_file, cleanup=cleanup, use_whole_paragraph_as_region=use_whole_paragraph_as_region, dest_file_name=dest_file_name)

Execute document mail merge operation.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
data = 'data_example' # str | Mail merge data (optional)
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
with_regions = false # bool | With regions flag. (optional) (default to false)
mail_merge_data_file = 'mail_merge_data_file_example' # str | Mail merge data. (optional)
cleanup = 'cleanup_example' # str | Clean up options. (optional)
use_whole_paragraph_as_region = true # bool | Gets or sets a value indicating whether paragraph with TableStart or              TableEnd field should be fully included into mail merge region or particular range between TableStart and TableEnd fields.              The default value is true. (optional) (default to true)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved with autogenerated name. (optional)

try:
    # Execute document mail merge operation.
    api_response = api_instance.post_document_execute_mail_merge(name, data=data, folder=folder, storage=storage, load_encoding=load_encoding, password=password, with_regions=with_regions, mail_merge_data_file=mail_merge_data_file, cleanup=cleanup, use_whole_paragraph_as_region=use_whole_paragraph_as_region, dest_file_name=dest_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->post_document_execute_mail_merge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **data** | **str**| Mail merge data | [optional] 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **with_regions** | **bool**| With regions flag. | [optional] [default to false]
 **mail_merge_data_file** | **str**| Mail merge data. | [optional] 
 **cleanup** | **str**| Clean up options. | [optional] 
 **use_whole_paragraph_as_region** | **bool**| Gets or sets a value indicating whether paragraph with TableStart or              TableEnd field should be fully included into mail merge region or particular range between TableStart and TableEnd fields.              The default value is true. | [optional] [default to true]
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved with autogenerated name. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_document_paragraph_format**
> ParagraphFormatResponse post_document_paragraph_format(name, dto, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates paragrpaph format properties, returns updated format properties.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
dto = aspose-words-cloud.ParagraphFormat() # ParagraphFormat | Paragraph format object
node_path = 'node_path_example' # str | Path to node which contains paragraphs.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates paragrpaph format properties, returns updated format properties.
    api_response = api_instance.post_document_paragraph_format(name, dto, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->post_document_paragraph_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **dto** | [**ParagraphFormat**](ParagraphFormat.md)| Paragraph format object | 
 **node_path** | **str**| Path to node which contains paragraphs. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**ParagraphFormatResponse**](ParagraphFormatResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_document_paragraph_run_font**
> FontResponse post_document_paragraph_run_font(name, font_dto, paragraph_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates font properties, returns updated font data.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
font_dto = aspose-words-cloud.Font() # Font | Font dto object
paragraph_path = 'paragraph_path_example' # str | Path to parent paragraph.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates font properties, returns updated font data.
    api_response = api_instance.post_document_paragraph_run_font(name, font_dto, paragraph_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->post_document_paragraph_run_font: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **font_dto** | [**Font**](Font.md)| Font dto object | 
 **paragraph_path** | **str**| Path to parent paragraph. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**FontResponse**](FontResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_document_save_as**
> SaveResponse post_document_save_as(name, save_options_data, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, fonts_location=fonts_location)

Convert document to destination format with detailed settings and save result to storage.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
save_options_data = aspose-words-cloud.SaveOptionsData() # SaveOptionsData | Save options.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Convert document to destination format with detailed settings and save result to storage.
    api_response = api_instance.post_document_save_as(name, save_options_data, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->post_document_save_as: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **save_options_data** | [**SaveOptionsData**](SaveOptionsData.md)| Save options. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

[**SaveResponse**](SaveResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_drawing_object**
> DrawingObjectResponse post_drawing_object(name, drawing_object, image_file, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)

Updates drawing object, returns updated  drawing object's data.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
drawing_object = 'drawing_object_example' # str | Drawing object parameters
image_file = '/path/to/file.txt' # file | File with image
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
node_path = 'node_path_example' # str | Path to node, which contains collection of drawing objects. (optional)

try:
    # Updates drawing object, returns updated  drawing object's data.
    api_response = api_instance.post_drawing_object(name, drawing_object, image_file, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->post_drawing_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **drawing_object** | **str**| Drawing object parameters | 
 **image_file** | **file**| File with image | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **node_path** | **str**| Path to node, which contains collection of drawing objects. | [optional] 

### Return type

[**DrawingObjectResponse**](DrawingObjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_execute_template**
> DocumentResponse post_execute_template(name, data, folder=folder, storage=storage, load_encoding=load_encoding, password=password, cleanup=cleanup, use_whole_paragraph_as_region=use_whole_paragraph_as_region, with_regions=with_regions, dest_file_name=dest_file_name)

Populate document template with data.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The template document name.
data = 'data_example' # str | Mail merge data
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
cleanup = 'cleanup_example' # str | Clean up options. (optional)
use_whole_paragraph_as_region = true # bool | Gets or sets a value indicating whether paragraph with TableStart or  TableEnd field should be fully included into mail merge region or particular range between TableStart and TableEnd fields.   The default value is true. (optional) (default to true)
with_regions = true # bool | Merge with regions or not. True by default (optional) (default to true)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved with autogenerated name. (optional)

try:
    # Populate document template with data.
    api_response = api_instance.post_execute_template(name, data, folder=folder, storage=storage, load_encoding=load_encoding, password=password, cleanup=cleanup, use_whole_paragraph_as_region=use_whole_paragraph_as_region, with_regions=with_regions, dest_file_name=dest_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->post_execute_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The template document name. | 
 **data** | **str**| Mail merge data | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **cleanup** | **str**| Clean up options. | [optional] 
 **use_whole_paragraph_as_region** | **bool**| Gets or sets a value indicating whether paragraph with TableStart or  TableEnd field should be fully included into mail merge region or particular range between TableStart and TableEnd fields.   The default value is true. | [optional] [default to true]
 **with_regions** | **bool**| Merge with regions or not. True by default | [optional] [default to true]
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved with autogenerated name. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_field**
> FieldResponse post_field(name, field, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)

Updates field's properties, returns updated field's data.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
field = aspose-words-cloud.Field() # Field | Field data.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
node_path = 'node_path_example' # str | Path to node, which contains collection of fields. (optional)

try:
    # Updates field's properties, returns updated field's data.
    api_response = api_instance.post_field(name, field, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->post_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **field** | [**Field**](Field.md)| Field data. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **node_path** | **str**| Path to node, which contains collection of fields. | [optional] 

### Return type

[**FieldResponse**](FieldResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_footnote**
> FootnoteResponse post_footnote(name, footnote_dto, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)

Updates footnote's properties, returns updated run's data.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
footnote_dto = aspose-words-cloud.Footnote() # Footnote | Footnote data.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
node_path = 'node_path_example' # str | Path to node, which contains collection of footnotes. (optional)

try:
    # Updates footnote's properties, returns updated run's data.
    api_response = api_instance.post_footnote(name, footnote_dto, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->post_footnote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **footnote_dto** | [**Footnote**](Footnote.md)| Footnote data. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **node_path** | **str**| Path to node, which contains collection of footnotes. | [optional] 

### Return type

[**FootnoteResponse**](FootnoteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_form_field**
> FormFieldResponse post_form_field(name, form_field, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)

Updates properties of form field, returns updated form field.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
form_field = aspose-words-cloud.FormField() # FormField | From field data.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
node_path = 'node_path_example' # str | Path to node that contains collection of formfields. (optional)

try:
    # Updates properties of form field, returns updated form field.
    api_response = api_instance.post_form_field(name, form_field, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->post_form_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **form_field** | [**FormField**](FormField.md)| From field data. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **node_path** | **str**| Path to node that contains collection of formfields. | [optional] 

### Return type

[**FormFieldResponse**](FormFieldResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_insert_document_watermark_image**
> DocumentResponse post_insert_document_watermark_image(name, image_file=image_file, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, rotation_angle=rotation_angle, image=image)

Insert document watermark image.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
image_file = '/path/to/file.txt' # file | File with image (optional)
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
rotation_angle = 0.0 # float | The watermark rotation angle. (optional) (default to 0.0)
image = 'image_example' # str | The image file server full name. If the name is empty the image is expected in request content. (optional)

try:
    # Insert document watermark image.
    api_response = api_instance.post_insert_document_watermark_image(name, image_file=image_file, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, rotation_angle=rotation_angle, image=image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->post_insert_document_watermark_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_file** | **file**| File with image | [optional] 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **rotation_angle** | **float**| The watermark rotation angle. | [optional] [default to 0.0]
 **image** | **str**| The image file server full name. If the name is empty the image is expected in request content. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_insert_document_watermark_text**
> DocumentResponse post_insert_document_watermark_text(name, watermark_text, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Insert document watermark text.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
watermark_text = aspose-words-cloud.WatermarkText() # WatermarkText | with the watermark data.            
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Insert document watermark text.
    api_response = api_instance.post_insert_document_watermark_text(name, watermark_text, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->post_insert_document_watermark_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **watermark_text** | [**WatermarkText**](WatermarkText.md)| with the watermark data.             | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_insert_page_numbers**
> DocumentResponse post_insert_page_numbers(name, page_number, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Insert document page numbers.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | A document name.
page_number = aspose-words-cloud.PageNumber() # PageNumber | with the page numbers settings.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Insert document page numbers.
    api_response = api_instance.post_insert_page_numbers(name, page_number, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->post_insert_page_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A document name. | 
 **page_number** | [**PageNumber**](PageNumber.md)| with the page numbers settings. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_load_web_document**
> SaveResponse post_load_web_document(data, storage=storage)

Loads new document from web into the file with any supported format of data.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
data = aspose-words-cloud.LoadWebDocumentData() # LoadWebDocumentData | Parameters of loading.
storage = 'storage_example' # str | File storage, which have to be used. (optional)

try:
    # Loads new document from web into the file with any supported format of data.
    api_response = api_instance.post_load_web_document(data, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->post_load_web_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**LoadWebDocumentData**](LoadWebDocumentData.md)| Parameters of loading. | 
 **storage** | **str**| File storage, which have to be used. | [optional] 

### Return type

[**SaveResponse**](SaveResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_replace_text**
> ReplaceTextResponse post_replace_text(name, replace_text, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Replace document text.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
replace_text = aspose-words-cloud.ReplaceTextRequest() # ReplaceTextRequest | with the replace operation settings.            
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Replace document text.
    api_response = api_instance.post_replace_text(name, replace_text, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->post_replace_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **replace_text** | [**ReplaceTextRequest**](ReplaceTextRequest.md)| with the replace operation settings.             | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**ReplaceTextResponse**](ReplaceTextResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_run**
> RunResponse post_run(name, run, paragraph_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates run's properties, returns updated run's data.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
run = aspose-words-cloud.Run() # Run | Run data.
paragraph_path = 'paragraph_path_example' # str | Path to parent paragraph.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates run's properties, returns updated run's data.
    api_response = api_instance.post_run(name, run, paragraph_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->post_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **run** | [**Run**](Run.md)| Run data. | 
 **paragraph_path** | **str**| Path to parent paragraph. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**RunResponse**](RunResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_split_document**
> SplitDocumentResponse post_split_document(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, format=format, _from=_from, to=to, zip_output=zip_output, fonts_location=fonts_location)

Split document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | Original document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
format = 'format_example' # str | Format to split. (optional)
_from = 56 # int | Start page. (optional)
to = 56 # int | End page. (optional)
zip_output = false # bool | ZipOutput or not. (optional) (default to false)
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Split document.
    api_response = api_instance.post_split_document(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, format=format, _from=_from, to=to, zip_output=zip_output, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->post_split_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Original document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **format** | **str**| Format to split. | [optional] 
 **_from** | **int**| Start page. | [optional] 
 **to** | **int**| End page. | [optional] 
 **zip_output** | **bool**| ZipOutput or not. | [optional] [default to false]
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

[**SplitDocumentResponse**](SplitDocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_update_document_bookmark**
> BookmarkResponse post_update_document_bookmark(name, bookmark_data, bookmark_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Update document bookmark.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
bookmark_data = aspose-words-cloud.BookmarkData() # BookmarkData | with new bookmark data.            
bookmark_name = 'bookmark_name_example' # str | The bookmark name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Update document bookmark.
    api_response = api_instance.post_update_document_bookmark(name, bookmark_data, bookmark_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->post_update_document_bookmark: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **bookmark_data** | [**BookmarkData**](BookmarkData.md)| with new bookmark data.             | 
 **bookmark_name** | **str**| The bookmark name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**BookmarkResponse**](BookmarkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_update_document_fields**
> DocumentResponse post_update_document_fields(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)

Update (reevaluate) fields in document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)

try:
    # Update (reevaluate) fields in document.
    api_response = api_instance.post_update_document_fields(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->post_update_document_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_comment**
> CommentResponse put_comment(name, comment, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Adds comment to document, returns inserted comment's data.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
comment = aspose-words-cloud.Comment() # Comment | Comment data.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Adds comment to document, returns inserted comment's data.
    api_response = api_instance.put_comment(name, comment, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->put_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **comment** | [**Comment**](Comment.md)| Comment data. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**CommentResponse**](CommentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_convert_document**
> file put_convert_document(document, format, storage=storage, out_path=out_path, document_file_name=document_file_name, fonts_location=fonts_location)

Convert document from request content to format specified.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
document = '/path/to/file.txt' # file | Converting document
format = 'format_example' # str | Format to convert.
storage = 'storage_example' # str | File storage, which have to be used. (optional)
out_path = 'out_path_example' # str | Path for saving operation result to the local storage. (optional)
document_file_name = 'sourceFilename' # str | This file name will be used when resulting document has dynamic field for document file name {filename}. If it is not setted, \"sourceFilename\" will be used instead.  (optional) (default to sourceFilename)
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Convert document from request content to format specified.
    api_response = api_instance.put_convert_document(document, format, storage=storage, out_path=out_path, document_file_name=document_file_name, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->put_convert_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document** | **file**| Converting document | 
 **format** | **str**| Format to convert. | 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **out_path** | **str**| Path for saving operation result to the local storage. | [optional] 
 **document_file_name** | **str**| This file name will be used when resulting document has dynamic field for document file name {filename}. If it is not setted, \&quot;sourceFilename\&quot; will be used instead.  | [optional] [default to sourceFilename]
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_create_document**
> DocumentResponse put_create_document(storage=storage, file_name=file_name, folder=folder)

Creates new document. Document is created with format which is recognized from file extensions.  Supported extentions: \".doc\", \".docx\", \".docm\", \".dot\", \".dotm\", \".dotx\", \".flatopc\", \".fopc\", \".flatopc_macro\", \".fopc_macro\", \".flatopc_template\", \".fopc_template\", \".flatopc_template_macro\", \".fopc_template_macro\", \".wordml\", \".wml\", \".rtf\"

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
storage = 'storage_example' # str | File storage, which have to be used. (optional)
file_name = 'file_name_example' # str | The file name. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Creates new document. Document is created with format which is recognized from file extensions.  Supported extentions: \".doc\", \".docx\", \".docm\", \".dot\", \".dotm\", \".dotx\", \".flatopc\", \".fopc\", \".flatopc_macro\", \".fopc_macro\", \".flatopc_template\", \".fopc_template\", \".flatopc_template_macro\", \".fopc_template_macro\", \".wordml\", \".wml\", \".rtf\"
    api_response = api_instance.put_create_document(storage=storage, file_name=file_name, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->put_create_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **file_name** | **str**| The file name. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_document_field_names**
> FieldNamesResponse put_document_field_names(template, use_non_merge_fields=use_non_merge_fields)

Read document field names.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
template = '/path/to/file.txt' # file | File with template
use_non_merge_fields = false # bool | Use non merge fields or not. (optional) (default to false)

try:
    # Read document field names.
    api_response = api_instance.put_document_field_names(template, use_non_merge_fields=use_non_merge_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->put_document_field_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | **file**| File with template | 
 **use_non_merge_fields** | **bool**| Use non merge fields or not. | [optional] [default to false]

### Return type

[**FieldNamesResponse**](FieldNamesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_document_save_as_tiff**
> SaveResponse put_document_save_as_tiff(name, save_options, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, result_file=result_file, use_anti_aliasing=use_anti_aliasing, use_high_quality_rendering=use_high_quality_rendering, image_brightness=image_brightness, image_color_mode=image_color_mode, image_contrast=image_contrast, numeral_format=numeral_format, page_count=page_count, page_index=page_index, paper_color=paper_color, pixel_format=pixel_format, resolution=resolution, scale=scale, tiff_compression=tiff_compression, dml_rendering_mode=dml_rendering_mode, dml_effects_rendering_mode=dml_effects_rendering_mode, tiff_binarization_method=tiff_binarization_method, zip_output=zip_output, fonts_location=fonts_location)

Convert document to tiff with detailed settings and save result to storage.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
save_options = aspose-words-cloud.TiffSaveOptionsData() # TiffSaveOptionsData | Tiff save options.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
result_file = 'result_file_example' # str | The resulting file name. (optional)
use_anti_aliasing = true # bool | Use antialiasing flag. (optional)
use_high_quality_rendering = true # bool | Use high quality flag. (optional)
image_brightness = 1.2 # float | Brightness for the generated images. (optional)
image_color_mode = 'image_color_mode_example' # str | Color mode for the generated images. (optional)
image_contrast = 1.2 # float | The contrast for the generated images. (optional)
numeral_format = 'numeral_format_example' # str | The images numeral format. (optional)
page_count = 56 # int | Number of pages to render. (optional)
page_index = 56 # int | Page index to start rendering. (optional)
paper_color = 'paper_color_example' # str | Background image color. (optional)
pixel_format = 'pixel_format_example' # str | The pixel format of generated images. (optional)
resolution = 1.2 # float | The resolution of generated images. (optional)
scale = 1.2 # float | Zoom factor for generated images. (optional)
tiff_compression = 'tiff_compression_example' # str | The compression tipe. (optional)
dml_rendering_mode = 'dml_rendering_mode_example' # str | Optional, default is Fallback. (optional)
dml_effects_rendering_mode = 'dml_effects_rendering_mode_example' # str | Optional, default is Simplified. (optional)
tiff_binarization_method = 'tiff_binarization_method_example' # str | Optional, Tiff binarization method, possible values are: FloydSteinbergDithering, Threshold. (optional)
zip_output = true # bool | Optional. A value determining zip output or not. (optional)
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Convert document to tiff with detailed settings and save result to storage.
    api_response = api_instance.put_document_save_as_tiff(name, save_options, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, result_file=result_file, use_anti_aliasing=use_anti_aliasing, use_high_quality_rendering=use_high_quality_rendering, image_brightness=image_brightness, image_color_mode=image_color_mode, image_contrast=image_contrast, numeral_format=numeral_format, page_count=page_count, page_index=page_index, paper_color=paper_color, pixel_format=pixel_format, resolution=resolution, scale=scale, tiff_compression=tiff_compression, dml_rendering_mode=dml_rendering_mode, dml_effects_rendering_mode=dml_effects_rendering_mode, tiff_binarization_method=tiff_binarization_method, zip_output=zip_output, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->put_document_save_as_tiff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **save_options** | [**TiffSaveOptionsData**](TiffSaveOptionsData.md)| Tiff save options. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **result_file** | **str**| The resulting file name. | [optional] 
 **use_anti_aliasing** | **bool**| Use antialiasing flag. | [optional] 
 **use_high_quality_rendering** | **bool**| Use high quality flag. | [optional] 
 **image_brightness** | **float**| Brightness for the generated images. | [optional] 
 **image_color_mode** | **str**| Color mode for the generated images. | [optional] 
 **image_contrast** | **float**| The contrast for the generated images. | [optional] 
 **numeral_format** | **str**| The images numeral format. | [optional] 
 **page_count** | **int**| Number of pages to render. | [optional] 
 **page_index** | **int**| Page index to start rendering. | [optional] 
 **paper_color** | **str**| Background image color. | [optional] 
 **pixel_format** | **str**| The pixel format of generated images. | [optional] 
 **resolution** | **float**| The resolution of generated images. | [optional] 
 **scale** | **float**| Zoom factor for generated images. | [optional] 
 **tiff_compression** | **str**| The compression tipe. | [optional] 
 **dml_rendering_mode** | **str**| Optional, default is Fallback. | [optional] 
 **dml_effects_rendering_mode** | **str**| Optional, default is Simplified. | [optional] 
 **tiff_binarization_method** | **str**| Optional, Tiff binarization method, possible values are: FloydSteinbergDithering, Threshold. | [optional] 
 **zip_output** | **bool**| Optional. A value determining zip output or not. | [optional] 
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

[**SaveResponse**](SaveResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_drawing_object**
> DrawingObjectResponse put_drawing_object(name, drawing_object, image_file, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)

Adds  drawing object to document, returns added  drawing object's data.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
drawing_object = 'drawing_object_example' # str | Drawing object parameters
image_file = '/path/to/file.txt' # file | File with image
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
node_path = 'node_path_example' # str | Path to node, which contains collection of drawing objects. (optional)

try:
    # Adds  drawing object to document, returns added  drawing object's data.
    api_response = api_instance.put_drawing_object(name, drawing_object, image_file, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->put_drawing_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **drawing_object** | **str**| Drawing object parameters | 
 **image_file** | **file**| File with image | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **node_path** | **str**| Path to node, which contains collection of drawing objects. | [optional] 

### Return type

[**DrawingObjectResponse**](DrawingObjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_execute_mail_merge_online**
> file put_execute_mail_merge_online(template, data, with_regions=with_regions, cleanup=cleanup, document_file_name=document_file_name)

Execute document mail merge online.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
template = '/path/to/file.txt' # file | File with template
data = '/path/to/file.txt' # file | File with mailmerge data
with_regions = false # bool | With regions flag. (optional) (default to false)
cleanup = 'cleanup_example' # str | Clean up options. (optional)
document_file_name = 'template' # str | This file name will be used when resulting document has dynamic field for document file name {filename}. If it is not setted, \"template\" will be used instead.  (optional) (default to template)

try:
    # Execute document mail merge online.
    api_response = api_instance.put_execute_mail_merge_online(template, data, with_regions=with_regions, cleanup=cleanup, document_file_name=document_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->put_execute_mail_merge_online: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | **file**| File with template | 
 **data** | **file**| File with mailmerge data | 
 **with_regions** | **bool**| With regions flag. | [optional] [default to false]
 **cleanup** | **str**| Clean up options. | [optional] 
 **document_file_name** | **str**| This file name will be used when resulting document has dynamic field for document file name {filename}. If it is not setted, \&quot;template\&quot; will be used instead.  | [optional] [default to template]

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_execute_template_online**
> file put_execute_template_online(template, data, cleanup=cleanup, use_whole_paragraph_as_region=use_whole_paragraph_as_region, with_regions=with_regions, document_file_name=document_file_name)

Populate document template with data online.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
template = '/path/to/file.txt' # file | File with template
data = '/path/to/file.txt' # file | File with mailmerge data
cleanup = 'cleanup_example' # str | Clean up options. (optional)
use_whole_paragraph_as_region = true # bool | Gets or sets a value indicating whether paragraph with TableStart or              TableEnd field should be fully included into mail merge region or particular range between TableStart and TableEnd fields.              The default value is true. (optional) (default to true)
with_regions = true # bool | Merge with regions or not. True by default (optional) (default to true)
document_file_name = 'template' # str | This file name will be used when resulting document has dynamic field for document file name {filename}.  If it is not setted, \"template\" will be used instead.  Note: if withRegions == true executeTemplate updates fields only inside regions (optional) (default to template)

try:
    # Populate document template with data online.
    api_response = api_instance.put_execute_template_online(template, data, cleanup=cleanup, use_whole_paragraph_as_region=use_whole_paragraph_as_region, with_regions=with_regions, document_file_name=document_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->put_execute_template_online: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | **file**| File with template | 
 **data** | **file**| File with mailmerge data | 
 **cleanup** | **str**| Clean up options. | [optional] 
 **use_whole_paragraph_as_region** | **bool**| Gets or sets a value indicating whether paragraph with TableStart or              TableEnd field should be fully included into mail merge region or particular range between TableStart and TableEnd fields.              The default value is true. | [optional] [default to true]
 **with_regions** | **bool**| Merge with regions or not. True by default | [optional] [default to true]
 **document_file_name** | **str**| This file name will be used when resulting document has dynamic field for document file name {filename}.  If it is not setted, \&quot;template\&quot; will be used instead.  Note: if withRegions &#x3D;&#x3D; true executeTemplate updates fields only inside regions | [optional] [default to template]

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_field**
> FieldResponse put_field(name, field, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path, insert_before_node=insert_before_node)

Adds field to document, returns inserted field's data.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
field = aspose-words-cloud.Field() # Field | Field data.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
node_path = 'node_path_example' # str | Path to node, which contains collection of fields. (optional)
insert_before_node = 'insert_before_node_example' # str | Field will be inserted before node with id=\"nodeId\". (optional)

try:
    # Adds field to document, returns inserted field's data.
    api_response = api_instance.put_field(name, field, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path, insert_before_node=insert_before_node)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->put_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **field** | [**Field**](Field.md)| Field data. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **node_path** | **str**| Path to node, which contains collection of fields. | [optional] 
 **insert_before_node** | **str**| Field will be inserted before node with id&#x3D;\&quot;nodeId\&quot;. | [optional] 

### Return type

[**FieldResponse**](FieldResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_footnote**
> FootnoteResponse put_footnote(name, footnote_dto, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)

Adds footnote to document, returns added footnote's data.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
footnote_dto = aspose-words-cloud.Footnote() # Footnote | Footnote data.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
node_path = 'node_path_example' # str | Path to node, which contains collection of footnotes. (optional)

try:
    # Adds footnote to document, returns added footnote's data.
    api_response = api_instance.put_footnote(name, footnote_dto, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->put_footnote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **footnote_dto** | [**Footnote**](Footnote.md)| Footnote data. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **node_path** | **str**| Path to node, which contains collection of footnotes. | [optional] 

### Return type

[**FootnoteResponse**](FootnoteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_form_field**
> FormFieldResponse put_form_field(name, form_field, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path, insert_before_node=insert_before_node)

Adds form field to paragraph, returns added form field's data.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
form_field = aspose-words-cloud.FormField() # FormField | From field data.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
node_path = 'node_path_example' # str | Path to node that contains collection of formfields. (optional)
insert_before_node = 'insert_before_node_example' # str | Form field will be inserted before node with index. (optional)

try:
    # Adds form field to paragraph, returns added form field's data.
    api_response = api_instance.put_form_field(name, form_field, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path, insert_before_node=insert_before_node)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->put_form_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **form_field** | [**FormField**](FormField.md)| From field data. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **node_path** | **str**| Path to node that contains collection of formfields. | [optional] 
 **insert_before_node** | **str**| Form field will be inserted before node with index. | [optional] 

### Return type

[**FormFieldResponse**](FormFieldResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_header_footer**
> HeaderFooterResponse put_header_footer(name, header_footer_type, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, section_path=section_path)

Insert to document header or footer.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
header_footer_type = 'header_footer_type_example' # str | Type of header/footer.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
section_path = 'section_path_example' # str | Path to parent section. (optional)

try:
    # Insert to document header or footer.
    api_response = api_instance.put_header_footer(name, header_footer_type, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, section_path=section_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->put_header_footer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **header_footer_type** | **str**| Type of header/footer. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **section_path** | **str**| Path to parent section. | [optional] 

### Return type

[**HeaderFooterResponse**](HeaderFooterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_paragraph**
> ParagraphResponse put_paragraph(name, paragraph, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path, insert_before_node=insert_before_node)

Adds paragraph to document, returns added paragraph's data.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
paragraph = aspose-words-cloud.ParagraphInsert() # ParagraphInsert | Paragraph data.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
node_path = 'node_path_example' # str | Path to node which contains paragraphs. (optional)
insert_before_node = 'insert_before_node_example' # str | Paragraph will be inserted before node with index. (optional)

try:
    # Adds paragraph to document, returns added paragraph's data.
    api_response = api_instance.put_paragraph(name, paragraph, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, node_path=node_path, insert_before_node=insert_before_node)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->put_paragraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **paragraph** | [**ParagraphInsert**](ParagraphInsert.md)| Paragraph data. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **node_path** | **str**| Path to node which contains paragraphs. | [optional] 
 **insert_before_node** | **str**| Paragraph will be inserted before node with index. | [optional] 

### Return type

[**ParagraphResponse**](ParagraphResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_protect_document**
> ProtectionDataResponse put_protect_document(name, protection_request, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)

Protect document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
protection_request = aspose-words-cloud.ProtectionRequest() # ProtectionRequest | with protection settings.            
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)

try:
    # Protect document.
    api_response = api_instance.put_protect_document(name, protection_request, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->put_protect_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **protection_request** | [**ProtectionRequest**](ProtectionRequest.md)| with protection settings.             | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 

### Return type

[**ProtectionDataResponse**](ProtectionDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_run**
> RunResponse put_run(name, paragraph_path, run, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, insert_before_node=insert_before_node)

Adds run to document, returns added paragraph's data.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
paragraph_path = 'paragraph_path_example' # str | Path to parent paragraph.
run = aspose-words-cloud.Run() # Run | Run data.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
insert_before_node = 'insert_before_node_example' # str | Paragraph will be inserted before node with index. (optional)

try:
    # Adds run to document, returns added paragraph's data.
    api_response = api_instance.put_run(name, paragraph_path, run, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, insert_before_node=insert_before_node)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->put_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **paragraph_path** | **str**| Path to parent paragraph. | 
 **run** | [**Run**](Run.md)| Run data. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **insert_before_node** | **str**| Paragraph will be inserted before node with index. | [optional] 

### Return type

[**RunResponse**](RunResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_all_revisions**
> RevisionsModificationResponse reject_all_revisions(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)

Reject all revisions in document

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)

try:
    # Reject all revisions in document
    api_response = api_instance.reject_all_revisions(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->reject_all_revisions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 

### Return type

[**RevisionsModificationResponse**](RevisionsModificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_drawing_object**
> file render_drawing_object(name, format, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path, fonts_location=fonts_location)

Renders drawing object to specified format.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The file name.
format = 'format_example' # str | The destination format.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
node_path = 'node_path_example' # str | Path to node, which contains drawing objects. (optional)
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Renders drawing object to specified format.
    api_response = api_instance.render_drawing_object(name, format, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->render_drawing_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **format** | **str**| The destination format. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **node_path** | **str**| Path to node, which contains drawing objects. | [optional] 
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_math_object**
> file render_math_object(name, format, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path, fonts_location=fonts_location)

Renders math object to specified format.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The file name.
format = 'format_example' # str | The destination format.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
node_path = 'node_path_example' # str | Path to node, which contains office math objects. (optional)
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Renders math object to specified format.
    api_response = api_instance.render_math_object(name, format, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->render_math_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **format** | **str**| The destination format. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **node_path** | **str**| Path to node, which contains office math objects. | [optional] 
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_page**
> file render_page(name, page_index, format, folder=folder, storage=storage, load_encoding=load_encoding, password=password, fonts_location=fonts_location)

Renders page to specified format.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The file name.
page_index = 56 # int | Comment index
format = 'format_example' # str | The destination format.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Renders page to specified format.
    api_response = api_instance.render_page(name, page_index, format, folder=folder, storage=storage, load_encoding=load_encoding, password=password, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->render_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **page_index** | **int**| Comment index | 
 **format** | **str**| The destination format. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_paragraph**
> file render_paragraph(name, format, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path, fonts_location=fonts_location)

Renders paragraph to specified format.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The file name.
format = 'format_example' # str | The destination format.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
node_path = 'node_path_example' # str | Path to node, which contains paragraphs. (optional)
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Renders paragraph to specified format.
    api_response = api_instance.render_paragraph(name, format, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->render_paragraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **format** | **str**| The destination format. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **node_path** | **str**| Path to node, which contains paragraphs. | [optional] 
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_table**
> file render_table(name, format, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path, fonts_location=fonts_location)

Renders table to specified format.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The file name.
format = 'format_example' # str | The destination format.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
node_path = 'node_path_example' # str | Path to node, which contains tables. (optional)
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Renders table to specified format.
    api_response = api_instance.render_table(name, format, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, node_path=node_path, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->render_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **format** | **str**| The destination format. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **node_path** | **str**| Path to node, which contains tables. | [optional] 
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_cache**
> AsposeResponse reset_cache()

Resets font's cache.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()

try:
    # Resets font's cache.
    api_response = api_instance.reset_cache()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->reset_cache: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> SearchResponse search(name, pattern, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Search text in document.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
pattern = 'pattern_example' # str | The regular expression used to find matches.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Search text in document.
    api_response = api_instance.search(name, pattern, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **pattern** | **str**| The regular expression used to find matches. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_border**
> BorderResponse update_border(name, border_properties, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates border properties.             

'nodePath' should refer to node with cell or row

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
border_properties = aspose-words-cloud.Border() # Border | Border properties
node_path = 'node_path_example' # str | Path to node with border(node should be cell or row).
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates border properties.             
    api_response = api_instance.update_border(name, border_properties, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_border: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **border_properties** | [**Border**](Border.md)| Border properties | 
 **node_path** | **str**| Path to node with border(node should be cell or row). | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**BorderResponse**](BorderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_section_page_setup**
> SectionPageSetupResponse update_section_page_setup(name, section_index, page_setup, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Update page setup of section.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
section_index = 56 # int | Section index
page_setup = aspose-words-cloud.PageSetup() # PageSetup | Page setup properties dto
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Update page setup of section.
    api_response = api_instance.update_section_page_setup(name, section_index, page_setup, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_section_page_setup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **section_index** | **int**| Section index | 
 **page_setup** | [**PageSetup**](PageSetup.md)| Page setup properties dto | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**SectionPageSetupResponse**](SectionPageSetupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_table_cell_format**
> TableCellFormatResponse update_table_cell_format(name, table_row_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, format=format)

Updates a table cell format.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
table_row_path = 'table_row_path_example' # str | Path to table row.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
format = aspose-words-cloud.TableCellFormat() # TableCellFormat | The properties. (optional)

try:
    # Updates a table cell format.
    api_response = api_instance.update_table_cell_format(name, table_row_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_table_cell_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **table_row_path** | **str**| Path to table row. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **format** | [**TableCellFormat**](TableCellFormat.md)| The properties. | [optional] 

### Return type

[**TableCellFormatResponse**](TableCellFormatResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_table_properties**
> TablePropertiesResponse update_table_properties(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, properties=properties, node_path=node_path)

Updates a table properties.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
properties = aspose-words-cloud.TableProperties() # TableProperties | The properties. (optional)
node_path = 'node_path_example' # str | Path to node, which contains tables. (optional)

try:
    # Updates a table properties.
    api_response = api_instance.update_table_properties(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, properties=properties, node_path=node_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_table_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **properties** | [**TableProperties**](TableProperties.md)| The properties. | [optional] 
 **node_path** | **str**| Path to node, which contains tables. | [optional] 

### Return type

[**TablePropertiesResponse**](TablePropertiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_table_row_format**
> TableRowFormatResponse update_table_row_format(name, table_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, format=format)

Updates a table row format.

### Example
```python
from __future__ import print_function
import time
import aspose-words-cloud
from aspose-words-cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose-words-cloud.WordsApi()
name = 'name_example' # str | The document name.
table_path = 'table_path_example' # str | Path to table.
index = 56 # int | Object's index
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | File storage, which have to be used. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
format = aspose-words-cloud.TableRowFormat() # TableRowFormat | Table row format. (optional)

try:
    # Updates a table row format.
    api_response = api_instance.update_table_row_format(name, table_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_table_row_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **table_path** | **str**| Path to table. | 
 **index** | **int**| Object&#39;s index | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| File storage, which have to be used. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **format** | [**TableRowFormat**](TableRowFormat.md)| Table row format. | [optional] 

### Return type

[**TableRowFormatResponse**](TableRowFormatResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

