words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_row = asposewordscloud.TableRowInsert(columns_count=5)
insert_request = asposewordscloud.models.requests.InsertTableRowRequest(name='Sample.docx', table_path='sections/0/tables/2', row=request_row)
words_api.insert_table_row(insert_request)