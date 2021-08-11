words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetOfficeMathObjectRequest(name = 'Sample.docx',index = 0)
words_api.get_office_math_object(request)