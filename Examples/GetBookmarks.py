words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetBookmarksRequest(name='Sample.docx')
words_api.get_bookmarks(request)