words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertHeaderFooterRequest(name='Sample.docx', section_path='', header_footer_type='FooterEven')
words_api.insert_header_footer(insert_request)