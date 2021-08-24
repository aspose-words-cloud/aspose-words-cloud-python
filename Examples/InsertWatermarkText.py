words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_watermark_text = asposewordscloud.WatermarkText(text='This is the text', rotation_angle=90.0)
insert_request = asposewordscloud.models.requests.InsertWatermarkTextRequest(name='Sample.docx', watermark_text=request_watermark_text)
words_api.insert_watermark_text(insert_request)