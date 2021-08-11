words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
optimize_request = asposewordscloud.models.requests.OptimizeDocumentRequest(name = 'Sample.docx',options = request_options)
words_api.optimize_document(optimize_request)