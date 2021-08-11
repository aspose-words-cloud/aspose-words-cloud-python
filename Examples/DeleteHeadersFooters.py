words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteHeadersFootersRequest(name = 'Sample.docx',section_path = '')
words_api.delete_headers_footers(delete_request)