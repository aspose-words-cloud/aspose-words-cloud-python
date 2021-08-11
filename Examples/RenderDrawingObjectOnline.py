documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
render_request = asposewordscloud.models.requests.RenderDrawingObjectOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),format = 'png',index = 0,node_path = 'sections/0')
words_api.render_drawing_object_online(render_request)