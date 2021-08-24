words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetDocumentHyperlinkByIndexOnlineRequest(document=request_document, hyperlink_index=0)
words_api.get_document_hyperlink_by_index_online(request)