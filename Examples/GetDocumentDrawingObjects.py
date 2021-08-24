words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetDocumentDrawingObjectsRequest(name='Sample.docx')
words_api.get_document_drawing_objects(request)