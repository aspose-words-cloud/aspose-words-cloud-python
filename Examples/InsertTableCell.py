words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_cell = asposewordscloud.TableCellInsert()
insert_request = asposewordscloud.models.requests.InsertTableCellRequest(name='Sample.docx', table_row_path='sections/0/tables/2/rows/0', cell=request_cell)
words_api.insert_table_cell(insert_request)