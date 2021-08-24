words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteTableRowRequest(name='Sample.docx', table_path='tables/1', index=0)
words_api.delete_table_row(delete_request)