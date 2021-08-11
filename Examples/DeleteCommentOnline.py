documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteCommentOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),comment_index = 0)
words_api.delete_comment_online(delete_request)