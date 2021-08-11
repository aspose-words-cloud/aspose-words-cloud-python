words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertCustomXmlPartRequest(name = 'Sample.docx',custom_xml_part = request_custom_xml_part)
words_api.insert_custom_xml_part(insert_request)