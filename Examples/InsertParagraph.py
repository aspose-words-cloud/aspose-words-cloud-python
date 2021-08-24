words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_paragraph = asposewordscloud.ParagraphInsert(text='This is a new paragraph for your document')
insert_request = asposewordscloud.models.requests.InsertParagraphRequest(name='Sample.docx', paragraph=request_paragraph)
words_api.insert_paragraph(insert_request)