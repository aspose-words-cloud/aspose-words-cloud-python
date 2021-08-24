words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
download_request = asposewordscloud.models.requests.DownloadFileRequest(path='Sample.docx')
words_api.download_file(download_request)