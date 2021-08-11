words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
remote_file_name= 'Sample.docx'

replace_request = asposewordscloud.models.requests.ReplaceTextRequest(name = remote_file_name,replace_text = request_replace_text,dest_file_name = remote_file_name)
words_api.replace_text(replace_request)