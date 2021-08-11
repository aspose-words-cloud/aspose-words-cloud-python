documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateRunFontOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),paragraph_path = 'paragraphs/0',font_dto = request_font_dto,index = 0)
words_api.update_run_font_online(update_request)