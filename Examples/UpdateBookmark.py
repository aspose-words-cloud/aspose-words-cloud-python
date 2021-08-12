words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
bookmark_name= 'aspose'

update_request = asposewordscloud.models.requests.UpdateBookmarkRequest(name = 'Sample.docx',bookmark_name = bookmark_name,bookmark_data = request_bookmark_data)
words_api.update_bookmark(update_request)