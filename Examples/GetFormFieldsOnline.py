documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetFormFieldsOnlineRequest(document = open(os.path.join(documents_dir, '/FormFilled.docx'), 'rb'),node_path = 'sections/0')
words_api.get_form_fields_online(request)