words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
remote_file_name= 'Sample.docx'

delete_request = asposewordscloud.models.requests.DeleteCustomXmlPartRequest(name = remote_file_name,custom_xml_part_index = 0,dest_file_name = remote_file_name)
words_api.delete_custom_xml_part(delete_request)