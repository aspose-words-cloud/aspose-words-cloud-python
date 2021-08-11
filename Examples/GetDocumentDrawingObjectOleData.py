words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetDocumentDrawingObjectOleDataRequest(name = 'Sample.docx',index = 0)
words_api.get_document_drawing_object_ole_data(request)