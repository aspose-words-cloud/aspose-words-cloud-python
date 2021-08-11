documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
protect_request = asposewordscloud.models.requests.ProtectDocumentOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),protection_request = request_protection_request)
words_api.protect_document_online(protect_request)