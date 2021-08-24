words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_protection_request = asposewordscloud.ProtectionRequest(password='aspose')
unprotect_request = asposewordscloud.models.requests.UnprotectDocumentRequest(name='Sample.docx', protection_request=request_protection_request)
words_api.unprotect_document(unprotect_request)