documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
bookmark_name= 'aspose'

update_request = asposewordscloud.models.requests.UpdateBookmarkOnlineRequest(document = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),bookmark_name = bookmark_name,bookmark_data = request_bookmark_data,dest_file_name = 'Sample.docx')
words_api.update_bookmark_online(update_request)