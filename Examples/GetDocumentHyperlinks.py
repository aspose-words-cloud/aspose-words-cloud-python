words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetDocumentHyperlinksRequest(name='Sample.docx')
words_api.get_document_hyperlinks(request)