documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertOrUpdateParagraphTabStopOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),tab_stop_insert_dto = request_tab_stop_insert_dto,index = 0)
words_api.insert_or_update_paragraph_tab_stop_online(insert_request)