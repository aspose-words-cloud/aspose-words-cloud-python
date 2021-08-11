documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateSectionPageSetupOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),section_index = 0,page_setup = request_page_setup)
words_api.update_section_page_setup_online(update_request)