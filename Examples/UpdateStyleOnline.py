documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateStyleOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),style_name = 'Heading 1',style_update = request_style_update)
words_api.update_style_online(update_request)