words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetDocumentPropertyRequest(name='Sample.docx', property_name='Author')
words_api.get_document_property(request)