documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetFootnotesOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb'))
words_api.get_footnotes_online(request)