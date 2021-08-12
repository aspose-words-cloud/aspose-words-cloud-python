documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteParagraphTabStopOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),position = 72.0,index = 0)
words_api.delete_paragraph_tab_stop_online(delete_request)