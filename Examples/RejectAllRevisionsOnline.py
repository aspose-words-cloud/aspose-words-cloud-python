words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
reject_request = asposewordscloud.models.requests.RejectAllRevisionsOnlineRequest(document=request_document)
words_api.reject_all_revisions_online(reject_request)