documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetTablePropertiesOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),index = 1,node_path = '')
words_api.get_table_properties_online(request)