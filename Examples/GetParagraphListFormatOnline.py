words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.doc', 'rb')
request = asposewordscloud.models.requests.GetParagraphListFormatOnlineRequest(document=request_document, index=0)
words_api.get_paragraph_list_format_online(request)