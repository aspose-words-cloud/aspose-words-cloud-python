words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
render_request = asposewordscloud.models.requests.RenderMathObjectRequest(name='Sample.docx', format='png', index=0)
words_api.render_math_object(render_request)