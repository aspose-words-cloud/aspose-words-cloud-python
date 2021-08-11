words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteRunRequest(name = 'Sample.docx',paragraph_path = 'paragraphs/1',index = 0)
words_api.delete_run(delete_request)