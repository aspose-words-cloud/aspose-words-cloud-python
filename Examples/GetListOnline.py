documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetListOnlineRequest(document = open(os.path.join(documents_dir, 'DocumentElements/Lists/ListsGet.doc'), 'rb'),list_id = 1)
words_api.get_list_online(request)