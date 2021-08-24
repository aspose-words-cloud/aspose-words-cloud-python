words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetDocumentDrawingObjectImageDataOnlineRequest(document=request_document, index=0, node_path='sections/0')
words_api.get_document_drawing_object_image_data_online(request)