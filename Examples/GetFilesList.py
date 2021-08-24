words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetFilesListRequest(path='')
words_api.get_files_list(request)