words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
remote_file_name= 'Sample.docx'
bookmark_name= 'aspose'

update_bookmark = asposewordscloud.models.requests.UpdateBookmarkRequest(name = remote_file_name,bookmark_name = bookmark_name,bookmark_data = request_bookmark_data,dest_file_name = self.remote_test_out + '/' + remote_file_name)
words_api.update_bookmark(update_bookmark)