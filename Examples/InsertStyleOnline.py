documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertStyleOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),style_insert = request_style_insert)
words_api.insert_style_online(insert_request)