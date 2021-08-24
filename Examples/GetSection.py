words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetSectionRequest(name='Sample.docx', section_index=0)
words_api.get_section(request)