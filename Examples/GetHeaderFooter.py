words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetHeaderFooterRequest(name = 'Sample.docx',header_footer_index = 0)
words_api.get_header_footer(request)