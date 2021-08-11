words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertCommentRequest(name = 'Sample.docx',comment = request_comment)
words_api.insert_comment(insert_request)