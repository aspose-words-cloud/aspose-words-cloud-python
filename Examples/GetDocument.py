words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetDocumentRequest(document_name = 'Sample.docx')
words_api.get_document(request)