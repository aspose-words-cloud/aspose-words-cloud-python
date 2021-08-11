documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetBorderOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),border_type = 'left',node_path = 'tables/1/rows/0/cells/0')
words_api.get_border_online(request)