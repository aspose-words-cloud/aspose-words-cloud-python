words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
delete_request = asposewordscloud.models.requests.DeleteTableCellOnlineRequest(document=request_document, table_row_path='sections/0/tables/2/rows/0', index=0)
words_api.delete_table_cell_online(delete_request)