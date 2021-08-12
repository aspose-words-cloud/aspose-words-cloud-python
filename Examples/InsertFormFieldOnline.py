documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertFormFieldOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),form_field = request_form_field,node_path = 'sections/0/paragraphs/0')
words_api.insert_form_field_online(insert_request)