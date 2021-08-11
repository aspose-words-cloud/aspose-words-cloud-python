words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
copy_request = asposewordscloud.models.requests.CopyStyleRequest(name = 'Sample.docx',style_copy = request_style_copy)
words_api.copy_style(copy_request)