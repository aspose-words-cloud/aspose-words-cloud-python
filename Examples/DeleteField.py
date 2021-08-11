words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteFieldRequest(name = 'Sample.docx',index = 0)
words_api.delete_field(delete_request)