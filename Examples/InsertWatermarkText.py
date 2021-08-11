words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
remote_file_name= 'Sample.docx'

insert_request = asposewordscloud.models.requests.InsertWatermarkTextRequest(name = remote_file_name,watermark_text = request_watermark_text,dest_file_name = remote_file_name)
words_api.insert_watermark_text(insert_request)