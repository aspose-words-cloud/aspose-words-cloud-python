words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteDocumentPropertyRequest(name='Sample.docx', property_name='testProp')
words_api.delete_document_property(delete_request)