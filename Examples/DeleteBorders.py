words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteBordersRequest(name = 'Sample.docx',node_path = 'tables/1/rows/0/cells/0')
words_api.delete_borders(delete_request)