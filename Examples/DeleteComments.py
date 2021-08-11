words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
remote_file_name= 'Sample.docx'

delete_request = asposewordscloud.models.requests.DeleteCommentsRequest(name = remote_file_name,dest_file_name = remote_file_name)
words_api.delete_comments(delete_request)