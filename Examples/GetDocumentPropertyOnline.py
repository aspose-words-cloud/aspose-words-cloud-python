documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetDocumentPropertyOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),property_name = 'Author')
words_api.get_document_property_online(request)