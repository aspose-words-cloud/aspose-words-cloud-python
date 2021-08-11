documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateFieldOnlineRequest(document = open(os.path.join(documents_dir, '/GetField.docx'), 'rb'),field = request_field,index = 0,node_path = 'sections/0/paragraphs/0')
words_api.update_field_online(update_request)