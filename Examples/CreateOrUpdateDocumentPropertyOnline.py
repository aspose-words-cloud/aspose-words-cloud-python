documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
create_request = asposewordscloud.models.requests.CreateOrUpdateDocumentPropertyOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),property_name = 'AsposeAuthor',_property = request_property)
words_api.create_or_update_document_property_online(create_request)