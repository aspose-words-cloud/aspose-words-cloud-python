words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteDrawingObjectRequest(name='Sample.docx', index=0)
words_api.delete_drawing_object(delete_request)