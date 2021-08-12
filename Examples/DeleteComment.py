words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteCommentRequest(name = 'Sample.docx',comment_index = 0)
words_api.delete_comment(delete_request)