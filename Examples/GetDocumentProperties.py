words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetDocumentPropertiesRequest(name='Sample.docx')
words_api.get_document_properties(request)