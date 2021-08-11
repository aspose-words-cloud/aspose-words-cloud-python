documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetCustomXmlPartOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),custom_xml_part_index = 0)
words_api.get_custom_xml_part_online(request)