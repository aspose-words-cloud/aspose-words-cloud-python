words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
delete_request = asposewordscloud.models.requests.DeleteParagraphTabStopOnlineRequest(document=request_document, position=72.0, index=0)
words_api.delete_paragraph_tab_stop_online(delete_request)