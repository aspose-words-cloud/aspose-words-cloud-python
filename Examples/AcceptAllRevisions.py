words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
remote_file_name= 'Sample.docx'

accept_request = asposewordscloud.models.requests.AcceptAllRevisionsRequest(name = remote_file_name,dest_file_name = remote_file_name)
words_api.accept_all_revisions(accept_request)