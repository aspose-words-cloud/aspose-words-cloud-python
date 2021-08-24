words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
classify_request = asposewordscloud.models.requests.ClassifyDocumentOnlineRequest(document=request_document, best_classes_count='3')
words_api.classify_document_online(classify_request)