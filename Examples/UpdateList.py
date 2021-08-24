words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_list_update = asposewordscloud.ListUpdate(is_restart_at_each_section=True)
update_request = asposewordscloud.models.requests.UpdateListRequest(name='TestGetLists.doc', list_id=1, list_update=request_list_update)
words_api.update_list(update_request)