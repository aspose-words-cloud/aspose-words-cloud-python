documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteOfficeMathObjectOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),index = 0)
words_api.delete_office_math_object_online(delete_request)