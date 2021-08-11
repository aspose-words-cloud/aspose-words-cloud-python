documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertTableRowOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),table_path = 'sections/0/tables/2',row = request_row)
words_api.insert_table_row_online(insert_request)