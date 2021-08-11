documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
accept_request = asposewordscloud.models.requests.AcceptAllRevisionsOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'))
words_api.accept_all_revisions_online(accept_request)