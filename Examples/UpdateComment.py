words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateCommentRequest(name = 'Sample.docx',comment_index = 0,comment = request_comment)
words_api.update_comment(update_request)