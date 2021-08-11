documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetFieldOnlineRequest(document = open(os.path.join(documents_dir, '/GetField.docx'), 'rb'),index = 0,node_path = 'sections/0/paragraphs/0')
words_api.get_field_online(request)