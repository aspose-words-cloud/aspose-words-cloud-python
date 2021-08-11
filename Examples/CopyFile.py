words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
copy_request = asposewordscloud.models.requests.CopyFileRequest(dest_path = '/TestCopyFileDest.docx',src_path = 'Sample.docx')
words_api.copy_file(copy_request)