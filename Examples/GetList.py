words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetListRequest(name='TestGetLists.doc', list_id=1)
words_api.get_list(request)