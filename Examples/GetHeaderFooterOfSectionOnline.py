words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.doc', 'rb')
request = asposewordscloud.models.requests.GetHeaderFooterOfSectionOnlineRequest(document=request_document, header_footer_index=0, section_index=0)
words_api.get_header_footer_of_section_online(request)