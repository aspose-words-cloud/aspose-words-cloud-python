words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
search_request = asposewordscloud.models.requests.SearchOnlineRequest(document=request_document, pattern='aspose')
words_api.search_online(search_request)