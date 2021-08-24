words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.doc', 'rb')
request = asposewordscloud.models.requests.GetRangeTextOnlineRequest(document=request_document, range_start_identifier='id0.0.0', range_end_identifier='id0.0.1')
words_api.get_range_text_online(request)