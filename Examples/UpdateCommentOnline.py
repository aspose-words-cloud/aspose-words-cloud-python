documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateCommentOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),comment_index = 0,comment = request_comment)
words_api.update_comment_online(update_request)