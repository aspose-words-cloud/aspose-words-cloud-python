documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetDocumentHyperlinkByIndexOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),hyperlink_index = 0)
words_api.get_document_hyperlink_by_index_online(request)