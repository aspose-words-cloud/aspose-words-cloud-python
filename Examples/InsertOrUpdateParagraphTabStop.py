words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertOrUpdateParagraphTabStopRequest(name = 'Sample.docx',index = 0,tab_stop_insert_dto = request_tab_stop_insert_dto)
words_api.insert_or_update_paragraph_tab_stop(insert_request)