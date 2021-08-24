words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetCustomXmlPartRequest(name='Sample.docx', custom_xml_part_index=0)
words_api.get_custom_xml_part(request)