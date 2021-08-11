documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetSectionOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),section_index = 0)
words_api.get_section_online(request)