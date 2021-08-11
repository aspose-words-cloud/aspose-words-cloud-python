documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateCustomXmlPartOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),custom_xml_part_index = 0,custom_xml_part = request_custom_xml_part)
words_api.update_custom_xml_part_online(update_request)