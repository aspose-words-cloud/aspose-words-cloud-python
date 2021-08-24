words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
reject_request = asposewordscloud.models.requests.RejectAllRevisionsRequest(name='Sample.docx')
words_api.reject_all_revisions(reject_request)