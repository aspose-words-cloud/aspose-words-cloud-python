words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteFieldsRequest(name = 'Sample.docx')
words_api.delete_fields(delete_request)