words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetCommentsRequest(name = 'Sample.docx')
words_api.get_comments(request)