documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteFormFieldOnlineRequest(document = open(os.path.join(documents_dir, '/FormFilled.docx'), 'rb'),index = 0,node_path = 'sections/0')
words_api.delete_form_field_online(delete_request)