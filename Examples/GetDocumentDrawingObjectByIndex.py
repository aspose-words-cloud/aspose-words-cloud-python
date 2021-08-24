words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetDocumentDrawingObjectByIndexRequest(name='Sample.docx', index=0)
words_api.get_document_drawing_object_by_index(request)