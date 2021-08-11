words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
unprotect_request = asposewordscloud.models.requests.UnprotectDocumentRequest(name = 'Sample.docx',protection_request = request_protection_request)
words_api.unprotect_document(unprotect_request)