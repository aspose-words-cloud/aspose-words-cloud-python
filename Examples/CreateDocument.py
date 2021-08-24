words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
create_request = asposewordscloud.models.requests.CreateDocumentRequest(file_name='Sample.docx')
words_api.create_document(create_request)