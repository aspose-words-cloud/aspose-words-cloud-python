words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request_document_list_document_entries0 = asposewordscloud.DocumentEntry(href='Sample.docx', import_format_mode='KeepSourceFormatting')
request_document_list_document_entries = [request_document_list_document_entries0]
request_document_list = asposewordscloud.DocumentEntryList(document_entries=request_document_list_document_entries)
append_request = asposewordscloud.models.requests.AppendDocumentOnlineRequest(document=request_document, document_list=request_document_list)
words_api.append_document_online(append_request)