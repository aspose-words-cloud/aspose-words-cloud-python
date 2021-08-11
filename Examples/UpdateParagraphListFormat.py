words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateParagraphListFormatRequest(name = 'Sample.docx',index = 0,list_format_dto = request_list_format_dto)
words_api.update_paragraph_list_format(update_request)