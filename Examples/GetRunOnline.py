documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetRunOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),paragraph_path = 'paragraphs/0',index = 0)
words_api.get_run_online(request)