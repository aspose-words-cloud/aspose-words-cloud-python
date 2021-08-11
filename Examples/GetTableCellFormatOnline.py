documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetTableCellFormatOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),table_row_path = 'sections/0/tables/2/rows/0',index = 0)
words_api.get_table_cell_format_online(request)