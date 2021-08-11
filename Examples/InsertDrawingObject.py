documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertDrawingObjectRequest(name = 'Sample.docx',drawing_object = request_drawing_object,image_file = open(os.path.join(documents_dir, 'Common/aspose-cloud.png'), 'rb'))
words_api.insert_drawing_object(insert_request)