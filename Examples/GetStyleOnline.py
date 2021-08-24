words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetStyleOnlineRequest(document=request_document, style_name='Heading 1')
words_api.get_style_online(request)