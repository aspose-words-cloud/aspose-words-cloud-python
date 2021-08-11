documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetRunFontOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),paragraph_path = 'paragraphs/0',index = 0)
words_api.get_run_font_online(request)