words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.doc', 'rb')
insert_request = asposewordscloud.models.requests.InsertHeaderFooterOnlineRequest(document=request_document, section_path='', header_footer_type='FooterEven')
words_api.insert_header_footer_online(insert_request)