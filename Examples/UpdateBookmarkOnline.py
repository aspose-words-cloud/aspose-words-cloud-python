words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
bookmark_name= 'aspose'

request_document = open('Sample.docx', 'rb')
request_bookmark_data = asposewordscloud.BookmarkData(name=bookmark_name, text='This will be the text for Aspose')
update_request = asposewordscloud.models.requests.UpdateBookmarkOnlineRequest(document=request_document, bookmark_name=bookmark_name, bookmark_data=request_bookmark_data, dest_file_name='Sample.docx')
words_api.update_bookmark_online(update_request)