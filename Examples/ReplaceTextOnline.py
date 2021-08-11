documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
replace_request = asposewordscloud.models.requests.ReplaceTextOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),replace_text = request_replace_text)
words_api.replace_text_online(replace_request)