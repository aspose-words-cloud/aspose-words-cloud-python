documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetStyleFromDocumentElementOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),styled_node_path = 'paragraphs/1/paragraphFormat')
words_api.get_style_from_document_element_online(request)