words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteFolderRequest(path = '')
words_api.delete_folder(delete_request)