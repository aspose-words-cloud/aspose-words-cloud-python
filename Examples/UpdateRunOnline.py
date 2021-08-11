documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateRunOnlineRequest(document = open(os.path.join(documents_dir, 'DocumentElements/Runs/Run.doc'), 'rb'),paragraph_path = 'paragraphs/1',run = request_run,index = 0)
words_api.update_run_online(update_request)