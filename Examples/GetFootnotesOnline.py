words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.doc', 'rb')
request = asposewordscloud.models.requests.GetFootnotesOnlineRequest(document=request_document)
words_api.get_footnotes_online(request)