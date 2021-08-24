words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
render_request = asposewordscloud.models.requests.RenderTableOnlineRequest(document=request_document, format='png', index=0)
words_api.render_table_online(render_request)