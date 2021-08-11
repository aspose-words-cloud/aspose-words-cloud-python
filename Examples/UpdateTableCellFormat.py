words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateTableCellFormatRequest(name = 'Sample.docx',table_row_path = 'sections/0/tables/2/rows/0',index = 0,format = request_format)
words_api.update_table_cell_format(update_request)