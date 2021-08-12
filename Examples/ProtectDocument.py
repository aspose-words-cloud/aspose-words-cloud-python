words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
protect_request = asposewordscloud.models.requests.ProtectDocumentRequest(name = 'Sample.docx',protection_request = request_protection_request)
words_api.protect_document(protect_request)