words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetOfficeMathObjectsRequest(name='Sample.docx')
words_api.get_office_math_objects(request)