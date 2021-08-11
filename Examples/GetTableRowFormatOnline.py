documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetTableRowFormatOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),table_path = 'sections/0/tables/2',index = 0)
words_api.get_table_row_format_online(request)