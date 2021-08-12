documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
convert_request = asposewordscloud.models.requests.ConvertDocumentRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),format = 'pdf')
words_api.convert_document(convert_request)