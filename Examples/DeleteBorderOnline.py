words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
delete_request = asposewordscloud.models.requests.DeleteBorderOnlineRequest(document=request_document, border_type='left', node_path='tables/1/rows/0/cells/0')
words_api.delete_border_online(delete_request)