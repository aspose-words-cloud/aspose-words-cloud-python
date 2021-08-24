words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetCommentOnlineRequest(document=request_document, comment_index=0)
words_api.get_comment_online(request)