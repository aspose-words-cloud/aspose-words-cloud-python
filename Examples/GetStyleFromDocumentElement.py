words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetStyleFromDocumentElementRequest(name = 'Sample.docx',styled_node_path = 'paragraphs/1/paragraphFormat')
words_api.get_style_from_document_element(request)