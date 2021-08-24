words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetRunsRequest(name='Sample.docx', paragraph_path='sections/0/paragraphs/0')
words_api.get_runs(request)