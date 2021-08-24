words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
delete_request = asposewordscloud.models.requests.DeleteCommentOnlineRequest(document=request_document, comment_index=0)
words_api.delete_comment_online(delete_request)