documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetParagraphsOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),node_path = 'sections/0')
words_api.get_paragraphs_online(request)