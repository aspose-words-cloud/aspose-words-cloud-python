documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
insert_request = asposewordscloud.models.requests.InsertPageNumbersOnlineRequest(document = open(os.path.join(documents_dir, 'Common/Sample.docx'), 'rb'),page_number = request_page_number)
words_api.insert_page_numbers_online(insert_request)