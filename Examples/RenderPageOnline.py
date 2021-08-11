documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
render_request = asposewordscloud.models.requests.RenderPageOnlineRequest(document = open(os.path.join(documents_dir, 'DocumentElements/Text/SampleWordDocument.docx'), 'rb'),page_index = 1,format = 'bmp')
words_api.render_page_online(render_request)