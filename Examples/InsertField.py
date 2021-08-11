words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertFieldRequest(name = 'Sample.docx',field = request_field)
words_api.insert_field(insert_request)