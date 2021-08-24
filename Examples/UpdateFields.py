words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateFieldsRequest(name='Sample.docx')
words_api.update_fields(update_request)