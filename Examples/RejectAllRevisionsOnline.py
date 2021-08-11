documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
reject_request = asposewordscloud.models.requests.RejectAllRevisionsOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'))
words_api.reject_all_revisions_online(reject_request)