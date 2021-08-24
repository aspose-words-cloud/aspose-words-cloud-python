words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetDocumentDrawingObjectByIndexOnlineRequest(document=request_document, index=0, node_path='sections/0')
words_api.get_document_drawing_object_by_index_online(request)