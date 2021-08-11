documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertCommentOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),comment = request_comment)
words_api.insert_comment_online(insert_request)