words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertRunRequest(name = 'Sample.docx',paragraph_path = 'paragraphs/1',run = request_run)
words_api.insert_run(insert_request)