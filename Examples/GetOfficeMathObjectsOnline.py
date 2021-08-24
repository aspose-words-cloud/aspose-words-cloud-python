words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetOfficeMathObjectsOnlineRequest(document=request_document)
words_api.get_office_math_objects_online(request)