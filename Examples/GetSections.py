words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetSectionsRequest(name='Sample.docx')
words_api.get_sections(request)