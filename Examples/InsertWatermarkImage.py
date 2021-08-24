words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertWatermarkImageRequest(name='Sample.docx', image_file=None, image='Sample.png')
words_api.insert_watermark_image(insert_request)