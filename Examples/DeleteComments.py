words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteCommentsRequest(name='Sample.docx')
words_api.delete_comments(delete_request)