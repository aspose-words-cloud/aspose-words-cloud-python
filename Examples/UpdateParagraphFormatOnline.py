documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateParagraphFormatOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),paragraph_format_dto = request_paragraph_format_dto,index = 0,node_path = '')
words_api.update_paragraph_format_online(update_request)