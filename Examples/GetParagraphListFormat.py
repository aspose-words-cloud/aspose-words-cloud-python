words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetParagraphListFormatRequest(name='Sample.docx', index=0)
words_api.get_paragraph_list_format(request)