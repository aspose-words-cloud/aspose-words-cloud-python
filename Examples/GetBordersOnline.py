words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetBordersOnlineRequest(document=request_document, node_path='tables/1/rows/0/cells/0')
words_api.get_borders_online(request)