words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
accept_request = asposewordscloud.models.requests.AcceptAllRevisionsOnlineRequest(document=request_document)
words_api.accept_all_revisions_online(accept_request)