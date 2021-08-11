documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetSectionPageSetupOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),section_index = 0)
words_api.get_section_page_setup_online(request)