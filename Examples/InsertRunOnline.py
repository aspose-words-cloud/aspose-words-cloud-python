documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertRunOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb'),paragraph_path = 'paragraphs/1',run = request_run)
words_api.insert_run_online(insert_request)