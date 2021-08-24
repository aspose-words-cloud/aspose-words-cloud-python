words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteWatermarkRequest(name='Sample.docx')
words_api.delete_watermark(delete_request)