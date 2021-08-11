documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetFootnoteOnlineRequest(document = open(os.path.join(documents_dir, '/Footnote.doc'), 'rb'),index = 0,node_path = '')
words_api.get_footnote_online(request)