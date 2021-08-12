documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
remove_request = asposewordscloud.models.requests.RemoveRangeOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb'),range_start_identifier = 'id0.0.0',range_end_identifier = 'id0.0.1')
words_api.remove_range_online(remove_request)