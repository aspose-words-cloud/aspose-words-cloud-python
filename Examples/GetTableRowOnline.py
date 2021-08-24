words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetTableRowOnlineRequest(document=request_document, table_path='tables/1', index=0)
words_api.get_table_row_online(request)