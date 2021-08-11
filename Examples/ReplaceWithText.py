words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
replace_request = asposewordscloud.models.requests.ReplaceWithTextRequest(name = 'Sample.docx',range_start_identifier = 'id0.0.0',range_text = request_range_text,range_end_identifier = 'id0.0.1')
words_api.replace_with_text(replace_request)