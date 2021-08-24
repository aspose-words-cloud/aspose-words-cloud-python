words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
delete_request = asposewordscloud.models.requests.DeleteFormFieldOnlineRequest(document=request_document, index=0, node_path='sections/0')
words_api.delete_form_field_online(delete_request)