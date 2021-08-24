words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteCustomXmlPartsRequest(name='Sample.docx')
words_api.delete_custom_xml_parts(delete_request)