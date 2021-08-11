words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
remote_file_name= 'Sample.docx'

protect_request = asposewordscloud.models.requests.ProtectDocumentRequest(name = remote_file_name,protection_request = request_protection_request,dest_file_name = remote_file_name)
words_api.protect_document(protect_request)