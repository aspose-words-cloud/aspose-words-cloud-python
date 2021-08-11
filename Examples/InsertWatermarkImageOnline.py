documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertWatermarkImageOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),image_file = open(os.path.join(documents_dir, 'Common/aspose-cloud.png'), 'rb'))
words_api.insert_watermark_image_online(insert_request)