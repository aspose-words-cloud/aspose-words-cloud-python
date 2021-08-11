words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetDocumentProtectionRequest(name = 'Sample.docx')
words_api.get_document_protection(request)