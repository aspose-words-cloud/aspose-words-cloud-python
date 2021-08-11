words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
apply_style_request = asposewordscloud.models.requests.ApplyStyleToDocumentElementRequest(name = 'Sample.docx',styled_node_path = 'paragraphs/1/paragraphFormat',style_apply = request_style_apply)
words_api.apply_style_to_document_element(apply_style_request)