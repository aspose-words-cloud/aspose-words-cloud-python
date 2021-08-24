words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_list_update = asposewordscloud.ListLevelUpdate(alignment='Right')
update_request = asposewordscloud.models.requests.UpdateListLevelRequest(name='TestGetLists.doc', list_id=1, list_level=1, list_update=request_list_update)
words_api.update_list_level(update_request)