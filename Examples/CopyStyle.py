words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_style_copy = asposewordscloud.StyleCopy(style_name='Heading 1')
copy_request = asposewordscloud.models.requests.CopyStyleRequest(name='Sample.docx', style_copy=request_style_copy)
words_api.copy_style(copy_request)