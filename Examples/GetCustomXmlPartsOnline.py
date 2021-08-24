words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetCustomXmlPartsOnlineRequest(document=request_document)
words_api.get_custom_xml_parts_online(request)