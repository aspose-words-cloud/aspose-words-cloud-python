documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteParagraphListFormatOnlineRequest(document = open(os.path.join(documents_dir, '/ParagraphDeleteListFormat.doc'), 'rb'),index = 0,node_path = '')
words_api.delete_paragraph_list_format_online(delete_request)