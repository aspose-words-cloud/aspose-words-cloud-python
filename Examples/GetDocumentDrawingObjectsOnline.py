documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetDocumentDrawingObjectsOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),node_path = 'sections/0')
words_api.get_document_drawing_objects_online(request)