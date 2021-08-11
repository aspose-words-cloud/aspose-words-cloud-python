documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
copy_request = asposewordscloud.models.requests.CopyStyleOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),style_copy = request_style_copy)
words_api.copy_style_online(copy_request)