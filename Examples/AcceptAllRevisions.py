words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
accept_request = asposewordscloud.models.requests.AcceptAllRevisionsRequest(name = 'Sample.docx')
words_api.accept_all_revisions(accept_request)