# asposewordscloud.WordsApi

All URIs are relative to *https://localhost/v4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_all_revisions**](WordsApi.md#accept_all_revisions) | **PUT** /words/{name}/revisions/acceptAll | Accepts all revisions in document.
[**append_document**](WordsApi.md#append_document) | **PUT** /words/{name}/appendDocument | Appends documents to original document.
[**apply_style_to_document_element**](WordsApi.md#apply_style_to_document_element) | **PUT** /words/{name}/{styledNodePath}/style | Apply a style to the document node.
[**build_report**](WordsApi.md#build_report) | **PUT** /words/{name}/buildReport | Executes document \&quot;build report\&quot; operation.
[**build_report_online**](WordsApi.md#build_report_online) | **PUT** /words/buildReport | Executes document \&quot;build report\&quot; online operation.
[**classify**](WordsApi.md#classify) | **PUT** /words/classify | Classifies raw text.
[**classify_document**](WordsApi.md#classify_document) | **GET** /words/{documentName}/classify | Classifies document.
[**compare_document**](WordsApi.md#compare_document) | **PUT** /words/{name}/compareDocument | Compares document with original document.
[**convert_document**](WordsApi.md#convert_document) | **PUT** /words/convert | Converts document from the request&#x27;s content to the specified format.
[**copy_file**](WordsApi.md#copy_file) | **PUT** /words/storage/file/copy/{srcPath} | Copy file
[**copy_folder**](WordsApi.md#copy_folder) | **PUT** /words/storage/folder/copy/{srcPath} | Copy folder
[**copy_style**](WordsApi.md#copy_style) | **POST** /words/{name}/styles/copy | Copy and insert a new style to the document, returns a copied style.
[**create_document**](WordsApi.md#create_document) | **PUT** /words/create | Creates new document. Document is created with format which is recognized from file extensions. Supported extensions: \&quot;.doc\&quot;, \&quot;.docx\&quot;, \&quot;.docm\&quot;, \&quot;.dot\&quot;, \&quot;.dotm\&quot;, \&quot;.dotx\&quot;, \&quot;.flatopc\&quot;, \&quot;.fopc\&quot;, \&quot;.flatopc_macro\&quot;, \&quot;.fopc_macro\&quot;, \&quot;.flatopc_template\&quot;, \&quot;.fopc_template\&quot;, \&quot;.flatopc_template_macro\&quot;, \&quot;.fopc_template_macro\&quot;, \&quot;.wordml\&quot;, \&quot;.wml\&quot;, \&quot;.rtf\&quot;.
[**create_folder**](WordsApi.md#create_folder) | **PUT** /words/storage/folder/{path} | Create the folder
[**create_or_update_document_property**](WordsApi.md#create_or_update_document_property) | **PUT** /words/{name}/documentProperties/{propertyName} | Adds new or update existing document property.
[**delete_all_paragraph_tab_stops**](WordsApi.md#delete_all_paragraph_tab_stops) | **DELETE** /words/{name}/{nodePath}/paragraphs/{index}/tabstops | Remove all tab stops.
[**delete_border**](WordsApi.md#delete_border) | **DELETE** /words/{name}/{nodePath}/borders/{borderType} | Resets border properties to default values.             
[**delete_borders**](WordsApi.md#delete_borders) | **DELETE** /words/{name}/{nodePath}/borders | Resets borders properties to default values.             
[**delete_comment**](WordsApi.md#delete_comment) | **DELETE** /words/{name}/comments/{commentIndex} | Removes comment from document.
[**delete_document_property**](WordsApi.md#delete_document_property) | **DELETE** /words/{name}/documentProperties/{propertyName} | Deletes document property.
[**delete_drawing_object**](WordsApi.md#delete_drawing_object) | **DELETE** /words/{name}/{nodePath}/drawingObjects/{index} | Removes drawing object from document.
[**delete_drawing_object_without_node_path**](WordsApi.md#delete_drawing_object_without_node_path) | **DELETE** /words/{name}/drawingObjects/{index} | Removes drawing object from document.
[**delete_field**](WordsApi.md#delete_field) | **DELETE** /words/{name}/{nodePath}/fields/{index} | Deletes field from document.
[**delete_field_without_node_path**](WordsApi.md#delete_field_without_node_path) | **DELETE** /words/{name}/fields/{index} | Deletes field from document.
[**delete_fields**](WordsApi.md#delete_fields) | **DELETE** /words/{name}/{nodePath}/fields | Removes fields from section paragraph.
[**delete_fields_without_node_path**](WordsApi.md#delete_fields_without_node_path) | **DELETE** /words/{name}/fields | Removes fields from section paragraph.
[**delete_file**](WordsApi.md#delete_file) | **DELETE** /words/storage/file/{path} | Delete file
[**delete_folder**](WordsApi.md#delete_folder) | **DELETE** /words/storage/folder/{path} | Delete folder
[**delete_footnote**](WordsApi.md#delete_footnote) | **DELETE** /words/{name}/{nodePath}/footnotes/{index} | Removes footnote from document.
[**delete_footnote_without_node_path**](WordsApi.md#delete_footnote_without_node_path) | **DELETE** /words/{name}/footnotes/{index} | Removes footnote from document.
[**delete_form_field**](WordsApi.md#delete_form_field) | **DELETE** /words/{name}/{nodePath}/formfields/{index} | Removes form field from document.
[**delete_form_field_without_node_path**](WordsApi.md#delete_form_field_without_node_path) | **DELETE** /words/{name}/formfields/{index} | Removes form field from document.
[**delete_header_footer**](WordsApi.md#delete_header_footer) | **DELETE** /words/{name}/{sectionPath}/headersfooters/{index} | Deletes header/footer from document.
[**delete_headers_footers**](WordsApi.md#delete_headers_footers) | **DELETE** /words/{name}/{sectionPath}/headersfooters | Deletes document headers and footers.
[**delete_macros**](WordsApi.md#delete_macros) | **DELETE** /words/{name}/macros | Removes macros from document.
[**delete_office_math_object**](WordsApi.md#delete_office_math_object) | **DELETE** /words/{name}/{nodePath}/OfficeMathObjects/{index} | Removes OfficeMath object from document.
[**delete_office_math_object_without_node_path**](WordsApi.md#delete_office_math_object_without_node_path) | **DELETE** /words/{name}/OfficeMathObjects/{index} | Removes OfficeMath object from document.
[**delete_paragraph**](WordsApi.md#delete_paragraph) | **DELETE** /words/{name}/{nodePath}/paragraphs/{index} | Removes paragraph from section.
[**delete_paragraph_list_format**](WordsApi.md#delete_paragraph_list_format) | **DELETE** /words/{name}/{nodePath}/paragraphs/{index}/listFormat | Delete paragraph list format, returns updated list format properties.
[**delete_paragraph_tab_stop**](WordsApi.md#delete_paragraph_tab_stop) | **DELETE** /words/{name}/{nodePath}/paragraphs/{index}/tabstop | Remove the i-th tab stop.
[**delete_paragraph_without_node_path**](WordsApi.md#delete_paragraph_without_node_path) | **DELETE** /words/{name}/paragraphs/{index} | Removes paragraph from section.
[**delete_run**](WordsApi.md#delete_run) | **DELETE** /words/{name}/{paragraphPath}/runs/{index} | Removes run from document.
[**delete_section**](WordsApi.md#delete_section) | **DELETE** /words/{name}/sections/{sectionIndex} | Removes section from document.
[**delete_table**](WordsApi.md#delete_table) | **DELETE** /words/{name}/{nodePath}/tables/{index} | Deletes a table.
[**delete_table_cell**](WordsApi.md#delete_table_cell) | **DELETE** /words/{name}/{tableRowPath}/cells/{index} | Deletes a table cell.
[**delete_table_row**](WordsApi.md#delete_table_row) | **DELETE** /words/{name}/{tablePath}/rows/{index} | Deletes a table row.
[**delete_table_without_node_path**](WordsApi.md#delete_table_without_node_path) | **DELETE** /words/{name}/tables/{index} | Deletes a table.
[**delete_watermark**](WordsApi.md#delete_watermark) | **POST** /words/{name}/watermarks/deleteLast | Deletes watermark (for deleting last watermark from the document).
[**download_file**](WordsApi.md#download_file) | **GET** /words/storage/file/{path} | Download file
[**execute_mail_merge**](WordsApi.md#execute_mail_merge) | **PUT** /words/{name}/MailMerge | Executes document mail merge operation.
[**execute_mail_merge_online**](WordsApi.md#execute_mail_merge_online) | **PUT** /words/MailMerge | Executes document mail merge online.
[**get_available_fonts**](WordsApi.md#get_available_fonts) | **GET** /words/fonts/available | Gets the list of fonts, available for document processing.
[**get_bookmark_by_name**](WordsApi.md#get_bookmark_by_name) | **GET** /words/{name}/bookmarks/{bookmarkName} | Reads document bookmark data by its name.
[**get_bookmarks**](WordsApi.md#get_bookmarks) | **GET** /words/{name}/bookmarks | Reads document bookmarks common info.
[**get_border**](WordsApi.md#get_border) | **GET** /words/{name}/{nodePath}/borders/{borderType} | Returns a border.
[**get_borders**](WordsApi.md#get_borders) | **GET** /words/{name}/{nodePath}/borders | Returns a collection of borders.
[**get_comment**](WordsApi.md#get_comment) | **GET** /words/{name}/comments/{commentIndex} | Gets comment from document.
[**get_comments**](WordsApi.md#get_comments) | **GET** /words/{name}/comments | Gets comments from document.
[**get_document**](WordsApi.md#get_document) | **GET** /words/{documentName} | Reads document common info.
[**get_document_drawing_object_by_index**](WordsApi.md#get_document_drawing_object_by_index) | **GET** /words/{name}/{nodePath}/drawingObjects/{index} | Reads document drawing object common info by its index or convert to format specified.
[**get_document_drawing_object_by_index_without_node_path**](WordsApi.md#get_document_drawing_object_by_index_without_node_path) | **GET** /words/{name}/drawingObjects/{index} | Reads document drawing object common info by its index or convert to format specified.
[**get_document_drawing_object_image_data**](WordsApi.md#get_document_drawing_object_image_data) | **GET** /words/{name}/{nodePath}/drawingObjects/{index}/imageData | Reads drawing object image data.
[**get_document_drawing_object_image_data_without_node_path**](WordsApi.md#get_document_drawing_object_image_data_without_node_path) | **GET** /words/{name}/drawingObjects/{index}/imageData | Reads drawing object image data.
[**get_document_drawing_object_ole_data**](WordsApi.md#get_document_drawing_object_ole_data) | **GET** /words/{name}/{nodePath}/drawingObjects/{index}/oleData | Gets drawing object OLE data.
[**get_document_drawing_object_ole_data_without_node_path**](WordsApi.md#get_document_drawing_object_ole_data_without_node_path) | **GET** /words/{name}/drawingObjects/{index}/oleData | Gets drawing object OLE data.
[**get_document_drawing_objects**](WordsApi.md#get_document_drawing_objects) | **GET** /words/{name}/{nodePath}/drawingObjects | Reads document drawing objects common info.
[**get_document_drawing_objects_without_node_path**](WordsApi.md#get_document_drawing_objects_without_node_path) | **GET** /words/{name}/drawingObjects | Reads document drawing objects common info.
[**get_document_field_names**](WordsApi.md#get_document_field_names) | **GET** /words/{name}/mailMerge/FieldNames | Reads document field names.
[**get_document_field_names_online**](WordsApi.md#get_document_field_names_online) | **PUT** /words/mailMerge/FieldNames | Reads document field names.
[**get_document_hyperlink_by_index**](WordsApi.md#get_document_hyperlink_by_index) | **GET** /words/{name}/hyperlinks/{hyperlinkIndex} | Reads document hyperlink by its index.
[**get_document_hyperlinks**](WordsApi.md#get_document_hyperlinks) | **GET** /words/{name}/hyperlinks | Reads document hyperlinks common info.
[**get_document_properties**](WordsApi.md#get_document_properties) | **GET** /words/{name}/documentProperties | Reads document properties info.
[**get_document_property**](WordsApi.md#get_document_property) | **GET** /words/{name}/documentProperties/{propertyName} | Reads document property info by the property name.
[**get_document_protection**](WordsApi.md#get_document_protection) | **GET** /words/{name}/protection | Reads document protection common info.
[**get_document_statistics**](WordsApi.md#get_document_statistics) | **GET** /words/{name}/statistics | Reads document statistics.
[**get_document_with_format**](WordsApi.md#get_document_with_format) | **GET** /words/{name} | Exports the document into the specified format.
[**get_field**](WordsApi.md#get_field) | **GET** /words/{name}/{nodePath}/fields/{index} | Gets field from document.
[**get_field_without_node_path**](WordsApi.md#get_field_without_node_path) | **GET** /words/{name}/fields/{index} | Gets field from document.
[**get_fields**](WordsApi.md#get_fields) | **GET** /words/{name}/{nodePath}/fields | Get fields from document.
[**get_fields_without_node_path**](WordsApi.md#get_fields_without_node_path) | **GET** /words/{name}/fields | Get fields from document.
[**get_files_list**](WordsApi.md#get_files_list) | **GET** /words/storage/folder/{path} | Get all files and folders within a folder
[**get_footnote**](WordsApi.md#get_footnote) | **GET** /words/{name}/{nodePath}/footnotes/{index} | Reads footnote by index.
[**get_footnote_without_node_path**](WordsApi.md#get_footnote_without_node_path) | **GET** /words/{name}/footnotes/{index} | Reads footnote by index.
[**get_footnotes**](WordsApi.md#get_footnotes) | **GET** /words/{name}/{nodePath}/footnotes | Gets footnotes from document.
[**get_footnotes_without_node_path**](WordsApi.md#get_footnotes_without_node_path) | **GET** /words/{name}/footnotes | Gets footnotes from document.
[**get_form_field**](WordsApi.md#get_form_field) | **GET** /words/{name}/{nodePath}/formfields/{index} | Returns representation of an one of the form field.
[**get_form_field_without_node_path**](WordsApi.md#get_form_field_without_node_path) | **GET** /words/{name}/formfields/{index} | Returns representation of an one of the form field.
[**get_form_fields**](WordsApi.md#get_form_fields) | **GET** /words/{name}/{nodePath}/formfields | Gets form fields from document.
[**get_form_fields_without_node_path**](WordsApi.md#get_form_fields_without_node_path) | **GET** /words/{name}/formfields | Gets form fields from document.
[**get_header_footer**](WordsApi.md#get_header_footer) | **GET** /words/{name}/headersfooters/{headerFooterIndex} | Returns a header/footer from the document by index.
[**get_header_footer_of_section**](WordsApi.md#get_header_footer_of_section) | **GET** /words/{name}/sections/{sectionIndex}/headersfooters/{headerFooterIndex} | Returns a header/footer from the document section.
[**get_header_footers**](WordsApi.md#get_header_footers) | **GET** /words/{name}/{sectionPath}/headersfooters | Returns a list of header/footers from the document.
[**get_list**](WordsApi.md#get_list) | **GET** /words/{name}/lists/{listId} | This resource represents one of the lists contained in the document.
[**get_lists**](WordsApi.md#get_lists) | **GET** /words/{name}/lists | Returns a list of lists that are contained in the document.
[**get_office_math_object**](WordsApi.md#get_office_math_object) | **GET** /words/{name}/{nodePath}/OfficeMathObjects/{index} | Reads OfficeMath object by index.
[**get_office_math_object_without_node_path**](WordsApi.md#get_office_math_object_without_node_path) | **GET** /words/{name}/OfficeMathObjects/{index} | Reads OfficeMath object by index.
[**get_office_math_objects**](WordsApi.md#get_office_math_objects) | **GET** /words/{name}/{nodePath}/OfficeMathObjects | Gets OfficeMath objects from document.
[**get_office_math_objects_without_node_path**](WordsApi.md#get_office_math_objects_without_node_path) | **GET** /words/{name}/OfficeMathObjects | Gets OfficeMath objects from document.
[**get_paragraph**](WordsApi.md#get_paragraph) | **GET** /words/{name}/{nodePath}/paragraphs/{index} | This resource represents one of the paragraphs contained in the document.
[**get_paragraph_format**](WordsApi.md#get_paragraph_format) | **GET** /words/{name}/{nodePath}/paragraphs/{index}/format | Represents all the formatting for a paragraph.
[**get_paragraph_format_without_node_path**](WordsApi.md#get_paragraph_format_without_node_path) | **GET** /words/{name}/paragraphs/{index}/format | Represents all the formatting for a paragraph.
[**get_paragraph_list_format**](WordsApi.md#get_paragraph_list_format) | **GET** /words/{name}/{nodePath}/paragraphs/{index}/listFormat | Represents list format for a paragraph.
[**get_paragraph_list_format_without_node_path**](WordsApi.md#get_paragraph_list_format_without_node_path) | **GET** /words/{name}/paragraphs/{index}/listFormat | Represents list format for a paragraph.
[**get_paragraph_tab_stops**](WordsApi.md#get_paragraph_tab_stops) | **GET** /words/{name}/{nodePath}/paragraphs/{index}/tabstops | Get all tab stops for the paragraph.
[**get_paragraph_without_node_path**](WordsApi.md#get_paragraph_without_node_path) | **GET** /words/{name}/paragraphs/{index} | This resource represents one of the paragraphs contained in the document.
[**get_paragraphs**](WordsApi.md#get_paragraphs) | **GET** /words/{name}/{nodePath}/paragraphs | Returns a list of paragraphs that are contained in the document.
[**get_paragraphs_without_node_path**](WordsApi.md#get_paragraphs_without_node_path) | **GET** /words/{name}/paragraphs | Returns a list of paragraphs that are contained in the document.
[**get_range_text**](WordsApi.md#get_range_text) | **GET** /words/{name}/range/{rangeStartIdentifier}/{rangeEndIdentifier} | Gets the text from the range.
[**get_run**](WordsApi.md#get_run) | **GET** /words/{name}/{paragraphPath}/runs/{index} | This resource represents run of text contained in the document.
[**get_run_font**](WordsApi.md#get_run_font) | **GET** /words/{name}/{paragraphPath}/runs/{index}/font | This resource represents font of run.
[**get_runs**](WordsApi.md#get_runs) | **GET** /words/{name}/{paragraphPath}/runs | This resource represents collection of runs in the paragraph.
[**get_section**](WordsApi.md#get_section) | **GET** /words/{name}/sections/{sectionIndex} | Gets document section by index.
[**get_section_page_setup**](WordsApi.md#get_section_page_setup) | **GET** /words/{name}/sections/{sectionIndex}/pageSetup | Gets page setup of section.
[**get_sections**](WordsApi.md#get_sections) | **GET** /words/{name}/sections | Returns a list of sections that are contained in the document.
[**get_style**](WordsApi.md#get_style) | **GET** /words/{name}/styles/{styleName} | This resource represents one of the styles contained in the document.
[**get_style_from_document_element**](WordsApi.md#get_style_from_document_element) | **GET** /words/{name}/{styledNodePath}/style | Gets a style from the document node.
[**get_styles**](WordsApi.md#get_styles) | **GET** /words/{name}/styles | Returns a list of styles contained in the document.
[**get_table**](WordsApi.md#get_table) | **GET** /words/{name}/{nodePath}/tables/{index} | Returns a table.
[**get_table_cell**](WordsApi.md#get_table_cell) | **GET** /words/{name}/{tableRowPath}/cells/{index} | Returns a table cell.
[**get_table_cell_format**](WordsApi.md#get_table_cell_format) | **GET** /words/{name}/{tableRowPath}/cells/{index}/cellformat | Returns a table cell format.
[**get_table_properties**](WordsApi.md#get_table_properties) | **GET** /words/{name}/{nodePath}/tables/{index}/properties | Returns a table properties.
[**get_table_properties_without_node_path**](WordsApi.md#get_table_properties_without_node_path) | **GET** /words/{name}/tables/{index}/properties | Returns a table properties.
[**get_table_row**](WordsApi.md#get_table_row) | **GET** /words/{name}/{tablePath}/rows/{index} | Returns a table row.
[**get_table_row_format**](WordsApi.md#get_table_row_format) | **GET** /words/{name}/{tablePath}/rows/{index}/rowformat | Returns a table row format.
[**get_table_without_node_path**](WordsApi.md#get_table_without_node_path) | **GET** /words/{name}/tables/{index} | Returns a table.
[**get_tables**](WordsApi.md#get_tables) | **GET** /words/{name}/{nodePath}/tables | Returns a list of tables that are contained in the document.
[**get_tables_without_node_path**](WordsApi.md#get_tables_without_node_path) | **GET** /words/{name}/tables | Returns a list of tables that are contained in the document.
[**insert_comment**](WordsApi.md#insert_comment) | **POST** /words/{name}/comments | Adds comment to document, returns inserted comment data.
[**insert_drawing_object**](WordsApi.md#insert_drawing_object) | **POST** /words/{name}/{nodePath}/drawingObjects | Adds drawing object to document, returns added  drawing object&#x27;s data.
[**insert_drawing_object_without_node_path**](WordsApi.md#insert_drawing_object_without_node_path) | **POST** /words/{name}/drawingObjects | Adds drawing object to document, returns added  drawing object&#x27;s data.
[**insert_field**](WordsApi.md#insert_field) | **POST** /words/{name}/{nodePath}/fields | Adds field to document, returns inserted field&#x27;s data.
[**insert_field_without_node_path**](WordsApi.md#insert_field_without_node_path) | **POST** /words/{name}/fields | Adds field to document, returns inserted field&#x27;s data.
[**insert_footnote**](WordsApi.md#insert_footnote) | **POST** /words/{name}/{nodePath}/footnotes | Adds footnote to document, returns added footnote&#x27;s data.
[**insert_footnote_without_node_path**](WordsApi.md#insert_footnote_without_node_path) | **POST** /words/{name}/footnotes | Adds footnote to document, returns added footnote&#x27;s data.
[**insert_form_field**](WordsApi.md#insert_form_field) | **POST** /words/{name}/{nodePath}/formfields | Adds form field to paragraph, returns added form field&#x27;s data.
[**insert_form_field_without_node_path**](WordsApi.md#insert_form_field_without_node_path) | **POST** /words/{name}/formfields | Adds form field to paragraph, returns added form field&#x27;s data.
[**insert_header_footer**](WordsApi.md#insert_header_footer) | **PUT** /words/{name}/{sectionPath}/headersfooters | Inserts to document header or footer.
[**insert_list**](WordsApi.md#insert_list) | **POST** /words/{name}/lists | Adds list to document, returns added list&#x27;s data.
[**insert_or_update_paragraph_tab_stop**](WordsApi.md#insert_or_update_paragraph_tab_stop) | **POST** /words/{name}/{nodePath}/paragraphs/{index}/tabstops | Insert or resplace tab stop if a tab stop with the position exists.
[**insert_page_numbers**](WordsApi.md#insert_page_numbers) | **PUT** /words/{name}/PageNumbers | Inserts document page numbers.
[**insert_paragraph**](WordsApi.md#insert_paragraph) | **POST** /words/{name}/{nodePath}/paragraphs | Adds paragraph to document, returns added paragraph&#x27;s data.
[**insert_run**](WordsApi.md#insert_run) | **POST** /words/{name}/{paragraphPath}/runs | Adds run to document, returns added paragraph&#x27;s data.
[**insert_style**](WordsApi.md#insert_style) | **POST** /words/{name}/styles/insert | Adds a style to the document, returns an added style.
[**insert_table**](WordsApi.md#insert_table) | **POST** /words/{name}/{nodePath}/tables | Adds table to document, returns added table&#x27;s data.             
[**insert_table_cell**](WordsApi.md#insert_table_cell) | **POST** /words/{name}/{tableRowPath}/cells | Adds table cell to table, returns added cell&#x27;s data.             
[**insert_table_row**](WordsApi.md#insert_table_row) | **POST** /words/{name}/{tablePath}/rows | Adds table row to table, returns added row&#x27;s data.             
[**insert_table_without_node_path**](WordsApi.md#insert_table_without_node_path) | **POST** /words/{name}/tables | Adds table to document, returns added table&#x27;s data.             
[**insert_watermark_image**](WordsApi.md#insert_watermark_image) | **POST** /words/{name}/watermarks/images | Inserts document watermark image.
[**insert_watermark_text**](WordsApi.md#insert_watermark_text) | **POST** /words/{name}/watermarks/texts | Inserts document watermark text.
[**load_web_document**](WordsApi.md#load_web_document) | **PUT** /words/loadWebDocument | Loads new document from web into the file with any supported format of data.
[**move_file**](WordsApi.md#move_file) | **PUT** /words/storage/file/move/{srcPath} | Move file
[**move_folder**](WordsApi.md#move_folder) | **PUT** /words/storage/folder/move/{srcPath} | Move folder
[**protect_document**](WordsApi.md#protect_document) | **PUT** /words/{name}/protection | Protects document.
[**reject_all_revisions**](WordsApi.md#reject_all_revisions) | **PUT** /words/{name}/revisions/rejectAll | Rejects all revisions in document.
[**remove_range**](WordsApi.md#remove_range) | **DELETE** /words/{name}/range/{rangeStartIdentifier}/{rangeEndIdentifier} | Removes the range from the document.
[**render_drawing_object**](WordsApi.md#render_drawing_object) | **GET** /words/{name}/{nodePath}/drawingObjects/{index}/render | Renders drawing object to specified format.
[**render_drawing_object_without_node_path**](WordsApi.md#render_drawing_object_without_node_path) | **GET** /words/{name}/drawingObjects/{index}/render | Renders drawing object to specified format.
[**render_math_object**](WordsApi.md#render_math_object) | **GET** /words/{name}/{nodePath}/OfficeMathObjects/{index}/render | Renders math object to specified format.
[**render_math_object_without_node_path**](WordsApi.md#render_math_object_without_node_path) | **GET** /words/{name}/OfficeMathObjects/{index}/render | Renders math object to specified format.
[**render_page**](WordsApi.md#render_page) | **GET** /words/{name}/pages/{pageIndex}/render | Renders page to specified format.
[**render_paragraph**](WordsApi.md#render_paragraph) | **GET** /words/{name}/{nodePath}/paragraphs/{index}/render | Renders paragraph to specified format.
[**render_paragraph_without_node_path**](WordsApi.md#render_paragraph_without_node_path) | **GET** /words/{name}/paragraphs/{index}/render | Renders paragraph to specified format.
[**render_table**](WordsApi.md#render_table) | **GET** /words/{name}/{nodePath}/tables/{index}/render | Renders table to specified format.
[**render_table_without_node_path**](WordsApi.md#render_table_without_node_path) | **GET** /words/{name}/tables/{index}/render | Renders table to specified format.
[**replace_text**](WordsApi.md#replace_text) | **PUT** /words/{name}/replaceText | Replaces document text.
[**replace_with_text**](WordsApi.md#replace_with_text) | **POST** /words/{name}/range/{rangeStartIdentifier}/{rangeEndIdentifier} | Replaces the content in the range.
[**reset_cache**](WordsApi.md#reset_cache) | **DELETE** /words/fonts/cache | Resets font&#x27;s cache.
[**save_as**](WordsApi.md#save_as) | **PUT** /words/{name}/saveAs | Converts document to destination format with detailed settings and saves result to storage.
[**save_as_range**](WordsApi.md#save_as_range) | **POST** /words/{name}/range/{rangeStartIdentifier}/{rangeEndIdentifier}/SaveAs | Saves the selected range as a new document.
[**save_as_tiff**](WordsApi.md#save_as_tiff) | **PUT** /words/{name}/saveAs/tiff | Converts document to tiff with detailed settings and saves result to storage.
[**search**](WordsApi.md#search) | **GET** /words/{name}/search | Searches text in document.
[**split_document**](WordsApi.md#split_document) | **PUT** /words/{name}/split | Splits document.
[**unprotect_document**](WordsApi.md#unprotect_document) | **DELETE** /words/{name}/protection | Unprotects document.
[**update_bookmark**](WordsApi.md#update_bookmark) | **PUT** /words/{name}/bookmarks/{bookmarkName} | Updates document bookmark.
[**update_border**](WordsApi.md#update_border) | **PUT** /words/{name}/{nodePath}/borders/{borderType} | Updates border properties.             
[**update_comment**](WordsApi.md#update_comment) | **PUT** /words/{name}/comments/{commentIndex} | Updates the comment, returns updated comment data.
[**update_drawing_object**](WordsApi.md#update_drawing_object) | **PUT** /words/{name}/{nodePath}/drawingObjects/{index} | Updates drawing object, returns updated  drawing object&#x27;s data.
[**update_drawing_object_without_node_path**](WordsApi.md#update_drawing_object_without_node_path) | **PUT** /words/{name}/drawingObjects/{index} | Updates drawing object, returns updated  drawing object&#x27;s data.
[**update_field**](WordsApi.md#update_field) | **PUT** /words/{name}/{nodePath}/fields/{index} | Updates field&#x27;s properties, returns updated field&#x27;s data.
[**update_fields**](WordsApi.md#update_fields) | **PUT** /words/{name}/updateFields | Updates (reevaluate) fields in document.
[**update_footnote**](WordsApi.md#update_footnote) | **PUT** /words/{name}/{nodePath}/footnotes/{index} | Updates footnote&#x27;s properties, returns updated run&#x27;s data.
[**update_footnote_without_node_path**](WordsApi.md#update_footnote_without_node_path) | **PUT** /words/{name}/footnotes/{index} | Updates footnote&#x27;s properties, returns updated run&#x27;s data.
[**update_form_field**](WordsApi.md#update_form_field) | **PUT** /words/{name}/{nodePath}/formfields/{index} | Updates properties of form field, returns updated form field.
[**update_form_field_without_node_path**](WordsApi.md#update_form_field_without_node_path) | **PUT** /words/{name}/formfields/{index} | Updates properties of form field, returns updated form field.
[**update_list**](WordsApi.md#update_list) | **PUT** /words/{name}/lists/{listId} | Updates list properties, returns updated list.
[**update_list_level**](WordsApi.md#update_list_level) | **PUT** /words/{name}/lists/{listId}/listLevels/{listLevel} | Updates list level in document list, returns updated list.
[**update_paragraph_format**](WordsApi.md#update_paragraph_format) | **PUT** /words/{name}/{nodePath}/paragraphs/{index}/format | Updates paragraph format properties, returns updated format properties.
[**update_paragraph_list_format**](WordsApi.md#update_paragraph_list_format) | **PUT** /words/{name}/{nodePath}/paragraphs/{index}/listFormat | Updates paragraph list format properties, returns updated list format properties.
[**update_run**](WordsApi.md#update_run) | **PUT** /words/{name}/{paragraphPath}/runs/{index} | Updates run&#x27;s properties, returns updated run&#x27;s data.
[**update_run_font**](WordsApi.md#update_run_font) | **PUT** /words/{name}/{paragraphPath}/runs/{index}/font | Updates font properties, returns updated font data.
[**update_section_page_setup**](WordsApi.md#update_section_page_setup) | **PUT** /words/{name}/sections/{sectionIndex}/pageSetup | Updates page setup of section.
[**update_style**](WordsApi.md#update_style) | **PUT** /words/{name}/styles/{styleName}/update | Updates style properties, returns an updated style.
[**update_table_cell_format**](WordsApi.md#update_table_cell_format) | **PUT** /words/{name}/{tableRowPath}/cells/{index}/cellformat | Updates a table cell format.
[**update_table_properties**](WordsApi.md#update_table_properties) | **PUT** /words/{name}/{nodePath}/tables/{index}/properties | Updates a table properties.
[**update_table_properties_without_node_path**](WordsApi.md#update_table_properties_without_node_path) | **PUT** /words/{name}/tables/{index}/properties | Updates a table properties.
[**update_table_row_format**](WordsApi.md#update_table_row_format) | **PUT** /words/{name}/{tablePath}/rows/{index}/rowformat | Updates a table row format.
[**upload_file**](WordsApi.md#upload_file) | **PUT** /words/storage/file/{path} | Upload file

# **accept_all_revisions**
> RevisionsModificationResponse accept_all_revisions(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)

Accepts all revisions in document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)

try:
    # Accepts all revisions in document.
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
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 

### Return type

[**RevisionsModificationResponse**](RevisionsModificationResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **append_document**
> DocumentResponse append_document(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Appends documents to original document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.DocumentEntryList() # DocumentEntryList | DocumentEntryList with a list of documents to append.
name = 'name_example' # str | Original document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Appends documents to original document.
    api_response = api_instance.append_document(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->append_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentEntryList**](DocumentEntryList.md)| DocumentEntryList with a list of documents to append. | 
 **name** | **str**| Original document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_style_to_document_element**
> WordsResponse apply_style_to_document_element(body, name, styled_node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Apply a style to the document node.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.StyleApply() # StyleApply | Style to apply.
name = 'name_example' # str | The document name.
styled_node_path = 'styled_node_path_example' # str | The path to the node that supports a style. Supported node types: ParagraphFormat, List, ListLevel, Table.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Apply a style to the document node.
    api_response = api_instance.apply_style_to_document_element(body, name, styled_node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->apply_style_to_document_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StyleApply**](StyleApply.md)| Style to apply. | 
 **name** | **str**| The document name. | 
 **styled_node_path** | **str**| The path to the node that supports a style. Supported node types: ParagraphFormat, List, ListLevel, Table. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**WordsResponse**](WordsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **build_report**
> DocumentResponse build_report(name, data=data, report_engine_settings=report_engine_settings, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)

Executes document \"build report\" operation.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The template name.
data = 'data_example' # str |  (optional)
report_engine_settings = asposewordscloud.ReportEngineSettings() # ReportEngineSettings |  (optional)
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved with autogenerated name. (optional)

try:
    # Executes document \"build report\" operation.
    api_response = api_instance.build_report(name, data=data, report_engine_settings=report_engine_settings, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->build_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The template name. | 
 **data** | **str**|  | [optional] 
 **report_engine_settings** | [**ReportEngineSettings**](.md)|  | [optional] 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved with autogenerated name. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **build_report_online**
> str build_report_online(template=template, data=data, report_engine_settings=report_engine_settings, document_file_name=document_file_name)

Executes document \"build report\" online operation.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
template = 'template_example' # str |  (optional)
data = 'data_example' # str |  (optional)
report_engine_settings = asposewordscloud.ReportEngineSettings() # ReportEngineSettings |  (optional)
document_file_name = 'document_file_name_example' # str | This file name will be used when resulting document has dynamic field for document file name {filename}. If it is not set, \"template\" will be used instead.  (optional)

try:
    # Executes document \"build report\" online operation.
    api_response = api_instance.build_report_online(template=template, data=data, report_engine_settings=report_engine_settings, document_file_name=document_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->build_report_online: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | **str**|  | [optional] 
 **data** | **str**|  | [optional] 
 **report_engine_settings** | [**ReportEngineSettings**](.md)|  | [optional] 
 **document_file_name** | **str**| This file name will be used when resulting document has dynamic field for document file name {filename}. If it is not set, \&quot;template\&quot; will be used instead.  | [optional] 

### Return type

**str**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **classify**
> ClassificationResponse classify(body, best_classes_count=best_classes_count)

Classifies raw text.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = 'body_example' # str | Text to classify.
best_classes_count = 'best_classes_count_example' # str | Number of the best classes to return. (optional)

try:
    # Classifies raw text.
    api_response = api_instance.classify(body, best_classes_count=best_classes_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->classify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Text to classify. | 
 **best_classes_count** | **str**| Number of the best classes to return. | [optional] 

### Return type

[**ClassificationResponse**](ClassificationResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **classify_document**
> ClassificationResponse classify_document(document_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, best_classes_count=best_classes_count, taxonomy=taxonomy)

Classifies document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
document_name = 'document_name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
best_classes_count = 'best_classes_count_example' # str | Count of the best classes to return. (optional)
taxonomy = 'taxonomy_example' # str | Taxonomy to use for classification return. (optional)

try:
    # Classifies document.
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
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **best_classes_count** | **str**| Count of the best classes to return. | [optional] 
 **taxonomy** | **str**| Taxonomy to use for classification return. | [optional] 

### Return type

[**ClassificationResponse**](ClassificationResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compare_document**
> DocumentResponse compare_document(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)

Compares document with original document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.CompareData() # CompareData | CompareData with a document to compare.
name = 'name_example' # str | Original document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)

try:
    # Compares document with original document.
    api_response = api_instance.compare_document(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->compare_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompareData**](CompareData.md)| CompareData with a document to compare. | 
 **name** | **str**| Original document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_document**
> str convert_document(format, document=document, storage=storage, out_path=out_path, file_name_field_value=file_name_field_value, fonts_location=fonts_location)

Converts document from the request's content to the specified format.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
format = 'format_example' # str | Format to convert.
document = 'document_example' # str |  (optional)
storage = 'storage_example' # str | Original document storage. (optional)
out_path = 'out_path_example' # str | Path for saving operation result to the local storage. (optional)
file_name_field_value = 'file_name_field_value_example' # str | This file name will be used when resulting document has dynamic field for document file name {filename}. If it is not set, \"sourceFilename\" will be used instead. (optional)
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Converts document from the request's content to the specified format.
    api_response = api_instance.convert_document(format, document=document, storage=storage, out_path=out_path, file_name_field_value=file_name_field_value, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->convert_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Format to convert. | 
 **document** | **str**|  | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **out_path** | **str**| Path for saving operation result to the local storage. | [optional] 
 **file_name_field_value** | **str**| This file name will be used when resulting document has dynamic field for document file name {filename}. If it is not set, \&quot;sourceFilename\&quot; will be used instead. | [optional] 
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

**str**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_file**
> copy_file(dest_path, src_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)

Copy file

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
dest_path = 'dest_path_example' # str | Destination file path
src_path = 'src_path_example' # str | Source file's path e.g. '/Folder 1/file.ext' or '/Bucket/Folder 1/file.ext'
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)
version_id = 'version_id_example' # str | File version ID to copy (optional)

try:
    # Copy file
    api_instance.copy_file(dest_path, src_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)
except ApiException as e:
    print("Exception when calling WordsApi->copy_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dest_path** | **str**| Destination file path | 
 **src_path** | **str**| Source file&#x27;s path e.g. &#x27;/Folder 1/file.ext&#x27; or &#x27;/Bucket/Folder 1/file.ext&#x27; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to copy | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_folder**
> copy_folder(dest_path, src_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)

Copy folder

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
dest_path = 'dest_path_example' # str | Destination folder path e.g. '/dst'
src_path = 'src_path_example' # str | Source folder path e.g. /Folder1
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)

try:
    # Copy folder
    api_instance.copy_folder(dest_path, src_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)
except ApiException as e:
    print("Exception when calling WordsApi->copy_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dest_path** | **str**| Destination folder path e.g. &#x27;/dst&#x27; | 
 **src_path** | **str**| Source folder path e.g. /Folder1 | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_style**
> StyleResponse copy_style(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Copy and insert a new style to the document, returns a copied style.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.StyleCopy() # StyleCopy | Style to copy.
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Copy and insert a new style to the document, returns a copied style.
    api_response = api_instance.copy_style(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->copy_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StyleCopy**](StyleCopy.md)| Style to copy. | 
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**StyleResponse**](StyleResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_document**
> DocumentResponse create_document(storage=storage, file_name=file_name, folder=folder)

Creates new document. Document is created with format which is recognized from file extensions. Supported extensions: \".doc\", \".docx\", \".docm\", \".dot\", \".dotm\", \".dotx\", \".flatopc\", \".fopc\", \".flatopc_macro\", \".fopc_macro\", \".flatopc_template\", \".fopc_template\", \".flatopc_template_macro\", \".fopc_template_macro\", \".wordml\", \".wml\", \".rtf\".

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
storage = 'storage_example' # str | Original document storage. (optional)
file_name = 'file_name_example' # str | The document name. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Creates new document. Document is created with format which is recognized from file extensions. Supported extensions: \".doc\", \".docx\", \".docm\", \".dot\", \".dotm\", \".dotx\", \".flatopc\", \".fopc\", \".flatopc_macro\", \".fopc_macro\", \".flatopc_template\", \".fopc_template\", \".flatopc_template_macro\", \".fopc_template_macro\", \".wordml\", \".wml\", \".rtf\".
    api_response = api_instance.create_document(storage=storage, file_name=file_name, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->create_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage** | **str**| Original document storage. | [optional] 
 **file_name** | **str**| The document name. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder**
> create_folder(path, storage_name=storage_name)

Create the folder

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
path = 'path_example' # str | Target folder's path e.g. Folder1/Folder2/. The folders will be created recursively
storage_name = 'storage_name_example' # str | Storage name (optional)

try:
    # Create the folder
    api_instance.create_folder(path, storage_name=storage_name)
except ApiException as e:
    print("Exception when calling WordsApi->create_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Target folder&#x27;s path e.g. Folder1/Folder2/. The folders will be created recursively | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_document_property**
> DocumentPropertyResponse create_or_update_document_property(body, name, property_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Adds new or update existing document property.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.DocumentPropertyCreateOrUpdate() # DocumentPropertyCreateOrUpdate | The property with new value.
name = 'name_example' # str | The document name.
property_name = 'property_name_example' # str | The property name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Adds new or update existing document property.
    api_response = api_instance.create_or_update_document_property(body, name, property_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->create_or_update_document_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentPropertyCreateOrUpdate**](DocumentPropertyCreateOrUpdate.md)| The property with new value. | 
 **name** | **str**| The document name. | 
 **property_name** | **str**| The property name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**DocumentPropertyResponse**](DocumentPropertyResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_paragraph_tab_stops**
> TabStopsResponse delete_all_paragraph_tab_stops(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)

Remove all tab stops.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node which contains paragraph.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)

try:
    # Remove all tab stops.
    api_response = api_instance.delete_all_paragraph_tab_stops(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_all_paragraph_tab_stops: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node which contains paragraph. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 

### Return type

[**TabStopsResponse**](TabStopsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_border**
> BorderResponse delete_border(name, node_path, border_type, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Resets border properties to default values.             

'nodePath' should refer to paragraph, cell or row.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node with border(node should be paragraph, cell or row).
border_type = 'border_type_example' # str | Border type.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Resets border properties to default values.             
    api_response = api_instance.delete_border(name, node_path, border_type, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_border: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node with border(node should be paragraph, cell or row). | 
 **border_type** | **str**| Border type. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**BorderResponse**](BorderResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_borders**
> BordersResponse delete_borders(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Resets borders properties to default values.             

'nodePath' should refer to paragraph, cell or row.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node with borders(node should be paragraph, cell or row).
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
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
 **node_path** | **str**| Path to the node with borders(node should be paragraph, cell or row). | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**BordersResponse**](BordersResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment**
> delete_comment(name, comment_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Removes comment from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
comment_index = 56 # int | The comment index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Removes comment from document.
    api_instance.delete_comment(name, comment_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **comment_index** | **int**| The comment index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_property**
> delete_document_property(name, property_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Deletes document property.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
property_name = 'property_name_example' # str | The property name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Deletes document property.
    api_instance.delete_document_property(name, property_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_document_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **property_name** | **str**| The property name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_drawing_object**
> delete_drawing_object(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Removes drawing object from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains collection of drawing objects.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Removes drawing object from document.
    api_instance.delete_drawing_object(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_drawing_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains collection of drawing objects. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_drawing_object_without_node_path**
> delete_drawing_object_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Removes drawing object from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Removes drawing object from document.
    api_instance.delete_drawing_object_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_drawing_object_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_field**
> delete_field(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Deletes field from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains collection of fields.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Deletes field from document.
    api_instance.delete_field(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains collection of fields. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_field_without_node_path**
> delete_field_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Deletes field from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Deletes field from document.
    api_instance.delete_field_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_field_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fields**
> delete_fields(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Removes fields from section paragraph.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains collection of fields.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Removes fields from section paragraph.
    api_instance.delete_fields(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains collection of fields. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fields_without_node_path**
> delete_fields_without_node_path(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Removes fields from section paragraph.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Removes fields from section paragraph.
    api_instance.delete_fields_without_node_path(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_fields_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> delete_file(path, storage_name=storage_name, version_id=version_id)

Delete file

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
path = 'path_example' # str | Path of the file including file name and extension e.g. /Folder1/file.ext
storage_name = 'storage_name_example' # str | Storage name (optional)
version_id = 'version_id_example' # str | File version ID to delete (optional)

try:
    # Delete file
    api_instance.delete_file(path, storage_name=storage_name, version_id=version_id)
except ApiException as e:
    print("Exception when calling WordsApi->delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path of the file including file name and extension e.g. /Folder1/file.ext | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to delete | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> delete_folder(path, storage_name=storage_name, recursive=recursive)

Delete folder

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
path = 'path_example' # str | Folder path e.g. /Folder1s
storage_name = 'storage_name_example' # str | Storage name (optional)
recursive = true # bool | Enable to delete folders, subfolders and files (optional)

try:
    # Delete folder
    api_instance.delete_folder(path, storage_name=storage_name, recursive=recursive)
except ApiException as e:
    print("Exception when calling WordsApi->delete_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path e.g. /Folder1s | 
 **storage_name** | **str**| Storage name | [optional] 
 **recursive** | **bool**| Enable to delete folders, subfolders and files | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_footnote**
> delete_footnote(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Removes footnote from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains collection of footnotes.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Removes footnote from document.
    api_instance.delete_footnote(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_footnote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains collection of footnotes. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_footnote_without_node_path**
> delete_footnote_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Removes footnote from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Removes footnote from document.
    api_instance.delete_footnote_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_footnote_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_form_field**
> delete_form_field(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Removes form field from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node that contains collection of formfields.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Removes form field from document.
    api_instance.delete_form_field(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_form_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node that contains collection of formfields. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_form_field_without_node_path**
> delete_form_field_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Removes form field from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Removes form field from document.
    api_instance.delete_form_field_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_form_field_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_header_footer**
> delete_header_footer(name, section_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Deletes header/footer from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
section_path = 'section_path_example' # str | Path to parent section.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Deletes header/footer from document.
    api_instance.delete_header_footer(name, section_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_header_footer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **section_path** | **str**| Path to parent section. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_headers_footers**
> delete_headers_footers(name, section_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, headers_footers_types=headers_footers_types)

Deletes document headers and footers.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
section_path = 'section_path_example' # str | Path to parent section.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
headers_footers_types = 'headers_footers_types_example' # str | List of types of headers and footers. (optional)

try:
    # Deletes document headers and footers.
    api_instance.delete_headers_footers(name, section_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, headers_footers_types=headers_footers_types)
except ApiException as e:
    print("Exception when calling WordsApi->delete_headers_footers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **section_path** | **str**| Path to parent section. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **headers_footers_types** | **str**| List of types of headers and footers. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_macros**
> delete_macros(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Removes macros from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Removes macros from document.
    api_instance.delete_macros(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_macros: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_office_math_object**
> delete_office_math_object(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Removes OfficeMath object from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains collection of OfficeMath objects.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Removes OfficeMath object from document.
    api_instance.delete_office_math_object(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_office_math_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains collection of OfficeMath objects. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_office_math_object_without_node_path**
> delete_office_math_object_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Removes OfficeMath object from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Removes OfficeMath object from document.
    api_instance.delete_office_math_object_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_office_math_object_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_paragraph**
> delete_paragraph(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Removes paragraph from section.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The file name.
node_path = 'node_path_example' # str | Path to the node which contains paragraphs.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Removes paragraph from section.
    api_instance.delete_paragraph(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_paragraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **node_path** | **str**| Path to the node which contains paragraphs. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_paragraph_list_format**
> ParagraphListFormatResponse delete_paragraph_list_format(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Delete paragraph list format, returns updated list format properties.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node which contains paragraphs.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Delete paragraph list format, returns updated list format properties.
    api_response = api_instance.delete_paragraph_list_format(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_paragraph_list_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node which contains paragraphs. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**ParagraphListFormatResponse**](ParagraphListFormatResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_paragraph_tab_stop**
> TabStopsResponse delete_paragraph_tab_stop(name, node_path, position, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)

Remove the i-th tab stop.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node which contains paragraph.
position = 1.2 # float | a tab stop position to remove.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)

try:
    # Remove the i-th tab stop.
    api_response = api_instance.delete_paragraph_tab_stop(name, node_path, position, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_paragraph_tab_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node which contains paragraph. | 
 **position** | **float**| a tab stop position to remove. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 

### Return type

[**TabStopsResponse**](TabStopsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_paragraph_without_node_path**
> delete_paragraph_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Removes paragraph from section.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The file name.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Removes paragraph from section.
    api_instance.delete_paragraph_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_paragraph_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_run**
> delete_run(name, paragraph_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Removes run from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
paragraph_path = 'paragraph_path_example' # str | Path to parent paragraph.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Removes run from document.
    api_instance.delete_run(name, paragraph_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **paragraph_path** | **str**| Path to parent paragraph. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_section**
> delete_section(name, section_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Removes section from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
section_index = 56 # int | Section index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Removes section from document.
    api_instance.delete_section(name, section_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **section_index** | **int**| Section index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_table**
> delete_table(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Deletes a table.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains tables.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Deletes a table.
    api_instance.delete_table(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains tables. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_table_cell**
> delete_table_cell(name, table_row_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Deletes a table cell.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
table_row_path = 'table_row_path_example' # str | Path to table row.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Deletes a table cell.
    api_instance.delete_table_cell(name, table_row_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_table_cell: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **table_row_path** | **str**| Path to table row. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_table_row**
> delete_table_row(name, table_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Deletes a table row.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
table_path = 'table_path_example' # str | Path to table.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Deletes a table row.
    api_instance.delete_table_row(name, table_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_table_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **table_path** | **str**| Path to table. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_table_without_node_path**
> delete_table_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Deletes a table.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Deletes a table.
    api_instance.delete_table_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
except ApiException as e:
    print("Exception when calling WordsApi->delete_table_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_watermark**
> DocumentResponse delete_watermark(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Deletes watermark (for deleting last watermark from the document).

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Deletes watermark (for deleting last watermark from the document).
    api_response = api_instance.delete_watermark(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->delete_watermark: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> str download_file(path, storage_name=storage_name, version_id=version_id)

Download file

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
path = 'path_example' # str | Path of the file including the file name and extension e.g. /folder1/file.ext
storage_name = 'storage_name_example' # str | Storage name (optional)
version_id = 'version_id_example' # str | File version ID to download (optional)

try:
    # Download file
    api_response = api_instance.download_file(path, storage_name=storage_name, version_id=version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path of the file including the file name and extension e.g. /folder1/file.ext | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to download | [optional] 

### Return type

**str**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_mail_merge**
> DocumentResponse execute_mail_merge(name, data=data, folder=folder, storage=storage, load_encoding=load_encoding, password=password, with_regions=with_regions, mail_merge_data_file=mail_merge_data_file, cleanup=cleanup, use_whole_paragraph_as_region=use_whole_paragraph_as_region, dest_file_name=dest_file_name)

Executes document mail merge operation.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The template name.
data = 'data_example' # str |  (optional)
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
with_regions = true # bool | With regions flag. (optional)
mail_merge_data_file = 'mail_merge_data_file_example' # str | Mail merge data. (optional)
cleanup = 'cleanup_example' # str | Clean up options. (optional)
use_whole_paragraph_as_region = true # bool | Gets or sets a value indicating whether paragraph with TableStart or.             TableEnd field should be fully included into mail merge region or particular range between TableStart and TableEnd fields.             The default value is true. (optional)
dest_file_name = 'dest_file_name_example' # str | Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved with autogenerated name. (optional)

try:
    # Executes document mail merge operation.
    api_response = api_instance.execute_mail_merge(name, data=data, folder=folder, storage=storage, load_encoding=load_encoding, password=password, with_regions=with_regions, mail_merge_data_file=mail_merge_data_file, cleanup=cleanup, use_whole_paragraph_as_region=use_whole_paragraph_as_region, dest_file_name=dest_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->execute_mail_merge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The template name. | 
 **data** | **str**|  | [optional] 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **with_regions** | **bool**| With regions flag. | [optional] 
 **mail_merge_data_file** | **str**| Mail merge data. | [optional] 
 **cleanup** | **str**| Clean up options. | [optional] 
 **use_whole_paragraph_as_region** | **bool**| Gets or sets a value indicating whether paragraph with TableStart or.             TableEnd field should be fully included into mail merge region or particular range between TableStart and TableEnd fields.             The default value is true. | [optional] 
 **dest_file_name** | **str**| Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved with autogenerated name. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_mail_merge_online**
> str execute_mail_merge_online(template=template, data=data, with_regions=with_regions, cleanup=cleanup, document_file_name=document_file_name)

Executes document mail merge online.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
template = 'template_example' # str |  (optional)
data = 'data_example' # str |  (optional)
with_regions = true # bool | With regions flag. (optional)
cleanup = 'cleanup_example' # str | Clean up options. (optional)
document_file_name = 'document_file_name_example' # str | This file name will be used when resulting document has dynamic field for document file name {filename}. If it is not set, \"template\" will be used instead. (optional)

try:
    # Executes document mail merge online.
    api_response = api_instance.execute_mail_merge_online(template=template, data=data, with_regions=with_regions, cleanup=cleanup, document_file_name=document_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->execute_mail_merge_online: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | **str**|  | [optional] 
 **data** | **str**|  | [optional] 
 **with_regions** | **bool**| With regions flag. | [optional] 
 **cleanup** | **str**| Clean up options. | [optional] 
 **document_file_name** | **str**| This file name will be used when resulting document has dynamic field for document file name {filename}. If it is not set, \&quot;template\&quot; will be used instead. | [optional] 

### Return type

**str**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_fonts**
> AvailableFontsResponse get_available_fonts(fonts_location=fonts_location)

Gets the list of fonts, available for document processing.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Gets the list of fonts, available for document processing.
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

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bookmark_by_name**
> BookmarkResponse get_bookmark_by_name(name, bookmark_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Reads document bookmark data by its name.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
bookmark_name = 'bookmark_name_example' # str | The bookmark name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Reads document bookmark data by its name.
    api_response = api_instance.get_bookmark_by_name(name, bookmark_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_bookmark_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **bookmark_name** | **str**| The bookmark name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**BookmarkResponse**](BookmarkResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bookmarks**
> BookmarksResponse get_bookmarks(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Reads document bookmarks common info.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Reads document bookmarks common info.
    api_response = api_instance.get_bookmarks(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_bookmarks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**BookmarksResponse**](BookmarksResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_border**
> BorderResponse get_border(name, node_path, border_type, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Returns a border.

'nodePath' should refer to paragraph, cell or row.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node with border(node should be paragraph, cell or row).
border_type = 'border_type_example' # str | Border type.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Returns a border.
    api_response = api_instance.get_border(name, node_path, border_type, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_border: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node with border(node should be paragraph, cell or row). | 
 **border_type** | **str**| Border type. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**BorderResponse**](BorderResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_borders**
> BordersResponse get_borders(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Returns a collection of borders.

'nodePath' should refer to paragraph, cell or row.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node with borders (node should be paragraph, cell or row).
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Returns a collection of borders.
    api_response = api_instance.get_borders(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_borders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node with borders (node should be paragraph, cell or row). | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**BordersResponse**](BordersResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment**
> CommentResponse get_comment(name, comment_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Gets comment from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
comment_index = 56 # int | The comment index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Gets comment from document.
    api_response = api_instance.get_comment(name, comment_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **comment_index** | **int**| The comment index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**CommentResponse**](CommentResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comments**
> CommentsResponse get_comments(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Gets comments from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Gets comments from document.
    api_response = api_instance.get_comments(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**CommentsResponse**](CommentsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> DocumentResponse get_document(document_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Reads document common info.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
document_name = 'document_name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Reads document common info.
    api_response = api_instance.get_document(document_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_drawing_object_by_index**
> DrawingObjectResponse get_document_drawing_object_by_index(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Reads document drawing object common info by its index or convert to format specified.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains collection of drawing objects.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Reads document drawing object common info by its index or convert to format specified.
    api_response = api_instance.get_document_drawing_object_by_index(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_drawing_object_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains collection of drawing objects. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**DrawingObjectResponse**](DrawingObjectResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_drawing_object_by_index_without_node_path**
> DrawingObjectResponse get_document_drawing_object_by_index_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Reads document drawing object common info by its index or convert to format specified.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Reads document drawing object common info by its index or convert to format specified.
    api_response = api_instance.get_document_drawing_object_by_index_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_drawing_object_by_index_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**DrawingObjectResponse**](DrawingObjectResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_drawing_object_image_data**
> str get_document_drawing_object_image_data(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Reads drawing object image data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains collection of drawing objects.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Reads drawing object image data.
    api_response = api_instance.get_document_drawing_object_image_data(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_drawing_object_image_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains collection of drawing objects. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

**str**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_drawing_object_image_data_without_node_path**
> str get_document_drawing_object_image_data_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Reads drawing object image data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Reads drawing object image data.
    api_response = api_instance.get_document_drawing_object_image_data_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_drawing_object_image_data_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

**str**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_drawing_object_ole_data**
> str get_document_drawing_object_ole_data(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Gets drawing object OLE data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains collection of drawing objects.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Gets drawing object OLE data.
    api_response = api_instance.get_document_drawing_object_ole_data(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_drawing_object_ole_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains collection of drawing objects. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

**str**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_drawing_object_ole_data_without_node_path**
> str get_document_drawing_object_ole_data_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Gets drawing object OLE data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Gets drawing object OLE data.
    api_response = api_instance.get_document_drawing_object_ole_data_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_drawing_object_ole_data_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

**str**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_drawing_objects**
> DrawingObjectsResponse get_document_drawing_objects(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Reads document drawing objects common info.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains collection of drawing objects.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Reads document drawing objects common info.
    api_response = api_instance.get_document_drawing_objects(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_drawing_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains collection of drawing objects. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**DrawingObjectsResponse**](DrawingObjectsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_drawing_objects_without_node_path**
> DrawingObjectsResponse get_document_drawing_objects_without_node_path(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Reads document drawing objects common info.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Reads document drawing objects common info.
    api_response = api_instance.get_document_drawing_objects_without_node_path(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_drawing_objects_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**DrawingObjectsResponse**](DrawingObjectsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_field_names**
> FieldNamesResponse get_document_field_names(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, use_non_merge_fields=use_non_merge_fields)

Reads document field names.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The template name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
use_non_merge_fields = true # bool | If true, result includes \"mustache\" field names. (optional)

try:
    # Reads document field names.
    api_response = api_instance.get_document_field_names(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, use_non_merge_fields=use_non_merge_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_field_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The template name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **use_non_merge_fields** | **bool**| If true, result includes \&quot;mustache\&quot; field names. | [optional] 

### Return type

[**FieldNamesResponse**](FieldNamesResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_field_names_online**
> FieldNamesResponse get_document_field_names_online(template=template, use_non_merge_fields=use_non_merge_fields)

Reads document field names.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
template = 'template_example' # str |  (optional)
use_non_merge_fields = true # bool | Use non merge fields or not. (optional)

try:
    # Reads document field names.
    api_response = api_instance.get_document_field_names_online(template=template, use_non_merge_fields=use_non_merge_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_field_names_online: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | **str**|  | [optional] 
 **use_non_merge_fields** | **bool**| Use non merge fields or not. | [optional] 

### Return type

[**FieldNamesResponse**](FieldNamesResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_hyperlink_by_index**
> HyperlinkResponse get_document_hyperlink_by_index(name, hyperlink_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Reads document hyperlink by its index.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
hyperlink_index = 56 # int | The hyperlink index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Reads document hyperlink by its index.
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
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**HyperlinkResponse**](HyperlinkResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_hyperlinks**
> HyperlinksResponse get_document_hyperlinks(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Reads document hyperlinks common info.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Reads document hyperlinks common info.
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
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**HyperlinksResponse**](HyperlinksResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_properties**
> DocumentPropertiesResponse get_document_properties(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Reads document properties info.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document's name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Reads document properties info.
    api_response = api_instance.get_document_properties(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document&#x27;s name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**DocumentPropertiesResponse**](DocumentPropertiesResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_property**
> DocumentPropertyResponse get_document_property(name, property_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Reads document property info by the property name.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
property_name = 'property_name_example' # str | The property name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Reads document property info by the property name.
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
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**DocumentPropertyResponse**](DocumentPropertyResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_protection**
> ProtectionDataResponse get_document_protection(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Reads document protection common info.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Reads document protection common info.
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
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**ProtectionDataResponse**](ProtectionDataResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_statistics**
> StatDataResponse get_document_statistics(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, include_comments=include_comments, include_footnotes=include_footnotes, include_text_in_shapes=include_text_in_shapes)

Reads document statistics.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
include_comments = true # bool | Support including/excluding comments from the WordCount. Default value is \"false\". (optional)
include_footnotes = true # bool | Support including/excluding footnotes from the WordCount. Default value is \"false\". (optional)
include_text_in_shapes = true # bool | Support including/excluding shape's text from the WordCount. Default value is \"false\". (optional)

try:
    # Reads document statistics.
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
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **include_comments** | **bool**| Support including/excluding comments from the WordCount. Default value is \&quot;false\&quot;. | [optional] 
 **include_footnotes** | **bool**| Support including/excluding footnotes from the WordCount. Default value is \&quot;false\&quot;. | [optional] 
 **include_text_in_shapes** | **bool**| Support including/excluding shape&#x27;s text from the WordCount. Default value is \&quot;false\&quot;. | [optional] 

### Return type

[**StatDataResponse**](StatDataResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_with_format**
> str get_document_with_format(name, format, folder=folder, storage=storage, load_encoding=load_encoding, password=password, out_path=out_path, fonts_location=fonts_location)

Exports the document into the specified format.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
format = 'format_example' # str | The destination format.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
out_path = 'out_path_example' # str | Path to save the result. (optional)
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Exports the document into the specified format.
    api_response = api_instance.get_document_with_format(name, format, folder=folder, storage=storage, load_encoding=load_encoding, password=password, out_path=out_path, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_document_with_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **format** | **str**| The destination format. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **out_path** | **str**| Path to save the result. | [optional] 
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

**str**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_field**
> FieldResponse get_field(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Gets field from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains collection of fields.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Gets field from document.
    api_response = api_instance.get_field(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains collection of fields. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**FieldResponse**](FieldResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_field_without_node_path**
> FieldResponse get_field_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Gets field from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Gets field from document.
    api_response = api_instance.get_field_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_field_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**FieldResponse**](FieldResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fields**
> FieldsResponse get_fields(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Get fields from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains collection of fields.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Get fields from document.
    api_response = api_instance.get_fields(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains collection of fields. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**FieldsResponse**](FieldsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fields_without_node_path**
> FieldsResponse get_fields_without_node_path(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Get fields from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Get fields from document.
    api_response = api_instance.get_fields_without_node_path(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_fields_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**FieldsResponse**](FieldsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files_list**
> FilesList get_files_list(path, storage_name=storage_name)

Get all files and folders within a folder

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
path = 'path_example' # str | Folder path e.g. /Folder1
storage_name = 'storage_name_example' # str | Storage name (optional)

try:
    # Get all files and folders within a folder
    api_response = api_instance.get_files_list(path, storage_name=storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_files_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path e.g. /Folder1 | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**FilesList**](FilesList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footnote**
> FootnoteResponse get_footnote(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Reads footnote by index.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains collection of footnotes.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Reads footnote by index.
    api_response = api_instance.get_footnote(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_footnote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains collection of footnotes. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**FootnoteResponse**](FootnoteResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footnote_without_node_path**
> FootnoteResponse get_footnote_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Reads footnote by index.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Reads footnote by index.
    api_response = api_instance.get_footnote_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_footnote_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**FootnoteResponse**](FootnoteResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footnotes**
> FootnotesResponse get_footnotes(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Gets footnotes from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains collection of footnotes.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Gets footnotes from document.
    api_response = api_instance.get_footnotes(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_footnotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains collection of footnotes. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**FootnotesResponse**](FootnotesResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footnotes_without_node_path**
> FootnotesResponse get_footnotes_without_node_path(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Gets footnotes from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Gets footnotes from document.
    api_response = api_instance.get_footnotes_without_node_path(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_footnotes_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**FootnotesResponse**](FootnotesResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_form_field**
> FormFieldResponse get_form_field(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Returns representation of an one of the form field.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node that contains collection of formfields.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Returns representation of an one of the form field.
    api_response = api_instance.get_form_field(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_form_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node that contains collection of formfields. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**FormFieldResponse**](FormFieldResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_form_field_without_node_path**
> FormFieldResponse get_form_field_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Returns representation of an one of the form field.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Returns representation of an one of the form field.
    api_response = api_instance.get_form_field_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_form_field_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**FormFieldResponse**](FormFieldResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_form_fields**
> FormFieldsResponse get_form_fields(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Gets form fields from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node containing collection of form fields.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Gets form fields from document.
    api_response = api_instance.get_form_fields(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_form_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node containing collection of form fields. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**FormFieldsResponse**](FormFieldsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_form_fields_without_node_path**
> FormFieldsResponse get_form_fields_without_node_path(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Gets form fields from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Gets form fields from document.
    api_response = api_instance.get_form_fields_without_node_path(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_form_fields_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**FormFieldsResponse**](FormFieldsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_header_footer**
> HeaderFooterResponse get_header_footer(name, header_footer_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, filter_by_type=filter_by_type)

Returns a header/footer from the document by index.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
header_footer_index = 56 # int | Header/footer index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
filter_by_type = 'filter_by_type_example' # str | List of types of headers and footers. (optional)

try:
    # Returns a header/footer from the document by index.
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
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **filter_by_type** | **str**| List of types of headers and footers. | [optional] 

### Return type

[**HeaderFooterResponse**](HeaderFooterResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_header_footer_of_section**
> HeaderFooterResponse get_header_footer_of_section(name, header_footer_index, section_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, filter_by_type=filter_by_type)

Returns a header/footer from the document section.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
header_footer_index = 56 # int | Header/footer index.
section_index = 56 # int | Section index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
filter_by_type = 'filter_by_type_example' # str | List of types of headers and footers. (optional)

try:
    # Returns a header/footer from the document section.
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
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **filter_by_type** | **str**| List of types of headers and footers. | [optional] 

### Return type

[**HeaderFooterResponse**](HeaderFooterResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_header_footers**
> HeaderFootersResponse get_header_footers(name, section_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, filter_by_type=filter_by_type)

Returns a list of header/footers from the document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
section_path = 'section_path_example' # str | Path to parent section.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
filter_by_type = 'filter_by_type_example' # str | List of types of headers and footers. (optional)

try:
    # Returns a list of header/footers from the document.
    api_response = api_instance.get_header_footers(name, section_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, filter_by_type=filter_by_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_header_footers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **section_path** | **str**| Path to parent section. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **filter_by_type** | **str**| List of types of headers and footers. | [optional] 

### Return type

[**HeaderFootersResponse**](HeaderFootersResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list**
> ListResponse get_list(name, list_id, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

This resource represents one of the lists contained in the document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
list_id = 56 # int | List unique identifier.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # This resource represents one of the lists contained in the document.
    api_response = api_instance.get_list(name, list_id, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **list_id** | **int**| List unique identifier. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**ListResponse**](ListResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lists**
> ListsResponse get_lists(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Returns a list of lists that are contained in the document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Returns a list of lists that are contained in the document.
    api_response = api_instance.get_lists(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_lists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**ListsResponse**](ListsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_office_math_object**
> OfficeMathObjectResponse get_office_math_object(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Reads OfficeMath object by index.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains collection of OfficeMath objects.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Reads OfficeMath object by index.
    api_response = api_instance.get_office_math_object(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_office_math_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains collection of OfficeMath objects. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**OfficeMathObjectResponse**](OfficeMathObjectResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_office_math_object_without_node_path**
> OfficeMathObjectResponse get_office_math_object_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Reads OfficeMath object by index.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Reads OfficeMath object by index.
    api_response = api_instance.get_office_math_object_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_office_math_object_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**OfficeMathObjectResponse**](OfficeMathObjectResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_office_math_objects**
> OfficeMathObjectsResponse get_office_math_objects(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Gets OfficeMath objects from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains collection of OfficeMath objects.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Gets OfficeMath objects from document.
    api_response = api_instance.get_office_math_objects(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_office_math_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains collection of OfficeMath objects. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**OfficeMathObjectsResponse**](OfficeMathObjectsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_office_math_objects_without_node_path**
> OfficeMathObjectsResponse get_office_math_objects_without_node_path(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Gets OfficeMath objects from document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Gets OfficeMath objects from document.
    api_response = api_instance.get_office_math_objects_without_node_path(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_office_math_objects_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**OfficeMathObjectsResponse**](OfficeMathObjectsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_paragraph**
> ParagraphResponse get_paragraph(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

This resource represents one of the paragraphs contained in the document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node which contains paragraphs.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # This resource represents one of the paragraphs contained in the document.
    api_response = api_instance.get_paragraph(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_paragraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node which contains paragraphs. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**ParagraphResponse**](ParagraphResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_paragraph_format**
> ParagraphFormatResponse get_paragraph_format(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Represents all the formatting for a paragraph.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node which contains paragraphs.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Represents all the formatting for a paragraph.
    api_response = api_instance.get_paragraph_format(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_paragraph_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node which contains paragraphs. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**ParagraphFormatResponse**](ParagraphFormatResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_paragraph_format_without_node_path**
> ParagraphFormatResponse get_paragraph_format_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Represents all the formatting for a paragraph.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Represents all the formatting for a paragraph.
    api_response = api_instance.get_paragraph_format_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_paragraph_format_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**ParagraphFormatResponse**](ParagraphFormatResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_paragraph_list_format**
> ParagraphListFormatResponse get_paragraph_list_format(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Represents list format for a paragraph.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node which contains paragraphs.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Represents list format for a paragraph.
    api_response = api_instance.get_paragraph_list_format(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_paragraph_list_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node which contains paragraphs. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**ParagraphListFormatResponse**](ParagraphListFormatResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_paragraph_list_format_without_node_path**
> ParagraphListFormatResponse get_paragraph_list_format_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Represents list format for a paragraph.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Represents list format for a paragraph.
    api_response = api_instance.get_paragraph_list_format_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_paragraph_list_format_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**ParagraphListFormatResponse**](ParagraphListFormatResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_paragraph_tab_stops**
> TabStopsResponse get_paragraph_tab_stops(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Get all tab stops for the paragraph.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node which contains paragraph.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Get all tab stops for the paragraph.
    api_response = api_instance.get_paragraph_tab_stops(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_paragraph_tab_stops: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node which contains paragraph. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**TabStopsResponse**](TabStopsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_paragraph_without_node_path**
> ParagraphResponse get_paragraph_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

This resource represents one of the paragraphs contained in the document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # This resource represents one of the paragraphs contained in the document.
    api_response = api_instance.get_paragraph_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_paragraph_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**ParagraphResponse**](ParagraphResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_paragraphs**
> ParagraphLinkCollectionResponse get_paragraphs(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Returns a list of paragraphs that are contained in the document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node which contains paragraphs.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Returns a list of paragraphs that are contained in the document.
    api_response = api_instance.get_paragraphs(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_paragraphs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node which contains paragraphs. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**ParagraphLinkCollectionResponse**](ParagraphLinkCollectionResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_paragraphs_without_node_path**
> ParagraphLinkCollectionResponse get_paragraphs_without_node_path(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Returns a list of paragraphs that are contained in the document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Returns a list of paragraphs that are contained in the document.
    api_response = api_instance.get_paragraphs_without_node_path(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_paragraphs_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**ParagraphLinkCollectionResponse**](ParagraphLinkCollectionResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_range_text**
> RangeTextResponse get_range_text(name, range_start_identifier, range_end_identifier, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Gets the text from the range.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document.
range_start_identifier = 'range_start_identifier_example' # str | The range start identifier. Identifier is the value of the \"nodeId\" field, which every document node has, extended with the prefix \"id\". It looks like \"id0.0.7\". Also values like \"image5\" and \"table3\" can be used as an identifier for images and tables, where the number is an index of the image/table.
range_end_identifier = 'range_end_identifier_example' # str | The range end identifier.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Gets the text from the range.
    api_response = api_instance.get_range_text(name, range_start_identifier, range_end_identifier, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_range_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document. | 
 **range_start_identifier** | **str**| The range start identifier. Identifier is the value of the \&quot;nodeId\&quot; field, which every document node has, extended with the prefix \&quot;id\&quot;. It looks like \&quot;id0.0.7\&quot;. Also values like \&quot;image5\&quot; and \&quot;table3\&quot; can be used as an identifier for images and tables, where the number is an index of the image/table. | 
 **range_end_identifier** | **str**| The range end identifier. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**RangeTextResponse**](RangeTextResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run**
> RunResponse get_run(name, paragraph_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

This resource represents run of text contained in the document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
paragraph_path = 'paragraph_path_example' # str | Path to parent paragraph.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # This resource represents run of text contained in the document.
    api_response = api_instance.get_run(name, paragraph_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **paragraph_path** | **str**| Path to parent paragraph. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**RunResponse**](RunResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_font**
> FontResponse get_run_font(name, paragraph_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

This resource represents font of run.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
paragraph_path = 'paragraph_path_example' # str | Path to parent paragraph.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # This resource represents font of run.
    api_response = api_instance.get_run_font(name, paragraph_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_run_font: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **paragraph_path** | **str**| Path to parent paragraph. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**FontResponse**](FontResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runs**
> RunsResponse get_runs(name, paragraph_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

This resource represents collection of runs in the paragraph.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
paragraph_path = 'paragraph_path_example' # str | Path to parent paragraph.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # This resource represents collection of runs in the paragraph.
    api_response = api_instance.get_runs(name, paragraph_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **paragraph_path** | **str**| Path to parent paragraph. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**RunsResponse**](RunsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section**
> SectionResponse get_section(name, section_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Gets document section by index.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
section_index = 56 # int | Section index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Gets document section by index.
    api_response = api_instance.get_section(name, section_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **section_index** | **int**| Section index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**SectionResponse**](SectionResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section_page_setup**
> SectionPageSetupResponse get_section_page_setup(name, section_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Gets page setup of section.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
section_index = 56 # int | Section index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Gets page setup of section.
    api_response = api_instance.get_section_page_setup(name, section_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_section_page_setup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **section_index** | **int**| Section index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**SectionPageSetupResponse**](SectionPageSetupResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sections**
> SectionLinkCollectionResponse get_sections(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Returns a list of sections that are contained in the document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Returns a list of sections that are contained in the document.
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
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**SectionLinkCollectionResponse**](SectionLinkCollectionResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_style**
> StyleResponse get_style(name, style_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

This resource represents one of the styles contained in the document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
style_name = 'style_name_example' # str | Style name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # This resource represents one of the styles contained in the document.
    api_response = api_instance.get_style(name, style_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **style_name** | **str**| Style name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**StyleResponse**](StyleResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_style_from_document_element**
> StyleResponse get_style_from_document_element(name, styled_node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Gets a style from the document node.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
styled_node_path = 'styled_node_path_example' # str | The path to the node that supports a style. Supported node types: ParagraphFormat, List, ListLevel, Table.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Gets a style from the document node.
    api_response = api_instance.get_style_from_document_element(name, styled_node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_style_from_document_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **styled_node_path** | **str**| The path to the node that supports a style. Supported node types: ParagraphFormat, List, ListLevel, Table. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**StyleResponse**](StyleResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_styles**
> StylesResponse get_styles(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Returns a list of styles contained in the document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Returns a list of styles contained in the document.
    api_response = api_instance.get_styles(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_styles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**StylesResponse**](StylesResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table**
> TableResponse get_table(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Returns a table.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains tables.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Returns a table.
    api_response = api_instance.get_table(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains tables. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**TableResponse**](TableResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table_cell**
> TableCellResponse get_table_cell(name, table_row_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Returns a table cell.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
table_row_path = 'table_row_path_example' # str | Path to table row.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Returns a table cell.
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
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**TableCellResponse**](TableCellResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table_cell_format**
> TableCellFormatResponse get_table_cell_format(name, table_row_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Returns a table cell format.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
table_row_path = 'table_row_path_example' # str | Path to table row.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Returns a table cell format.
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
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**TableCellFormatResponse**](TableCellFormatResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table_properties**
> TablePropertiesResponse get_table_properties(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Returns a table properties.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains tables.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Returns a table properties.
    api_response = api_instance.get_table_properties(name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_table_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains tables. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**TablePropertiesResponse**](TablePropertiesResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table_properties_without_node_path**
> TablePropertiesResponse get_table_properties_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Returns a table properties.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Returns a table properties.
    api_response = api_instance.get_table_properties_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_table_properties_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**TablePropertiesResponse**](TablePropertiesResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table_row**
> TableRowResponse get_table_row(name, table_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Returns a table row.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
table_path = 'table_path_example' # str | Path to table.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Returns a table row.
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
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**TableRowResponse**](TableRowResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table_row_format**
> TableRowFormatResponse get_table_row_format(name, table_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Returns a table row format.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
table_path = 'table_path_example' # str | Path to table.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Returns a table row format.
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
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**TableRowFormatResponse**](TableRowFormatResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table_without_node_path**
> TableResponse get_table_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Returns a table.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Returns a table.
    api_response = api_instance.get_table_without_node_path(name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_table_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**TableResponse**](TableResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tables**
> TableLinkCollectionResponse get_tables(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Returns a list of tables that are contained in the document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains tables.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Returns a list of tables that are contained in the document.
    api_response = api_instance.get_tables(name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_tables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains tables. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**TableLinkCollectionResponse**](TableLinkCollectionResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tables_without_node_path**
> TableLinkCollectionResponse get_tables_without_node_path(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Returns a list of tables that are contained in the document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Returns a list of tables that are contained in the document.
    api_response = api_instance.get_tables_without_node_path(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->get_tables_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**TableLinkCollectionResponse**](TableLinkCollectionResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_comment**
> CommentResponse insert_comment(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Adds comment to document, returns inserted comment data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.CommentInsert() # CommentInsert | The comment data.
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Adds comment to document, returns inserted comment data.
    api_response = api_instance.insert_comment(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommentInsert**](CommentInsert.md)| The comment data. | 
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**CommentResponse**](CommentResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_drawing_object**
> DrawingObjectResponse insert_drawing_object(name, node_path, drawing_object=drawing_object, image_file=image_file, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Adds drawing object to document, returns added  drawing object's data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains collection of drawing objects.
drawing_object = asposewordscloud.DrawingObjectInsert() # DrawingObjectInsert |  (optional)
image_file = 'image_file_example' # str |  (optional)
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Adds drawing object to document, returns added  drawing object's data.
    api_response = api_instance.insert_drawing_object(name, node_path, drawing_object=drawing_object, image_file=image_file, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_drawing_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains collection of drawing objects. | 
 **drawing_object** | [**DrawingObjectInsert**](.md)|  | [optional] 
 **image_file** | **str**|  | [optional] 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**DrawingObjectResponse**](DrawingObjectResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_drawing_object_without_node_path**
> DrawingObjectResponse insert_drawing_object_without_node_path(name, drawing_object=drawing_object, image_file=image_file, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Adds drawing object to document, returns added  drawing object's data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
drawing_object = asposewordscloud.DrawingObjectInsert() # DrawingObjectInsert |  (optional)
image_file = 'image_file_example' # str |  (optional)
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Adds drawing object to document, returns added  drawing object's data.
    api_response = api_instance.insert_drawing_object_without_node_path(name, drawing_object=drawing_object, image_file=image_file, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_drawing_object_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **drawing_object** | [**DrawingObjectInsert**](.md)|  | [optional] 
 **image_file** | **str**|  | [optional] 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**DrawingObjectResponse**](DrawingObjectResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_field**
> FieldResponse insert_field(body, name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, insert_before_node=insert_before_node)

Adds field to document, returns inserted field's data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.FieldInsert() # FieldInsert | Field data.
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains collection of fields.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
insert_before_node = 'insert_before_node_example' # str | Field will be inserted before node with id=\"nodeId\". (optional)

try:
    # Adds field to document, returns inserted field's data.
    api_response = api_instance.insert_field(body, name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, insert_before_node=insert_before_node)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FieldInsert**](FieldInsert.md)| Field data. | 
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains collection of fields. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **insert_before_node** | **str**| Field will be inserted before node with id&#x3D;\&quot;nodeId\&quot;. | [optional] 

### Return type

[**FieldResponse**](FieldResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_field_without_node_path**
> FieldResponse insert_field_without_node_path(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, insert_before_node=insert_before_node)

Adds field to document, returns inserted field's data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.FieldInsert() # FieldInsert | Field data.
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
insert_before_node = 'insert_before_node_example' # str | Field will be inserted before node with id=\"nodeId\". (optional)

try:
    # Adds field to document, returns inserted field's data.
    api_response = api_instance.insert_field_without_node_path(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, insert_before_node=insert_before_node)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_field_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FieldInsert**](FieldInsert.md)| Field data. | 
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **insert_before_node** | **str**| Field will be inserted before node with id&#x3D;\&quot;nodeId\&quot;. | [optional] 

### Return type

[**FieldResponse**](FieldResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_footnote**
> FootnoteResponse insert_footnote(body, name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Adds footnote to document, returns added footnote's data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.FootnoteInsert() # FootnoteInsert | Footnote data.
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains collection of footnotes.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Adds footnote to document, returns added footnote's data.
    api_response = api_instance.insert_footnote(body, name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_footnote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FootnoteInsert**](FootnoteInsert.md)| Footnote data. | 
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains collection of footnotes. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**FootnoteResponse**](FootnoteResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_footnote_without_node_path**
> FootnoteResponse insert_footnote_without_node_path(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Adds footnote to document, returns added footnote's data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.FootnoteInsert() # FootnoteInsert | Footnote data.
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Adds footnote to document, returns added footnote's data.
    api_response = api_instance.insert_footnote_without_node_path(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_footnote_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FootnoteInsert**](FootnoteInsert.md)| Footnote data. | 
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**FootnoteResponse**](FootnoteResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_form_field**
> FormFieldResponse insert_form_field(body, name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, insert_before_node=insert_before_node)

Adds form field to paragraph, returns added form field's data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.FormField() # FormField | From field data.
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node that contains collection of formfields.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
insert_before_node = 'insert_before_node_example' # str | Form field will be inserted before node with index. (optional)

try:
    # Adds form field to paragraph, returns added form field's data.
    api_response = api_instance.insert_form_field(body, name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, insert_before_node=insert_before_node)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_form_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FormField**](FormField.md)| From field data. | 
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node that contains collection of formfields. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **insert_before_node** | **str**| Form field will be inserted before node with index. | [optional] 

### Return type

[**FormFieldResponse**](FormFieldResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_form_field_without_node_path**
> FormFieldResponse insert_form_field_without_node_path(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, insert_before_node=insert_before_node)

Adds form field to paragraph, returns added form field's data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.FormField() # FormField | From field data.
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
insert_before_node = 'insert_before_node_example' # str | Form field will be inserted before node with index. (optional)

try:
    # Adds form field to paragraph, returns added form field's data.
    api_response = api_instance.insert_form_field_without_node_path(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, insert_before_node=insert_before_node)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_form_field_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FormField**](FormField.md)| From field data. | 
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **insert_before_node** | **str**| Form field will be inserted before node with index. | [optional] 

### Return type

[**FormFieldResponse**](FormFieldResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_header_footer**
> HeaderFooterResponse insert_header_footer(body, name, section_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Inserts to document header or footer.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = 'body_example' # str | Type of header/footer.
name = 'name_example' # str | The document name.
section_path = 'section_path_example' # str | Path to parent section.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Inserts to document header or footer.
    api_response = api_instance.insert_header_footer(body, name, section_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_header_footer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Type of header/footer. | 
 **name** | **str**| The document name. | 
 **section_path** | **str**| Path to parent section. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**HeaderFooterResponse**](HeaderFooterResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_list**
> ListResponse insert_list(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Adds list to document, returns added list's data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.ListInsert() # ListInsert | List to insert.
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Adds list to document, returns added list's data.
    api_response = api_instance.insert_list(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListInsert**](ListInsert.md)| List to insert. | 
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**ListResponse**](ListResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_or_update_paragraph_tab_stop**
> TabStopsResponse insert_or_update_paragraph_tab_stop(body, name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)

Insert or resplace tab stop if a tab stop with the position exists.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.TabStopInsert() # TabStopInsert | Paragraph tab stop.
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node which contains paragraph.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)

try:
    # Insert or resplace tab stop if a tab stop with the position exists.
    api_response = api_instance.insert_or_update_paragraph_tab_stop(body, name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_or_update_paragraph_tab_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TabStopInsert**](TabStopInsert.md)| Paragraph tab stop. | 
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node which contains paragraph. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 

### Return type

[**TabStopsResponse**](TabStopsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_page_numbers**
> DocumentResponse insert_page_numbers(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Inserts document page numbers.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.PageNumber() # PageNumber | PageNumber with the page numbers settings.
name = 'name_example' # str | A document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Inserts document page numbers.
    api_response = api_instance.insert_page_numbers(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_page_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PageNumber**](PageNumber.md)| PageNumber with the page numbers settings. | 
 **name** | **str**| A document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_paragraph**
> ParagraphResponse insert_paragraph(body, name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, insert_before_node=insert_before_node)

Adds paragraph to document, returns added paragraph's data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.ParagraphInsert() # ParagraphInsert | Paragraph data.
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node which contains paragraphs.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
insert_before_node = 'insert_before_node_example' # str | Paragraph will be inserted before node with index. (optional)

try:
    # Adds paragraph to document, returns added paragraph's data.
    api_response = api_instance.insert_paragraph(body, name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, insert_before_node=insert_before_node)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_paragraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ParagraphInsert**](ParagraphInsert.md)| Paragraph data. | 
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node which contains paragraphs. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **insert_before_node** | **str**| Paragraph will be inserted before node with index. | [optional] 

### Return type

[**ParagraphResponse**](ParagraphResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_run**
> RunResponse insert_run(body, name, paragraph_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, insert_before_node=insert_before_node)

Adds run to document, returns added paragraph's data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.RunInsert() # RunInsert | Run data.
name = 'name_example' # str | The document name.
paragraph_path = 'paragraph_path_example' # str | Path to parent paragraph.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
insert_before_node = 'insert_before_node_example' # str | Paragraph will be inserted before node with index. (optional)

try:
    # Adds run to document, returns added paragraph's data.
    api_response = api_instance.insert_run(body, name, paragraph_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, insert_before_node=insert_before_node)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RunInsert**](RunInsert.md)| Run data. | 
 **name** | **str**| The document name. | 
 **paragraph_path** | **str**| Path to parent paragraph. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **insert_before_node** | **str**| Paragraph will be inserted before node with index. | [optional] 

### Return type

[**RunResponse**](RunResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_style**
> StyleResponse insert_style(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Adds a style to the document, returns an added style.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.StyleInsert() # StyleInsert | Style to insert.
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Adds a style to the document, returns an added style.
    api_response = api_instance.insert_style(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StyleInsert**](StyleInsert.md)| Style to insert. | 
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**StyleResponse**](StyleResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_table**
> TableResponse insert_table(body, name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Adds table to document, returns added table's data.             

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.TableInsert() # TableInsert | Table parameters/.
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains tables.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Adds table to document, returns added table's data.             
    api_response = api_instance.insert_table(body, name, node_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableInsert**](TableInsert.md)| Table parameters/. | 
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains tables. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**TableResponse**](TableResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_table_cell**
> TableCellResponse insert_table_cell(body, name, table_row_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Adds table cell to table, returns added cell's data.             

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.TableCellInsert() # TableCellInsert | Table cell parameters/.
name = 'name_example' # str | The document name.
table_row_path = 'table_row_path_example' # str | Path to table row.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Adds table cell to table, returns added cell's data.             
    api_response = api_instance.insert_table_cell(body, name, table_row_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_table_cell: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableCellInsert**](TableCellInsert.md)| Table cell parameters/. | 
 **name** | **str**| The document name. | 
 **table_row_path** | **str**| Path to table row. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**TableCellResponse**](TableCellResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_table_row**
> TableRowResponse insert_table_row(body, name, table_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Adds table row to table, returns added row's data.             

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.TableRowInsert() # TableRowInsert | Table row parameters/.
name = 'name_example' # str | The document name.
table_path = 'table_path_example' # str | Path to table.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Adds table row to table, returns added row's data.             
    api_response = api_instance.insert_table_row(body, name, table_path, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_table_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableRowInsert**](TableRowInsert.md)| Table row parameters/. | 
 **name** | **str**| The document name. | 
 **table_path** | **str**| Path to table. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**TableRowResponse**](TableRowResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_table_without_node_path**
> TableResponse insert_table_without_node_path(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Adds table to document, returns added table's data.             

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.TableInsert() # TableInsert | Table parameters/.
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Adds table to document, returns added table's data.             
    api_response = api_instance.insert_table_without_node_path(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_table_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableInsert**](TableInsert.md)| Table parameters/. | 
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**TableResponse**](TableResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_watermark_image**
> DocumentResponse insert_watermark_image(name, image_file=image_file, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, rotation_angle=rotation_angle, image=image)

Inserts document watermark image.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
image_file = 'image_file_example' # str |  (optional)
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)
rotation_angle = 1.2 # float | The watermark rotation angle. (optional)
image = 'image_example' # str | The image file server full name. If the name is empty the image is expected in request content. (optional)

try:
    # Inserts document watermark image.
    api_response = api_instance.insert_watermark_image(name, image_file=image_file, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time, rotation_angle=rotation_angle, image=image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_watermark_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_file** | **str**|  | [optional] 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 
 **rotation_angle** | **float**| The watermark rotation angle. | [optional] 
 **image** | **str**| The image file server full name. If the name is empty the image is expected in request content. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_watermark_text**
> DocumentResponse insert_watermark_text(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Inserts document watermark text.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.WatermarkText() # WatermarkText | WatermarkText with the watermark data.
            
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Inserts document watermark text.
    api_response = api_instance.insert_watermark_text(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->insert_watermark_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WatermarkText**](WatermarkText.md)| WatermarkText with the watermark data.
             | 
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_web_document**
> SaveResponse load_web_document(body, storage=storage)

Loads new document from web into the file with any supported format of data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.LoadWebDocumentData() # LoadWebDocumentData | Parameters of loading.
storage = 'storage_example' # str | Original document storage. (optional)

try:
    # Loads new document from web into the file with any supported format of data.
    api_response = api_instance.load_web_document(body, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->load_web_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoadWebDocumentData**](LoadWebDocumentData.md)| Parameters of loading. | 
 **storage** | **str**| Original document storage. | [optional] 

### Return type

[**SaveResponse**](SaveResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_file**
> move_file(dest_path, src_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)

Move file

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
dest_path = 'dest_path_example' # str | Destination file path e.g. '/dest.ext'
src_path = 'src_path_example' # str | Source file's path e.g. '/Folder 1/file.ext' or '/Bucket/Folder 1/file.ext'
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)
version_id = 'version_id_example' # str | File version ID to move (optional)

try:
    # Move file
    api_instance.move_file(dest_path, src_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)
except ApiException as e:
    print("Exception when calling WordsApi->move_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dest_path** | **str**| Destination file path e.g. &#x27;/dest.ext&#x27; | 
 **src_path** | **str**| Source file&#x27;s path e.g. &#x27;/Folder 1/file.ext&#x27; or &#x27;/Bucket/Folder 1/file.ext&#x27; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to move | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_folder**
> move_folder(dest_path, src_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)

Move folder

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
dest_path = 'dest_path_example' # str | Destination folder path to move to e.g '/dst'
src_path = 'src_path_example' # str | Source folder path e.g. /Folder1
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)

try:
    # Move folder
    api_instance.move_folder(dest_path, src_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)
except ApiException as e:
    print("Exception when calling WordsApi->move_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dest_path** | **str**| Destination folder path to move to e.g &#x27;/dst&#x27; | 
 **src_path** | **str**| Source folder path e.g. /Folder1 | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_document**
> ProtectionDataResponse protect_document(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)

Protects document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.ProtectionRequest() # ProtectionRequest | ProtectionRequest with protection settings.
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)

try:
    # Protects document.
    api_response = api_instance.protect_document(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->protect_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtectionRequest**](ProtectionRequest.md)| ProtectionRequest with protection settings. | 
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 

### Return type

[**ProtectionDataResponse**](ProtectionDataResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_all_revisions**
> RevisionsModificationResponse reject_all_revisions(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)

Rejects all revisions in document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)

try:
    # Rejects all revisions in document.
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
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 

### Return type

[**RevisionsModificationResponse**](RevisionsModificationResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_range**
> DocumentResponse remove_range(name, range_start_identifier, range_end_identifier, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)

Removes the range from the document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document.
range_start_identifier = 'range_start_identifier_example' # str | The range start identifier. Identifier is the value of the \"nodeId\" field, which every document node has, extended with the prefix \"id\". It looks like \"id0.0.7\". Also values like \"image5\" and \"table3\" can be used as an identifier for images and tables, where the number is an index of the image/table.
range_end_identifier = 'range_end_identifier_example' # str | The range end identifier.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)

try:
    # Removes the range from the document.
    api_response = api_instance.remove_range(name, range_start_identifier, range_end_identifier, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->remove_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document. | 
 **range_start_identifier** | **str**| The range start identifier. Identifier is the value of the \&quot;nodeId\&quot; field, which every document node has, extended with the prefix \&quot;id\&quot;. It looks like \&quot;id0.0.7\&quot;. Also values like \&quot;image5\&quot; and \&quot;table3\&quot; can be used as an identifier for images and tables, where the number is an index of the image/table. | 
 **range_end_identifier** | **str**| The range end identifier. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_drawing_object**
> str render_drawing_object(name, format, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, fonts_location=fonts_location)

Renders drawing object to specified format.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
format = 'format_example' # str | The destination format.
node_path = 'node_path_example' # str | Path to the node, which contains drawing objects.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Renders drawing object to specified format.
    api_response = api_instance.render_drawing_object(name, format, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->render_drawing_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **format** | **str**| The destination format. | 
 **node_path** | **str**| Path to the node, which contains drawing objects. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

**str**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_drawing_object_without_node_path**
> str render_drawing_object_without_node_path(name, format, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, fonts_location=fonts_location)

Renders drawing object to specified format.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
format = 'format_example' # str | The destination format.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Renders drawing object to specified format.
    api_response = api_instance.render_drawing_object_without_node_path(name, format, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->render_drawing_object_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **format** | **str**| The destination format. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

**str**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_math_object**
> str render_math_object(name, format, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, fonts_location=fonts_location)

Renders math object to specified format.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
format = 'format_example' # str | The destination format.
node_path = 'node_path_example' # str | Path to the node, which contains office math objects.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Renders math object to specified format.
    api_response = api_instance.render_math_object(name, format, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->render_math_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **format** | **str**| The destination format. | 
 **node_path** | **str**| Path to the node, which contains office math objects. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

**str**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_math_object_without_node_path**
> str render_math_object_without_node_path(name, format, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, fonts_location=fonts_location)

Renders math object to specified format.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
format = 'format_example' # str | The destination format.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Renders math object to specified format.
    api_response = api_instance.render_math_object_without_node_path(name, format, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->render_math_object_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **format** | **str**| The destination format. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

**str**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_page**
> str render_page(name, page_index, format, folder=folder, storage=storage, load_encoding=load_encoding, password=password, fonts_location=fonts_location)

Renders page to specified format.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
page_index = 56 # int | Comment index.
format = 'format_example' # str | The destination format.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
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
 **name** | **str**| The document name. | 
 **page_index** | **int**| Comment index. | 
 **format** | **str**| The destination format. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

**str**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_paragraph**
> str render_paragraph(name, format, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, fonts_location=fonts_location)

Renders paragraph to specified format.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
format = 'format_example' # str | The destination format.
node_path = 'node_path_example' # str | Path to the node, which contains paragraphs.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Renders paragraph to specified format.
    api_response = api_instance.render_paragraph(name, format, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->render_paragraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **format** | **str**| The destination format. | 
 **node_path** | **str**| Path to the node, which contains paragraphs. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

**str**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_paragraph_without_node_path**
> str render_paragraph_without_node_path(name, format, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, fonts_location=fonts_location)

Renders paragraph to specified format.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
format = 'format_example' # str | The destination format.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Renders paragraph to specified format.
    api_response = api_instance.render_paragraph_without_node_path(name, format, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->render_paragraph_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **format** | **str**| The destination format. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

**str**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_table**
> str render_table(name, format, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, fonts_location=fonts_location)

Renders table to specified format.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
format = 'format_example' # str | The destination format.
node_path = 'node_path_example' # str | Path to the node, which contains tables.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Renders table to specified format.
    api_response = api_instance.render_table(name, format, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->render_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **format** | **str**| The destination format. | 
 **node_path** | **str**| Path to the node, which contains tables. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

**str**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_table_without_node_path**
> str render_table_without_node_path(name, format, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, fonts_location=fonts_location)

Renders table to specified format.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
format = 'format_example' # str | The destination format.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Renders table to specified format.
    api_response = api_instance.render_table_without_node_path(name, format, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->render_table_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **format** | **str**| The destination format. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

**str**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_text**
> ReplaceTextResponse replace_text(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Replaces document text.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.ReplaceTextParameters() # ReplaceTextParameters | ReplaceTextResponse with the replace operation settings.
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Replaces document text.
    api_response = api_instance.replace_text(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->replace_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReplaceTextParameters**](ReplaceTextParameters.md)| ReplaceTextResponse with the replace operation settings. | 
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**ReplaceTextResponse**](ReplaceTextResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_with_text**
> DocumentResponse replace_with_text(body, name, range_start_identifier, range_end_identifier, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)

Replaces the content in the range.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.ReplaceRange() # ReplaceRange | Model with text for replacement.
name = 'name_example' # str | The document.
range_start_identifier = 'range_start_identifier_example' # str | The range start identifier. Identifier is the value of the \"nodeId\" field, which every document node has, extended with the prefix \"id\". It looks like \"id0.0.7\". Also values like \"image5\" and \"table3\" can be used as an identifier for images and tables, where the number is an index of the image/table.
range_end_identifier = 'range_end_identifier_example' # str | The range end identifier.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)

try:
    # Replaces the content in the range.
    api_response = api_instance.replace_with_text(body, name, range_start_identifier, range_end_identifier, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->replace_with_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReplaceRange**](ReplaceRange.md)| Model with text for replacement. | 
 **name** | **str**| The document. | 
 **range_start_identifier** | **str**| The range start identifier. Identifier is the value of the \&quot;nodeId\&quot; field, which every document node has, extended with the prefix \&quot;id\&quot;. It looks like \&quot;id0.0.7\&quot;. Also values like \&quot;image5\&quot; and \&quot;table3\&quot; can be used as an identifier for images and tables, where the number is an index of the image/table. | 
 **range_end_identifier** | **str**| The range end identifier. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_cache**
> reset_cache()

Resets font's cache.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))

try:
    # Resets font's cache.
    api_instance.reset_cache()
except ApiException as e:
    print("Exception when calling WordsApi->reset_cache: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_as**
> SaveResponse save_as(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, fonts_location=fonts_location)

Converts document to destination format with detailed settings and saves result to storage.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.SaveOptionsData() # SaveOptionsData | Save options.
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Converts document to destination format with detailed settings and saves result to storage.
    api_response = api_instance.save_as(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->save_as: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SaveOptionsData**](SaveOptionsData.md)| Save options. | 
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

[**SaveResponse**](SaveResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_as_range**
> DocumentResponse save_as_range(body, name, range_start_identifier, range_end_identifier, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Saves the selected range as a new document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.RangeDocument() # RangeDocument | Parameters of a new document.
name = 'name_example' # str | The document.
range_start_identifier = 'range_start_identifier_example' # str | The range start identifier. Identifier is the value of the \"nodeId\" field, which every document node has, extended with the prefix \"id\". It looks like \"id0.0.7\". Also values like \"image5\" and \"table3\" can be used as an identifier for images and tables, where the number is an index of the image/table.
range_end_identifier = 'range_end_identifier_example' # str | The range end identifier.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Saves the selected range as a new document.
    api_response = api_instance.save_as_range(body, name, range_start_identifier, range_end_identifier, folder=folder, storage=storage, load_encoding=load_encoding, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->save_as_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RangeDocument**](RangeDocument.md)| Parameters of a new document. | 
 **name** | **str**| The document. | 
 **range_start_identifier** | **str**| The range start identifier. Identifier is the value of the \&quot;nodeId\&quot; field, which every document node has, extended with the prefix \&quot;id\&quot;. It looks like \&quot;id0.0.7\&quot;. Also values like \&quot;image5\&quot; and \&quot;table3\&quot; can be used as an identifier for images and tables, where the number is an index of the image/table. | 
 **range_end_identifier** | **str**| The range end identifier. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_as_tiff**
> SaveResponse save_as_tiff(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, use_anti_aliasing=use_anti_aliasing, use_high_quality_rendering=use_high_quality_rendering, image_brightness=image_brightness, image_color_mode=image_color_mode, image_contrast=image_contrast, numeral_format=numeral_format, page_count=page_count, page_index=page_index, paper_color=paper_color, pixel_format=pixel_format, resolution=resolution, scale=scale, tiff_compression=tiff_compression, dml_rendering_mode=dml_rendering_mode, dml_effects_rendering_mode=dml_effects_rendering_mode, tiff_binarization_method=tiff_binarization_method, zip_output=zip_output, fonts_location=fonts_location)

Converts document to tiff with detailed settings and saves result to storage.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.TiffSaveOptionsData() # TiffSaveOptionsData | Tiff save options.
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
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
    # Converts document to tiff with detailed settings and saves result to storage.
    api_response = api_instance.save_as_tiff(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, use_anti_aliasing=use_anti_aliasing, use_high_quality_rendering=use_high_quality_rendering, image_brightness=image_brightness, image_color_mode=image_color_mode, image_contrast=image_contrast, numeral_format=numeral_format, page_count=page_count, page_index=page_index, paper_color=paper_color, pixel_format=pixel_format, resolution=resolution, scale=scale, tiff_compression=tiff_compression, dml_rendering_mode=dml_rendering_mode, dml_effects_rendering_mode=dml_effects_rendering_mode, tiff_binarization_method=tiff_binarization_method, zip_output=zip_output, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->save_as_tiff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TiffSaveOptionsData**](TiffSaveOptionsData.md)| Tiff save options. | 
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
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

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> SearchResponse search(name, pattern, folder=folder, storage=storage, load_encoding=load_encoding, password=password)

Searches text in document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
pattern = 'pattern_example' # str | The regular expression used to find matches.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)

try:
    # Searches text in document.
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
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **split_document**
> SplitDocumentResponse split_document(name, format, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, _from=_from, to=to, zip_output=zip_output, fonts_location=fonts_location)

Splits document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | Original document name.
format = 'format_example' # str | Format to split.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
_from = 56 # int | Start page. (optional)
to = 56 # int | End page. (optional)
zip_output = true # bool | ZipOutput or not. (optional)
fonts_location = 'fonts_location_example' # str | Folder in filestorage with custom fonts. (optional)

try:
    # Splits document.
    api_response = api_instance.split_document(name, format, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, _from=_from, to=to, zip_output=zip_output, fonts_location=fonts_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->split_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Original document name. | 
 **format** | **str**| Format to split. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **_from** | **int**| Start page. | [optional] 
 **to** | **int**| End page. | [optional] 
 **zip_output** | **bool**| ZipOutput or not. | [optional] 
 **fonts_location** | **str**| Folder in filestorage with custom fonts. | [optional] 

### Return type

[**SplitDocumentResponse**](SplitDocumentResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unprotect_document**
> ProtectionDataResponse unprotect_document(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)

Unprotects document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.ProtectionRequest() # ProtectionRequest | ProtectionRequest with protection settings.
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)

try:
    # Unprotects document.
    api_response = api_instance.unprotect_document(body, name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->unprotect_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtectionRequest**](ProtectionRequest.md)| ProtectionRequest with protection settings. | 
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 

### Return type

[**ProtectionDataResponse**](ProtectionDataResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bookmark**
> BookmarkResponse update_bookmark(body, name, bookmark_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates document bookmark.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.BookmarkData() # BookmarkData | BookmarkData with new bookmark data.
name = 'name_example' # str | The document name.
bookmark_name = 'bookmark_name_example' # str | The bookmark name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates document bookmark.
    api_response = api_instance.update_bookmark(body, name, bookmark_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_bookmark: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BookmarkData**](BookmarkData.md)| BookmarkData with new bookmark data. | 
 **name** | **str**| The document name. | 
 **bookmark_name** | **str**| The bookmark name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**BookmarkResponse**](BookmarkResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_border**
> BorderResponse update_border(body, name, node_path, border_type, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates border properties.             

'nodePath' should refer to paragraph, cell or row.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.Border() # Border | Border properties.
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node with border(node should be paragraph, cell or row).
border_type = 'border_type_example' # str | Border type.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates border properties.             
    api_response = api_instance.update_border(body, name, node_path, border_type, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_border: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Border**](Border.md)| Border properties. | 
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node with border(node should be paragraph, cell or row). | 
 **border_type** | **str**| Border type. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**BorderResponse**](BorderResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comment**
> CommentResponse update_comment(body, name, comment_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates the comment, returns updated comment data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.CommentUpdate() # CommentUpdate | The comment data.
name = 'name_example' # str | The document name.
comment_index = 56 # int | The comment index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates the comment, returns updated comment data.
    api_response = api_instance.update_comment(body, name, comment_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommentUpdate**](CommentUpdate.md)| The comment data. | 
 **name** | **str**| The document name. | 
 **comment_index** | **int**| The comment index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**CommentResponse**](CommentResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_drawing_object**
> DrawingObjectResponse update_drawing_object(name, node_path, index, drawing_object=drawing_object, image_file=image_file, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates drawing object, returns updated  drawing object's data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains collection of drawing objects.
index = 56 # int | Object index.
drawing_object = asposewordscloud.DrawingObjectUpdate() # DrawingObjectUpdate |  (optional)
image_file = 'image_file_example' # str |  (optional)
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates drawing object, returns updated  drawing object's data.
    api_response = api_instance.update_drawing_object(name, node_path, index, drawing_object=drawing_object, image_file=image_file, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_drawing_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains collection of drawing objects. | 
 **index** | **int**| Object index. | 
 **drawing_object** | [**DrawingObjectUpdate**](.md)|  | [optional] 
 **image_file** | **str**|  | [optional] 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**DrawingObjectResponse**](DrawingObjectResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_drawing_object_without_node_path**
> DrawingObjectResponse update_drawing_object_without_node_path(name, index, drawing_object=drawing_object, image_file=image_file, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates drawing object, returns updated  drawing object's data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
index = 56 # int | Object index.
drawing_object = asposewordscloud.DrawingObjectUpdate() # DrawingObjectUpdate |  (optional)
image_file = 'image_file_example' # str |  (optional)
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates drawing object, returns updated  drawing object's data.
    api_response = api_instance.update_drawing_object_without_node_path(name, index, drawing_object=drawing_object, image_file=image_file, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_drawing_object_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **index** | **int**| Object index. | 
 **drawing_object** | [**DrawingObjectUpdate**](.md)|  | [optional] 
 **image_file** | **str**|  | [optional] 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**DrawingObjectResponse**](DrawingObjectResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_field**
> FieldResponse update_field(body, name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates field's properties, returns updated field's data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.FieldUpdate() # FieldUpdate | Field data.
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains collection of fields.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates field's properties, returns updated field's data.
    api_response = api_instance.update_field(body, name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FieldUpdate**](FieldUpdate.md)| Field data. | 
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains collection of fields. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**FieldResponse**](FieldResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fields**
> DocumentResponse update_fields(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)

Updates (reevaluate) fields in document.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)

try:
    # Updates (reevaluate) fields in document.
    api_response = api_instance.update_fields(name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_footnote**
> FootnoteResponse update_footnote(body, name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates footnote's properties, returns updated run's data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.FootnoteUpdate() # FootnoteUpdate | Footnote data.
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains collection of footnotes.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates footnote's properties, returns updated run's data.
    api_response = api_instance.update_footnote(body, name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_footnote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FootnoteUpdate**](FootnoteUpdate.md)| Footnote data. | 
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains collection of footnotes. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**FootnoteResponse**](FootnoteResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_footnote_without_node_path**
> FootnoteResponse update_footnote_without_node_path(body, name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates footnote's properties, returns updated run's data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.FootnoteUpdate() # FootnoteUpdate | Footnote data.
name = 'name_example' # str | The document name.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates footnote's properties, returns updated run's data.
    api_response = api_instance.update_footnote_without_node_path(body, name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_footnote_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FootnoteUpdate**](FootnoteUpdate.md)| Footnote data. | 
 **name** | **str**| The document name. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**FootnoteResponse**](FootnoteResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_form_field**
> FormFieldResponse update_form_field(body, name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates properties of form field, returns updated form field.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.FormField() # FormField | From field data.
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node that contains collection of formfields.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates properties of form field, returns updated form field.
    api_response = api_instance.update_form_field(body, name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_form_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FormField**](FormField.md)| From field data. | 
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node that contains collection of formfields. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**FormFieldResponse**](FormFieldResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_form_field_without_node_path**
> FormFieldResponse update_form_field_without_node_path(body, name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates properties of form field, returns updated form field.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.FormField() # FormField | From field data.
name = 'name_example' # str | The document name.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates properties of form field, returns updated form field.
    api_response = api_instance.update_form_field_without_node_path(body, name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_form_field_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FormField**](FormField.md)| From field data. | 
 **name** | **str**| The document name. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**FormFieldResponse**](FormFieldResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_list**
> ListResponse update_list(body, name, list_id, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates list properties, returns updated list.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.ListUpdate() # ListUpdate | List object.
name = 'name_example' # str | The document name.
list_id = 56 # int | List unique identifier.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates list properties, returns updated list.
    api_response = api_instance.update_list(body, name, list_id, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListUpdate**](ListUpdate.md)| List object. | 
 **name** | **str**| The document name. | 
 **list_id** | **int**| List unique identifier. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**ListResponse**](ListResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_list_level**
> ListResponse update_list_level(body, name, list_id, list_level, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates list level in document list, returns updated list.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.ListLevelUpdate() # ListLevelUpdate | List object.
name = 'name_example' # str | The document name.
list_id = 56 # int | List unique identifier.
list_level = 56 # int | List level identifier.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates list level in document list, returns updated list.
    api_response = api_instance.update_list_level(body, name, list_id, list_level, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_list_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListLevelUpdate**](ListLevelUpdate.md)| List object. | 
 **name** | **str**| The document name. | 
 **list_id** | **int**| List unique identifier. | 
 **list_level** | **int**| List level identifier. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**ListResponse**](ListResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_paragraph_format**
> ParagraphFormatResponse update_paragraph_format(body, name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates paragraph format properties, returns updated format properties.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.ParagraphFormat() # ParagraphFormat | Paragraph format object.
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node which contains paragraphs.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates paragraph format properties, returns updated format properties.
    api_response = api_instance.update_paragraph_format(body, name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_paragraph_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ParagraphFormat**](ParagraphFormat.md)| Paragraph format object. | 
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node which contains paragraphs. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**ParagraphFormatResponse**](ParagraphFormatResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_paragraph_list_format**
> ParagraphListFormatResponse update_paragraph_list_format(body, name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates paragraph list format properties, returns updated list format properties.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.ListFormatUpdate() # ListFormatUpdate | Paragraph format object.
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node which contains paragraphs.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates paragraph list format properties, returns updated list format properties.
    api_response = api_instance.update_paragraph_list_format(body, name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_paragraph_list_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListFormatUpdate**](ListFormatUpdate.md)| Paragraph format object. | 
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node which contains paragraphs. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**ParagraphListFormatResponse**](ParagraphListFormatResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_run**
> RunResponse update_run(body, name, paragraph_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates run's properties, returns updated run's data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.RunUpdate() # RunUpdate | Run data.
name = 'name_example' # str | The document name.
paragraph_path = 'paragraph_path_example' # str | Path to parent paragraph.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates run's properties, returns updated run's data.
    api_response = api_instance.update_run(body, name, paragraph_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RunUpdate**](RunUpdate.md)| Run data. | 
 **name** | **str**| The document name. | 
 **paragraph_path** | **str**| Path to parent paragraph. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**RunResponse**](RunResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_run_font**
> FontResponse update_run_font(body, name, paragraph_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates font properties, returns updated font data.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.Font() # Font | Font dto object.
name = 'name_example' # str | The document name.
paragraph_path = 'paragraph_path_example' # str | Path to parent paragraph.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates font properties, returns updated font data.
    api_response = api_instance.update_run_font(body, name, paragraph_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_run_font: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Font**](Font.md)| Font dto object. | 
 **name** | **str**| The document name. | 
 **paragraph_path** | **str**| Path to parent paragraph. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**FontResponse**](FontResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_section_page_setup**
> SectionPageSetupResponse update_section_page_setup(body, name, section_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates page setup of section.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.PageSetup() # PageSetup | Page setup properties dto.
name = 'name_example' # str | The document name.
section_index = 56 # int | Section index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates page setup of section.
    api_response = api_instance.update_section_page_setup(body, name, section_index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_section_page_setup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PageSetup**](PageSetup.md)| Page setup properties dto. | 
 **name** | **str**| The document name. | 
 **section_index** | **int**| Section index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**SectionPageSetupResponse**](SectionPageSetupResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_style**
> StyleResponse update_style(body, name, style_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates style properties, returns an updated style.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.StyleUpdate() # StyleUpdate | Style properties to update.
name = 'name_example' # str | The document name.
style_name = 'style_name_example' # str | Style name.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates style properties, returns an updated style.
    api_response = api_instance.update_style(body, name, style_name, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StyleUpdate**](StyleUpdate.md)| Style properties to update. | 
 **name** | **str**| The document name. | 
 **style_name** | **str**| Style name. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**StyleResponse**](StyleResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_table_cell_format**
> TableCellFormatResponse update_table_cell_format(body, name, table_row_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates a table cell format.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.TableCellFormat() # TableCellFormat | The properties.
name = 'name_example' # str | The document name.
table_row_path = 'table_row_path_example' # str | Path to table row.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates a table cell format.
    api_response = api_instance.update_table_cell_format(body, name, table_row_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_table_cell_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableCellFormat**](TableCellFormat.md)| The properties. | 
 **name** | **str**| The document name. | 
 **table_row_path** | **str**| Path to table row. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**TableCellFormatResponse**](TableCellFormatResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_table_properties**
> TablePropertiesResponse update_table_properties(body, name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates a table properties.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.TableProperties() # TableProperties | The properties.
name = 'name_example' # str | The document name.
node_path = 'node_path_example' # str | Path to the node, which contains tables.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates a table properties.
    api_response = api_instance.update_table_properties(body, name, node_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_table_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableProperties**](TableProperties.md)| The properties. | 
 **name** | **str**| The document name. | 
 **node_path** | **str**| Path to the node, which contains tables. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**TablePropertiesResponse**](TablePropertiesResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_table_properties_without_node_path**
> TablePropertiesResponse update_table_properties_without_node_path(body, name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates a table properties.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.TableProperties() # TableProperties | The properties.
name = 'name_example' # str | The document name.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates a table properties.
    api_response = api_instance.update_table_properties_without_node_path(body, name, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_table_properties_without_node_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableProperties**](TableProperties.md)| The properties. | 
 **name** | **str**| The document name. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**TablePropertiesResponse**](TablePropertiesResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_table_row_format**
> TableRowFormatResponse update_table_row_format(body, name, table_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)

Updates a table row format.

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
body = asposewordscloud.TableRowFormat() # TableRowFormat | Table row format.
name = 'name_example' # str | The document name.
table_path = 'table_path_example' # str | Path to table.
index = 56 # int | Object index.
folder = 'folder_example' # str | Original document folder. (optional)
storage = 'storage_example' # str | Original document storage. (optional)
load_encoding = 'load_encoding_example' # str | Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. (optional)
password = 'password_example' # str | Password for opening an encrypted document. (optional)
dest_file_name = 'dest_file_name_example' # str | Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. (optional)
revision_author = 'revision_author_example' # str | Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. (optional)
revision_date_time = 'revision_date_time_example' # str | The date and time to use for revisions. (optional)

try:
    # Updates a table row format.
    api_response = api_instance.update_table_row_format(body, name, table_path, index, folder=folder, storage=storage, load_encoding=load_encoding, password=password, dest_file_name=dest_file_name, revision_author=revision_author, revision_date_time=revision_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->update_table_row_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableRowFormat**](TableRowFormat.md)| Table row format. | 
 **name** | **str**| The document name. | 
 **table_path** | **str**| Path to table. | 
 **index** | **int**| Object index. | 
 **folder** | **str**| Original document folder. | [optional] 
 **storage** | **str**| Original document storage. | [optional] 
 **load_encoding** | **str**| Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML. | [optional] 
 **password** | **str**| Password for opening an encrypted document. | [optional] 
 **dest_file_name** | **str**| Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document. | [optional] 
 **revision_author** | **str**| Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions. | [optional] 
 **revision_date_time** | **str**| The date and time to use for revisions. | [optional] 

### Return type

[**TableRowFormatResponse**](TableRowFormatResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> FilesUploadResult upload_file(path, file_content=file_content, storage_name=storage_name)

Upload file

### Example
```python
from __future__ import print_function
import time
import asposewordscloud
from asposewordscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposewordscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposewordscloud.WordsApi(asposewordscloud.ApiClient(configuration))
path = 'path_example' # str | Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext              If the content is multipart and path does not contains the file name it tries to get them from filename parameter              from Content-Disposition header.
file_content = 'file_content_example' # str |  (optional)
storage_name = 'storage_name_example' # str | Storage name (optional)

try:
    # Upload file
    api_response = api_instance.upload_file(path, file_content=file_content, storage_name=storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordsApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext              If the content is multipart and path does not contains the file name it tries to get them from filename parameter              from Content-Disposition header. | 
 **file_content** | **str**|  | [optional] 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**FilesUploadResult**](FilesUploadResult.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

