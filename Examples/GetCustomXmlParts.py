words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetCustomXmlPartsRequest(name='Sample.docx')
words_api.get_custom_xml_parts(request)