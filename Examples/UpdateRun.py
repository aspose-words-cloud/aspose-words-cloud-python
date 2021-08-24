words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_run = asposewordscloud.RunUpdate(text='run with text')
update_request = asposewordscloud.models.requests.UpdateRunRequest(name='Sample.docx', paragraph_path='paragraphs/1', index=0, run=request_run)
words_api.update_run(update_request)