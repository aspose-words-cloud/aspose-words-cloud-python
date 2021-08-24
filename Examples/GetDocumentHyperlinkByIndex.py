words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetDocumentHyperlinkByIndexRequest(name='Sample.docx', hyperlink_index=0)
words_api.get_document_hyperlink_by_index(request)