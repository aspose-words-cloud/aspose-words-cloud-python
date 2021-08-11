words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteParagraphListFormatRequest(name = 'Sample.docx',index = 0)
words_api.delete_paragraph_list_format(delete_request)