words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
delete_request = asposewordscloud.models.requests.DeleteMacrosOnlineRequest(document=request_document)
words_api.delete_macros_online(delete_request)