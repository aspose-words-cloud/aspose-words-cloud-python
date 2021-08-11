documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
render_request = asposewordscloud.models.requests.RenderParagraphOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),format = 'png',index = 0,node_path = '')
words_api.render_paragraph_online(render_request)