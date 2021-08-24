words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetTablePropertiesOnlineRequest(document=request_document, index=1)
words_api.get_table_properties_online(request)