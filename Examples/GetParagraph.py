words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetParagraphRequest(name='Sample.docx', index=0)
words_api.get_paragraph(request)