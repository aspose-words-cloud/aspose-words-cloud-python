words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetDocumentDrawingObjectImageDataRequest(name='Sample.docx', index=0)
words_api.get_document_drawing_object_image_data(request)