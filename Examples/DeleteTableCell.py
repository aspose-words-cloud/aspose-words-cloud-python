words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteTableCellRequest(name='Sample.docx', table_row_path='sections/0/tables/2/rows/0', index=0)
words_api.delete_table_cell(delete_request)