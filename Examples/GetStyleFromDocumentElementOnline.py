words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_document = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetStyleFromDocumentElementOnlineRequest(document=request_document, styled_node_path='paragraphs/1/paragraphFormat')
words_api.get_style_from_document_element_online(request)