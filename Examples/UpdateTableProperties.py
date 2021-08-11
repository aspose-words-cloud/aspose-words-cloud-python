words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateTablePropertiesRequest(name = 'Sample.docx',index = 1,properties = request_properties)
words_api.update_table_properties(update_request)