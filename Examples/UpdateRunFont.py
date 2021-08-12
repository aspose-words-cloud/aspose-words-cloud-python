words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateRunFontRequest(name = 'Sample.docx',paragraph_path = 'paragraphs/0',index = 0,font_dto = request_font_dto)
words_api.update_run_font(update_request)