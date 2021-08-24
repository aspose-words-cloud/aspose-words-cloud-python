words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_style_insert = asposewordscloud.StyleInsert(style_name='My Style', style_type='Paragraph')
insert_request = asposewordscloud.models.requests.InsertStyleRequest(name='Sample.docx', style_insert=request_style_insert)
words_api.insert_style(insert_request)