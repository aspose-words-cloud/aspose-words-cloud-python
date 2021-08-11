words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertStyleRequest(name = 'Sample.docx',style_insert = request_style_insert)
words_api.insert_style(insert_request)