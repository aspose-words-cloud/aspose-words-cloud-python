words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateBorderRequest(name = 'Sample.docx',border_type = 'left',border_properties = request_border_properties,node_path = 'tables/1/rows/0/cells/0')
words_api.update_border(update_request)