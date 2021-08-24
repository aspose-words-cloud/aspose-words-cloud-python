words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
render_request = asposewordscloud.models.requests.RenderPageOnlineRequest(document=request_document, page_index=1, format='bmp')
words_api.render_page_online(render_request)