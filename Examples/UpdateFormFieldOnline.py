documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateFormFieldOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),form_field = request_form_field,index = 0,node_path = 'sections/0')
words_api.update_form_field_online(update_request)