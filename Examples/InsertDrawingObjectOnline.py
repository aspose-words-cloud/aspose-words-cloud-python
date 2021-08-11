documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertDrawingObjectOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),drawing_object = request_drawing_object,image_file = open(os.path.join(documents_dir, 'Common/aspose-cloud.png'), 'rb'),node_path = '')
words_api.insert_drawing_object_online(insert_request)