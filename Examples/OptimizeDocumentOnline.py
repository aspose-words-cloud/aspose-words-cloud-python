documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
optimize_request = asposewordscloud.models.requests.OptimizeDocumentOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),options = request_options)
words_api.optimize_document_online(optimize_request)