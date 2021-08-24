words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
convert_request = asposewordscloud.models.requests.ConvertDocumentRequest(document=request_document, format='pdf')
words_api.convert_document(convert_request)