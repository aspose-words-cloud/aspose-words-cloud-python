documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
render_request = asposewordscloud.models.requests.RenderTableOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),format = 'png',index = 0)
words_api.render_table_online(render_request)