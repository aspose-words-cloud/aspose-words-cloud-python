words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteHeaderFooterRequest(name = 'Sample.docx',section_path = '',index = 0)
words_api.delete_header_footer(delete_request)