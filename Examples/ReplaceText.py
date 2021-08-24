words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_replace_text = asposewordscloud.ReplaceTextParameters(old_value='Testing', new_value='Aspose testing')
replace_request = asposewordscloud.models.requests.ReplaceTextRequest(name='Sample.docx', replace_text=request_replace_text)
words_api.replace_text(replace_request)