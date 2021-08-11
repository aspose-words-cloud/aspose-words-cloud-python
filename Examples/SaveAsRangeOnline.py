documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
save_request = asposewordscloud.models.requests.SaveAsRangeOnlineRequest(document = open(os.path.join(documents_dir, 'DocumentElements/Range/RangeGet.doc'), 'rb'),range_start_identifier = 'id0.0.0',document_parameters = request_document_parameters,range_end_identifier = 'id0.0.1')
words_api.save_as_range_online(save_request)