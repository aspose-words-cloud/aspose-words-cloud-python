words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetFieldsOnlineRequest(document=request_document, node_path='sections/0')
words_api.get_fields_online(request)