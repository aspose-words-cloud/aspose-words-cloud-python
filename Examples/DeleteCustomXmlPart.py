words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteCustomXmlPartRequest(name = 'Sample.docx',custom_xml_part_index = 0)
words_api.delete_custom_xml_part(delete_request)