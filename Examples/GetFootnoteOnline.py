documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetFootnoteOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb'),index = 0)
words_api.get_footnote_online(request)