words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertFootnoteRequest(name = 'Sample.docx',footnote_dto = request_footnote_dto)
words_api.insert_footnote(insert_request)