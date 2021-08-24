words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteFootnoteRequest(name='Sample.docx', index=0)
words_api.delete_footnote(delete_request)