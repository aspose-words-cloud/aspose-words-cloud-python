words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
search_request = asposewordscloud.models.requests.SearchRequest(name = 'Sample.docx',pattern = 'aspose')
words_api.search(search_request)