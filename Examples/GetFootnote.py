words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetFootnoteRequest(name='Sample.docx', index=0)
words_api.get_footnote(request)