words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.doc', 'rb')
request = asposewordscloud.models.requests.GetListOnlineRequest(document=request_document, list_id=1)
words_api.get_list_online(request)