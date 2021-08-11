documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetBookmarkByNameOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),bookmark_name = 'aspose')
words_api.get_bookmark_by_name_online(request)