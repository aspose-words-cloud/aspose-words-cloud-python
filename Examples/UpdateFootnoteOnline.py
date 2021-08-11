documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
update_request = asposewordscloud.models.requests.UpdateFootnoteOnlineRequest(document = open(os.path.join(documents_dir, '/Footnote.doc'), 'rb'),footnote_dto = request_footnote_dto,index = 0,node_path = '')
words_api.update_footnote_online(update_request)