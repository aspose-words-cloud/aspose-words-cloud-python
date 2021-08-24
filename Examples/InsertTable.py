words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_table = asposewordscloud.TableInsert(columns_count=5, rows_count=4)
insert_request = asposewordscloud.models.requests.InsertTableRequest(name='Sample.docx', table=request_table)
words_api.insert_table(insert_request)