documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertFootnoteOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.doc'), 'rb'),footnote_dto = request_footnote_dto)
words_api.insert_footnote_online(insert_request)