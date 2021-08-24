words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetRunFontOnlineRequest(document=request_document, paragraph_path='paragraphs/0', index=0)
words_api.get_run_font_online(request)