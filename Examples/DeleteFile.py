words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteFileRequest(path='Sample.docx')
words_api.delete_file(delete_request)