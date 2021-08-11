words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetParagraphsRequest(name = 'Sample.docx')
words_api.get_paragraphs(request)