words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetListsRequest(name = 'TestGetLists.doc')
words_api.get_lists(request)