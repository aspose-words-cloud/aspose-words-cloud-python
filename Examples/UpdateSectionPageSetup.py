words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateSectionPageSetupRequest(name = 'Sample.docx',section_index = 0,page_setup = request_page_setup)
words_api.update_section_page_setup(update_request)