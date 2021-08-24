words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
move_request = asposewordscloud.models.requests.MoveFileRequest(dest_path='/TestMoveFileDest_Sample.docx', src_path='Sample.docx')
words_api.move_file(move_request)