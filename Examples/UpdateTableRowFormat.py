words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateTableRowFormatRequest(name = 'Sample.docx',table_path = 'sections/0/tables/2',index = 0,format = request_format)
words_api.update_table_row_format(update_request)