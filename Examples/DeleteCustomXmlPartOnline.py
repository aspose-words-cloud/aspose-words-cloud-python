documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteCustomXmlPartOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),custom_xml_part_index = 0)
words_api.delete_custom_xml_part_online(delete_request)