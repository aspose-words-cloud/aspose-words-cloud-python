words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetDocumentPropertyOnlineRequest(document=request_document, property_name='Author')
words_api.get_document_property_online(request)