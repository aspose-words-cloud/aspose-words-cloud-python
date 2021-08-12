documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteAllParagraphTabStopsOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),index = 0)
words_api.delete_all_paragraph_tab_stops_online(delete_request)