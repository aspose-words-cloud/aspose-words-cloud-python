documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateParagraphListFormatOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb'),list_format_dto = request_list_format_dto,index = 0)
words_api.update_paragraph_list_format_online(update_request)