documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetHeaderFooterOfSectionOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb'),header_footer_index = 0,section_index = 0)
words_api.get_header_footer_of_section_online(request)