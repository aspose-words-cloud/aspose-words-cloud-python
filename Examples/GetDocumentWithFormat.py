words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetDocumentWithFormatRequest(name='Sample.docx', format='text', out_path='/TestGetDocumentWithFormatAndOutPath.text')
words_api.get_document_with_format(request)