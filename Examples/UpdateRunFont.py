words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
remote_file_name= 'Sample.docx'

update_request = asposewordscloud.models.requests.UpdateRunFontRequest(name = remote_file_name,paragraph_path = 'paragraphs/0',index = 0,font_dto = request_font_dto,dest_file_name = remote_file_name)
words_api.update_run_font(update_request)