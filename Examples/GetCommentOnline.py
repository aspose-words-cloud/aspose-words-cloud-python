documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetCommentOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),comment_index = 0)
words_api.get_comment_online(request)