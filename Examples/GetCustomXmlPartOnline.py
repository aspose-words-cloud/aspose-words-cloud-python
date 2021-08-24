words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetCustomXmlPartOnlineRequest(document=request_document, custom_xml_part_index=0)
words_api.get_custom_xml_part_online(request)