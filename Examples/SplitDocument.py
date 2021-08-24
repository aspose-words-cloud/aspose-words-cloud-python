words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
split_request = asposewordscloud.models.requests.SplitDocumentRequest(name='Sample.docx', format='text', dest_file_name='/TestSplitDocument.text', _from=1, to=2)
words_api.split_document(split_request)