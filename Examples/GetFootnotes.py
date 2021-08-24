words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetFootnotesRequest(name='Sample.docx')
words_api.get_footnotes(request)