documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetParagraphTabStopsOnlineRequest(document = open(os.path.join(documents_dir, '/ParagraphTabStops.docx'), 'rb'),index = 0,node_path = '')
words_api.get_paragraph_tab_stops_online(request)