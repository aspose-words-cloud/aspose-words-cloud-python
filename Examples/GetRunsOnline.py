words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetRunsOnlineRequest(document=request_document, paragraph_path='sections/0/paragraphs/0')
words_api.get_runs_online(request)