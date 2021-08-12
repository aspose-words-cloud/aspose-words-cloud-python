documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetParagraphListFormatOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb'),index = 0)
words_api.get_paragraph_list_format_online(request)