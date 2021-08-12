documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertHeaderFooterOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb'),section_path = '',header_footer_type = 'FooterEven')
words_api.insert_header_footer_online(insert_request)