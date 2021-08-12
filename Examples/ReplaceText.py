words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
replace_request = asposewordscloud.models.requests.ReplaceTextRequest(name = 'Sample.docx',replace_text = request_replace_text)
words_api.replace_text(replace_request)