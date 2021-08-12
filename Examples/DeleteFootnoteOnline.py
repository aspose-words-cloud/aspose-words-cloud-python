documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteFootnoteOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb'),index = 0)
words_api.delete_footnote_online(delete_request)