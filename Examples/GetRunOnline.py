words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetRunOnlineRequest(document=request_document, paragraph_path='paragraphs/0', index=0)
words_api.get_run_online(request)