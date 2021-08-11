words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateStyleRequest(name = 'Sample.docx',style_name = 'Heading 1',style_update = request_style_update)
words_api.update_style(update_request)