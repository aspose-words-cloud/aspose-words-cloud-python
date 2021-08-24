words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetTableRowFormatRequest(name='Sample.docx', table_path='sections/0/tables/2', index=0)
words_api.get_table_row_format(request)