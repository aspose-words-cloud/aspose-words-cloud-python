words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateParagraphFormatRequest(name = 'Sample.docx',index = 0,paragraph_format_dto = request_paragraph_format_dto)
words_api.update_paragraph_format(update_request)