words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertListRequest(name = 'TestGetLists.doc',list_insert = request_list_insert)
words_api.insert_list(insert_request)