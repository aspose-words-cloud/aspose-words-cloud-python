words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
save_request = asposewordscloud.models.requests.SaveAsRangeRequest(name = 'Sample.docx',range_start_identifier = 'id0.0.0',document_parameters = request_document_parameters,range_end_identifier = 'id0.0.1')
words_api.save_as_range(save_request)