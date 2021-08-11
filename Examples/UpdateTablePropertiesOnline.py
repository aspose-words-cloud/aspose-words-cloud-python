documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateTablePropertiesOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),properties = request_properties,index = 1,node_path = '')
words_api.update_table_properties_online(update_request)