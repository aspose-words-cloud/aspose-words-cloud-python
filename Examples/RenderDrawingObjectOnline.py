words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
render_request = asposewordscloud.models.requests.RenderDrawingObjectOnlineRequest(document=request_document, format='png', index=0, node_path='sections/0')
words_api.render_drawing_object_online(render_request)