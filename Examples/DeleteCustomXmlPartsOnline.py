words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
delete_request = asposewordscloud.models.requests.DeleteCustomXmlPartsOnlineRequest(document=request_document)
words_api.delete_custom_xml_parts_online(delete_request)