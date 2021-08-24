words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetDocumentFieldNamesRequest(name='Sample.docx')
words_api.get_document_field_names(request)