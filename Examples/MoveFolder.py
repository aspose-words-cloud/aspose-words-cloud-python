words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
move_request = asposewordscloud.models.requests.MoveFolderRequest(dest_path = '/TestMoveFolderDest_Sample',src_path = '/TestMoveFolderSrc')
words_api.move_folder(move_request)