words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetDocumentStatisticsOnlineRequest(document=request_document)
words_api.get_document_statistics_online(request)