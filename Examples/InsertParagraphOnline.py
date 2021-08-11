documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertParagraphOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),paragraph = request_paragraph,node_path = 'sections/0')
words_api.insert_paragraph_online(insert_request)