documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertWatermarkTextOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),watermark_text = request_watermark_text)
words_api.insert_watermark_text_online(insert_request)