documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteRunOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb'),paragraph_path = 'paragraphs/1',index = 0)
words_api.delete_run_online(delete_request)