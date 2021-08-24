words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetTableRowFormatOnlineRequest(document=request_document, table_path='sections/0/tables/2', index=0)
words_api.get_table_row_format_online(request)