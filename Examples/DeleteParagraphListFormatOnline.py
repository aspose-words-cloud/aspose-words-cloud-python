words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.doc', 'rb')
delete_request = asposewordscloud.models.requests.DeleteParagraphListFormatOnlineRequest(document=request_document, index=0)
words_api.delete_paragraph_list_format_online(delete_request)