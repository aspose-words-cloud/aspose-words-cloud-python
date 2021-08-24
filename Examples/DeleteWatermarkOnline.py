words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
delete_request = asposewordscloud.models.requests.DeleteWatermarkOnlineRequest(document=request_document)
words_api.delete_watermark_online(delete_request)