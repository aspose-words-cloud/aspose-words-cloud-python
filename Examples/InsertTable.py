words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertTableRequest(name = 'Sample.docx',table = request_table)
words_api.insert_table(insert_request)