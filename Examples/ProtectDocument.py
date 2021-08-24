words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_protection_request = asposewordscloud.ProtectionRequest(password='123', protection_type='ReadOnly')
protect_request = asposewordscloud.models.requests.ProtectDocumentRequest(name='Sample.docx', protection_request=request_protection_request)
words_api.protect_document(protect_request)