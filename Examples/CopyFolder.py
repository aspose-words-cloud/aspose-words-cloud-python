words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
folder_to_copy= '/TestCopyFolder'

copy_request = asposewordscloud.models.requests.CopyFolderRequest(dest_path = folder_to_copy + 'Dest',src_path = folder_to_copy + 'Src')
words_api.copy_folder(copy_request)