words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
render_request = asposewordscloud.models.requests.RenderPageRequest(name = 'Sample.docx',page_index = 1,format = 'bmp')
words_api.render_page(render_request)