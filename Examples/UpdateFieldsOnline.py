words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
update_request = asposewordscloud.models.requests.UpdateFieldsOnlineRequest(document=request_document)
words_api.update_fields_online(update_request)