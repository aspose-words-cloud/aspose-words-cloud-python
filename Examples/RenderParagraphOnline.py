words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
render_request = asposewordscloud.models.requests.RenderParagraphOnlineRequest(document=request_document, format='png', index=0)
words_api.render_paragraph_online(render_request)