documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertListOnlineRequest(document = open(os.path.join(documents_dir, 'DocumentElements/Lists/ListsGet.doc'), 'rb'),list_insert = request_list_insert)
words_api.insert_list_online(insert_request)