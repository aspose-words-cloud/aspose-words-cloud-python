words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetParagraphTabStopsOnlineRequest(document=request_document, index=0)
words_api.get_paragraph_tab_stops_online(request)