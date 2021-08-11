documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateTableCellFormatOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),table_row_path = 'sections/0/tables/2/rows/0',format = request_format,index = 0)
words_api.update_table_cell_format_online(update_request)