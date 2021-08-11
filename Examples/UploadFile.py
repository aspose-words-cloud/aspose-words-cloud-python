documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
upload_request = asposewordscloud.models.requests.UploadFileRequest(file_content = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),path = 'Sample.docx')
words_api.upload_file(upload_request)