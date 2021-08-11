words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteSectionRequest(name = 'Sample.docx',section_index = 0)
words_api.delete_section(delete_request)