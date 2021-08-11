documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetDocumentDrawingObjectOleDataOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),index = 0,node_path = 'sections/0')
words_api.get_document_drawing_object_ole_data_online(request)