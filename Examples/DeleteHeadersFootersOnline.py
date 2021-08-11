documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteHeadersFootersOnlineRequest(document = open(os.path.join(documents_dir, 'DocumentElements/HeaderFooters/HeadersFooters.doc'), 'rb'),section_path = '')
words_api.delete_headers_footers_online(delete_request)