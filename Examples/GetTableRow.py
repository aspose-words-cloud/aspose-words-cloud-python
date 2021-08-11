words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetTableRowRequest(name = 'Sample.docx',table_path = 'tables/1',index = 0)
words_api.get_table_row(request)