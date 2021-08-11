documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
search_request = asposewordscloud.models.requests.SearchOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),pattern = 'aspose')
words_api.search_online(search_request)