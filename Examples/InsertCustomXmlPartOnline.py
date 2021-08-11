documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertCustomXmlPartOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),custom_xml_part = request_custom_xml_part)
words_api.insert_custom_xml_part_online(insert_request)