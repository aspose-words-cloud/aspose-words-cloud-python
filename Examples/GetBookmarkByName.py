words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetBookmarkByNameRequest(name='Sample.docx', bookmark_name='aspose')
words_api.get_bookmark_by_name(request)