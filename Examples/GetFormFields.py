words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetFormFieldsRequest(name = 'Sample.docx')
words_api.get_form_fields(request)