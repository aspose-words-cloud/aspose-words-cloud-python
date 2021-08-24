words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetCommentRequest(name='Sample.docx', comment_index=0)
words_api.get_comment(request)