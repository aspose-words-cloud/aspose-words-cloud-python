words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.doc', 'rb')
delete_request = asposewordscloud.models.requests.DeleteHeaderFooterOnlineRequest(document=request_document, section_path='', index=0)
words_api.delete_header_footer_online(delete_request)