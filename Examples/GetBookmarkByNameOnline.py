words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetBookmarkByNameOnlineRequest(document=request_document, bookmark_name='aspose')
words_api.get_bookmark_by_name_online(request)