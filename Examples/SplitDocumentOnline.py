documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
split_request = asposewordscloud.models.requests.SplitDocumentOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),format = 'text',dest_file_name = '/TestSplitDocument.text',_from = 1,to = 2)
words_api.split_document_online(split_request)