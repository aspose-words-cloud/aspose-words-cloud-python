words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
remote_file_name= 'Sample.docx'

create_request = asposewordscloud.models.requests.CreateOrUpdateDocumentPropertyRequest(name = remote_file_name,property_name = 'AsposeAuthor',_property = request_property,dest_file_name = remote_file_name)
words_api.create_or_update_document_property(create_request)