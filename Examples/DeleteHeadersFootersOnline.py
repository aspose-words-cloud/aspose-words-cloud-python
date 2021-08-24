words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.doc', 'rb')
delete_request = asposewordscloud.models.requests.DeleteHeadersFootersOnlineRequest(document=request_document, section_path='')
words_api.delete_headers_footers_online(delete_request)