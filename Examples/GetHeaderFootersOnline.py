words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.doc', 'rb')
request = asposewordscloud.models.requests.GetHeaderFootersOnlineRequest(document=request_document, section_path='')
words_api.get_header_footers_online(request)