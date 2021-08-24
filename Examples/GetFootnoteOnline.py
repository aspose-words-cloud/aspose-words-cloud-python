words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.doc', 'rb')
request = asposewordscloud.models.requests.GetFootnoteOnlineRequest(document=request_document, index=0)
words_api.get_footnote_online(request)