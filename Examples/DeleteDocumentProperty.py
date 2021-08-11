words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
remote_file_name= 'Sample.docx'

delete_request = asposewordscloud.models.requests.DeleteDocumentPropertyRequest(name = remote_file_name,property_name = 'testProp',dest_file_name = remote_file_name)
words_api.delete_document_property(delete_request)