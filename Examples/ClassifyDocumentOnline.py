documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
classify_request = asposewordscloud.models.requests.ClassifyDocumentOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),best_classes_count = '3')
words_api.classify_document_online(classify_request)