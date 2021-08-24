words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetParagraphTabStopsRequest(name='Sample.docx', index=0)
words_api.get_paragraph_tab_stops(request)