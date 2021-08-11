documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertTableOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),table = request_table,node_path = '')
words_api.insert_table_online(insert_request)