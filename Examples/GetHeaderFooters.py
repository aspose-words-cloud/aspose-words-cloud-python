words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetHeaderFootersRequest(name = 'Sample.docx',section_path = '')
words_api.get_header_footers(request)