words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.doc', 'rb')
remove_request = asposewordscloud.models.requests.RemoveRangeOnlineRequest(document=request_document, range_start_identifier='id0.0.0', range_end_identifier='id0.0.1')
words_api.remove_range_online(remove_request)