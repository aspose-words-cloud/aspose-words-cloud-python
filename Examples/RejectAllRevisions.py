words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
remote_file_name= 'Sample.docx'

reject_request = asposewordscloud.models.requests.RejectAllRevisionsRequest(name = remote_file_name,dest_file_name = remote_file_name)
words_api.reject_all_revisions(reject_request)