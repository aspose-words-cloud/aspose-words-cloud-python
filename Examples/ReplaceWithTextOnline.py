documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
replace_request = asposewordscloud.models.requests.ReplaceWithTextOnlineRequest(document = open(os.path.join(documents_dir, 'DocumentElements/Range/RangeGet.doc'), 'rb'),range_start_identifier = 'id0.0.0',range_text = request_range_text,range_end_identifier = 'id0.0.1')
words_api.replace_with_text_online(replace_request)