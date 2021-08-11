documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteBordersOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),node_path = 'tables/1/rows/0/cells/0')
words_api.delete_borders_online(delete_request)