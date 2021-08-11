documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
apply_style_request = asposewordscloud.models.requests.ApplyStyleToDocumentElementOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),styled_node_path = 'paragraphs/1/paragraphFormat',style_apply = request_style_apply)
words_api.apply_style_to_document_element_online(apply_style_request)