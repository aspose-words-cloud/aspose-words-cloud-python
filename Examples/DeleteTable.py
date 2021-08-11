words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteTableRequest(name = 'Sample.docx',index = 1)
words_api.delete_table(delete_request)