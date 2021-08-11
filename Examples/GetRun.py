words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetRunRequest(name = 'Sample.docx',paragraph_path = 'paragraphs/0',index = 0)
words_api.get_run(request)