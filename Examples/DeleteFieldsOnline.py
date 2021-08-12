documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteFieldsOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'))
words_api.delete_fields_online(delete_request)