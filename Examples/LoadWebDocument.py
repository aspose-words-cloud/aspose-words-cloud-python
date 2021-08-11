words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
load_request = asposewordscloud.models.requests.LoadWebDocumentRequest(data = request_data)
words_api.load_web_document(load_request)