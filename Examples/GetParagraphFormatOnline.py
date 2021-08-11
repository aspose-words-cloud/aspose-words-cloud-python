documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetParagraphFormatOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),index = 0,node_path = '')
words_api.get_paragraph_format_online(request)