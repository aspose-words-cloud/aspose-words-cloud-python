documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateBorderOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),border_properties = request_border_properties,border_type = 'left',node_path = 'tables/1/rows/0/cells/0')
words_api.update_border_online(update_request)