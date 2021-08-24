words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetFormFieldOnlineRequest(document=request_document, index=0, node_path='sections/0')
words_api.get_form_field_online(request)