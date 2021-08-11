documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetFieldsOnlineRequest(document = open(os.path.join(documents_dir, '/GetField.docx'), 'rb'),node_path = 'sections/0')
words_api.get_fields_online(request)