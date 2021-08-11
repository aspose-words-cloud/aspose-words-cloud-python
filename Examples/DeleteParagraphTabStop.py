words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
delete_request = asposewordscloud.models.requests.DeleteParagraphTabStopRequest(name = 'Sample.docx',position = 72.0,index = 0)
words_api.delete_paragraph_tab_stop(delete_request)