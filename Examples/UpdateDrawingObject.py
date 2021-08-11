documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateDrawingObjectRequest(name = 'Sample.docx',drawing_object = request_drawing_object,image_file = open(os.path.join(documents_dir, 'Common/aspose-cloud.png'), 'rb'),index = 0)
words_api.update_drawing_object(update_request)