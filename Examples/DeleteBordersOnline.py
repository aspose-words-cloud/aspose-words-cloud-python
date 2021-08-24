words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
delete_request = asposewordscloud.models.requests.DeleteBordersOnlineRequest(document=request_document, node_path='tables/1/rows/0/cells/0')
words_api.delete_borders_online(delete_request)