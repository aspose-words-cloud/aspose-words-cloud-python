words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateFootnoteRequest(name = 'Sample.docx',index = 0,footnote_dto = request_footnote_dto)
words_api.update_footnote(update_request)