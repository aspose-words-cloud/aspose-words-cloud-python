words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteAllParagraphTabStopsRequest(name='Sample.docx', index=0)
words_api.delete_all_paragraph_tab_stops(delete_request)