documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetOfficeMathObjectsOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'))
words_api.get_office_math_objects_online(request)