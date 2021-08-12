documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteHeaderFooterOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb'),section_path = '',index = 0)
words_api.delete_header_footer_online(delete_request)