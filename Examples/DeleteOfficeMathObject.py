words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteOfficeMathObjectRequest(name = 'Sample.docx',index = 0)
words_api.delete_office_math_object(delete_request)