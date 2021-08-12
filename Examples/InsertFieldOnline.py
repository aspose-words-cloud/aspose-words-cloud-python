documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertFieldOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),field = request_field,node_path = 'sections/0/paragraphs/0')
words_api.insert_field_online(insert_request)