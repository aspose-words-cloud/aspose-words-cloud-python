words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_list_insert = asposewordscloud.ListInsert(template='OutlineLegal')
insert_request = asposewordscloud.models.requests.InsertListRequest(name='TestGetLists.doc', list_insert=request_list_insert)
words_api.insert_list(insert_request)