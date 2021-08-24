words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetTableCellFormatOnlineRequest(document=request_document, table_row_path='sections/0/tables/2/rows/0', index=0)
words_api.get_table_cell_format_online(request)