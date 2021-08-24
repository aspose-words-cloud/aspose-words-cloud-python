words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetStyleRequest(name='Sample.docx', style_name='Heading 1')
words_api.get_style(request)