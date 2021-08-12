documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateDrawingObjectOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),drawing_object = request_drawing_object,image_file = open(os.path.join(documents_dir, 'Common/aspose-cloud.png'), 'rb'),index = 0)
words_api.update_drawing_object_online(update_request)