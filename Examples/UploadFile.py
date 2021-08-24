words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_file_content = open('Sample.docx', 'rb')
upload_request = asposewordscloud.models.requests.UploadFileRequest(file_content=request_file_content, path='Sample.docx')
words_api.upload_file(upload_request)