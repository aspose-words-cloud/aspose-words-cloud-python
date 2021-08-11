documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
remote_file_name= 'Sample.docx'

insert_request = asposewordscloud.models.requests.InsertWatermarkImageRequest(name = remote_file_name,image_file = None,dest_file_name = remote_file_name,image = 'Sample.png')
words_api.insert_watermark_image(insert_request)