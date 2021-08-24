words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetBorderOnlineRequest(document=request_document, border_type='left', node_path='tables/1/rows/0/cells/0')
words_api.get_border_online(request)