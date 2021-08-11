words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
remove_request = asposewordscloud.models.requests.RemoveRangeRequest(name = 'Sample.docx',range_start_identifier = 'id0.0.0',range_end_identifier = 'id0.0.1')
words_api.remove_range(remove_request)