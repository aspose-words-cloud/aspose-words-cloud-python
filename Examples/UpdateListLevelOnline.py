documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateListLevelOnlineRequest(document = open(os.path.join(documents_dir, 'DocumentElements/Lists/ListsGet.doc'), 'rb'),list_id = 1,list_update = request_list_update,list_level = 1)
words_api.update_list_level_online(update_request)