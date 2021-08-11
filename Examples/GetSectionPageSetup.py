words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetSectionPageSetupRequest(name = 'Sample.docx',section_index = 0)
words_api.get_section_page_setup(request)