documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetRangeTextOnlineRequest(document = open(os.path.join(documents_dir, 'DocumentElements/Range/RangeGet.doc'), 'rb'),range_start_identifier = 'id0.0.0',range_end_identifier = 'id0.0.1')
words_api.get_range_text_online(request)