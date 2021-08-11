documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetTableRowOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),table_path = 'tables/1',index = 0)
words_api.get_table_row_online(request)