words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
delete_request = asposewordscloud.models.requests.DeleteDocumentPropertyOnlineRequest(document=request_document, property_name='testProp')
words_api.delete_document_property_online(delete_request)