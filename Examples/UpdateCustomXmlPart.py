words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_custom_xml_part = asposewordscloud.CustomXmlPartUpdate(data='<data>Hello world</data>')
update_request = asposewordscloud.models.requests.UpdateCustomXmlPartRequest(name='Sample.docx', custom_xml_part_index=0, custom_xml_part=request_custom_xml_part)
words_api.update_custom_xml_part(update_request)