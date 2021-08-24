words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_options = asposewordscloud.OptimizationOptions(ms_word_version='Word2002')
optimize_request = asposewordscloud.models.requests.OptimizeDocumentRequest(name='Sample.docx', options=request_options)
words_api.optimize_document(optimize_request)