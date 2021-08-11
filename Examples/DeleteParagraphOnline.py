documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteParagraphOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),index = 0,node_path = '')
words_api.delete_paragraph_online(delete_request)