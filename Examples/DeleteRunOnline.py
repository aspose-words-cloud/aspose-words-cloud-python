words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.doc', 'rb')
delete_request = asposewordscloud.models.requests.DeleteRunOnlineRequest(document=request_document, paragraph_path='paragraphs/1', index=0)
words_api.delete_run_online(delete_request)