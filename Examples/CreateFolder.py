words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
create_request = asposewordscloud.models.requests.CreateFolderRequest(path='/TestCreateFolder')
words_api.create_folder(create_request)