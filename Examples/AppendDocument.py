words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
remote_file_name= 'Sample.docx'

request_document_list_document_entries0 = asposewordscloud.DocumentEntry(href=remote_file_name, import_format_mode='KeepSourceFormatting')
request_document_list_document_entries = [request_document_list_document_entries0]
request_document_list = asposewordscloud.DocumentEntryList(document_entries=request_document_list_document_entries)
append_request = asposewordscloud.models.requests.AppendDocumentRequest(name=remote_file_name, document_list=request_document_list)
words_api.append_document(append_request)