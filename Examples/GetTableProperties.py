words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetTablePropertiesRequest(name='Sample.docx', index=1)
words_api.get_table_properties(request)