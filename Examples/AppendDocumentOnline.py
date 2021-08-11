documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
append_request = asposewordscloud.models.requests.AppendDocumentOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),document_list = request_document_list)
words_api.append_document_online(append_request)