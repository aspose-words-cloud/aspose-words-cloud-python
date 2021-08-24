words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.doc', 'rb')
request = asposewordscloud.models.requests.GetHeaderFooterOnlineRequest(document=request_document, header_footer_index=0)
words_api.get_header_footer_online(request)