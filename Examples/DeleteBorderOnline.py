documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteBorderOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),border_type = 'left',node_path = 'tables/1/rows/0/cells/0')
words_api.delete_border_online(delete_request)