words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetStylesRequest(name='Sample.docx')
words_api.get_styles(request)