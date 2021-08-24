words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetBordersRequest(name='Sample.docx', node_path='tables/1/rows/0/cells/0')
words_api.get_borders(request)