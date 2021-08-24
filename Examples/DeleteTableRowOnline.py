words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
delete_request = asposewordscloud.models.requests.DeleteTableRowOnlineRequest(document=request_document, table_path='tables/1', index=0)
words_api.delete_table_row_online(delete_request)