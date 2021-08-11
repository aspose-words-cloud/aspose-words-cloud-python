words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertParagraphRequest(name = 'Sample.docx',paragraph = request_paragraph)
words_api.insert_paragraph(insert_request)