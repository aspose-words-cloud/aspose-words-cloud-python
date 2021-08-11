words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
render_request = asposewordscloud.models.requests.RenderDrawingObjectRequest(name = 'Sample.docx',format = 'png',index = 0)
words_api.render_drawing_object(render_request)