documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetCommentsOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'))
words_api.get_comments_online(request)