words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetSectionPageSetupOnlineRequest(document=request_document, section_index=0)
words_api.get_section_page_setup_online(request)