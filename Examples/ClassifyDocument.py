words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
classify_request = asposewordscloud.models.requests.ClassifyDocumentRequest(name = 'Sample.docx',best_classes_count = '3')
words_api.classify_document(classify_request)