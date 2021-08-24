words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.doc', 'rb')
delete_request = asposewordscloud.models.requests.DeleteFootnoteOnlineRequest(document=request_document, index=0)
words_api.delete_footnote_online(delete_request)