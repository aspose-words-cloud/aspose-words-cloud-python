words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
remote_file_name= 'Sample.docx'

insert_request = asposewordscloud.models.requests.InsertPageNumbersRequest(name = remote_file_name,page_number = request_page_number,dest_file_name = remote_file_name)
words_api.insert_page_numbers(insert_request)