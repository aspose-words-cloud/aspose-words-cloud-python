documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
save_request = asposewordscloud.models.requests.SaveAsOnlineRequest(document = open(os.path.join(documents_dir, 'Common/test_multi_pages.docx'), 'rb'),save_options_data = request_save_options_data)
words_api.save_as_online(save_request)