words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
remote_file_name= 'Sample.docx'

delete_request = asposewordscloud.models.requests.DeleteFormFieldRequest(name = remote_file_name,index = 0,dest_file_name = remote_file_name)
words_api.delete_form_field(delete_request)