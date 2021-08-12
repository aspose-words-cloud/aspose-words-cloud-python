documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetOfficeMathObjectOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),index = 0)
words_api.get_office_math_object_online(request)