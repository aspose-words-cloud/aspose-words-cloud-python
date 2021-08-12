words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
bookmark_name= 'aspose'
remote_file_name= 'Sample.docx'

update_request = asposewordscloud.models.requests.UpdateBookmarkRequest(name = remote_file_name,bookmark_name = bookmark_name,bookmark_data = request_bookmark_data,dest_file_name = remote_file_name)
words_api.update_bookmark(update_request)