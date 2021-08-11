words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteMacrosRequest(name = 'Sample.docx')
words_api.delete_macros(delete_request)