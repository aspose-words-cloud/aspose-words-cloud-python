words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
delete_request = asposewordscloud.models.requests.DeleteAllParagraphTabStopsOnlineRequest(document=request_document, index=0)
words_api.delete_all_paragraph_tab_stops_online(delete_request)