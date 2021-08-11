documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertTableCellOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),table_row_path = 'sections/0/tables/2/rows/0',cell = request_cell)
words_api.insert_table_cell_online(insert_request)