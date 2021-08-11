words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetTableRequest(name = 'Sample.docx',index = 1)
words_api.get_table(request)