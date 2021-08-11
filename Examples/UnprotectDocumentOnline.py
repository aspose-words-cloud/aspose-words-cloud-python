documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
unprotect_request = asposewordscloud.models.requests.UnprotectDocumentOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),protection_request = request_protection_request)
words_api.unprotect_document_online(unprotect_request)