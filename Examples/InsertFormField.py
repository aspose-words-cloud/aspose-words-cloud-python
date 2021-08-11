words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
remote_file_name= 'Sample.docx'

insert_request = asposewordscloud.models.requests.InsertFormFieldRequest(name = remote_file_name,form_field = request_form_field,dest_file_name = remote_file_name)
words_api.insert_form_field(insert_request)