words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetOfficeMathObjectOnlineRequest(document=request_document, index=0)
words_api.get_office_math_object_online(request)