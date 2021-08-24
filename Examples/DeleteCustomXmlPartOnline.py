words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
delete_request = asposewordscloud.models.requests.DeleteCustomXmlPartOnlineRequest(document=request_document, custom_xml_part_index=0)
words_api.delete_custom_xml_part_online(delete_request)