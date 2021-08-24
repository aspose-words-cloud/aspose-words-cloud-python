words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteFormFieldRequest(name='Sample.docx', index=0)
words_api.delete_form_field(delete_request)