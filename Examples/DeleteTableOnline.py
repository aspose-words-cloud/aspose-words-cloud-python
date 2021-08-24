words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
delete_request = asposewordscloud.models.requests.DeleteTableOnlineRequest(document=request_document, index=1)
words_api.delete_table_online(delete_request)