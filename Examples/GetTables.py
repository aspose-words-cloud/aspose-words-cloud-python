words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetTablesRequest(name='Sample.docx')
words_api.get_tables(request)