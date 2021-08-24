words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteBorderRequest(name='Sample.docx', border_type='left', node_path='tables/1/rows/0/cells/0')
words_api.delete_border(delete_request)