words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
remote_file_name= 'Sample.docx'

delete_request = asposewordscloud.models.requests.DeleteCommentRequest(name = remote_file_name,comment_index = 0,dest_file_name = remote_file_name)
words_api.delete_comment(delete_request)