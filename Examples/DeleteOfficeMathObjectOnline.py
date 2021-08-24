words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
delete_request = asposewordscloud.models.requests.DeleteOfficeMathObjectOnlineRequest(document=request_document, index=0)
words_api.delete_office_math_object_online(delete_request)