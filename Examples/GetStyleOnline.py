documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetStyleOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),style_name = 'Heading 1')
words_api.get_style_online(request)