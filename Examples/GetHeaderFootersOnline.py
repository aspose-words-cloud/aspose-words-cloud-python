documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetHeaderFootersOnlineRequest(document = open(os.path.join(documents_dir, 'DocumentElements/HeaderFooters/HeadersFooters.doc'), 'rb'),section_path = '')
words_api.get_header_footers_online(request)