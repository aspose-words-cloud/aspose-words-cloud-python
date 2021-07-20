words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
remote_file_name= 'Sample.docx'
bookmark_name= 'aspose'

update_bookmark = asposewordscloud.models.requests.UpdateBookmarkRequest(name = remote_file_name,bookmark_name = bookmark_name,bookmark_data = test_bookmark_data)
words_api.update_bookmark(update_bookmark)