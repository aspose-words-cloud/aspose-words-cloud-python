documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteTableRowOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),table_path = 'tables/1',index = 0)
words_api.delete_table_row_online(delete_request)