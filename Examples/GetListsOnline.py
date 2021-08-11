documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetListsOnlineRequest(document = open(os.path.join(documents_dir, 'DocumentElements/Lists/ListsGet.doc'), 'rb'))
words_api.get_lists_online(request)