words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
save_request = asposewordscloud.models.requests.SaveAsRequest(name = 'Sample.docx',save_options_data = request_save_options_data)
words_api.save_as(save_request)