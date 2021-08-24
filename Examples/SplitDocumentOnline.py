words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
split_request = asposewordscloud.models.requests.SplitDocumentOnlineRequest(document=request_document, format='text', dest_file_name='/TestSplitDocument.text', _from=1, to=2)
words_api.split_document_online(split_request)