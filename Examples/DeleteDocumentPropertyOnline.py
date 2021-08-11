documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteDocumentPropertyOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),property_name = 'testProp')
words_api.delete_document_property_online(delete_request)