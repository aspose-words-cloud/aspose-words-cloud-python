words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertWatermarkTextRequest(name = 'Sample.docx',watermark_text = request_watermark_text)
words_api.insert_watermark_text(insert_request)