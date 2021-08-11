documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteSectionOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),section_index = 0)
words_api.delete_section_online(delete_request)