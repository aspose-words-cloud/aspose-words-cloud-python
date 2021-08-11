documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
save_request = asposewordscloud.models.requests.SaveAsTiffOnlineRequest(document = open(os.path.join(documents_dir, 'Common/test_multi_pages.docx'), 'rb'),save_options = request_save_options)
words_api.save_as_tiff_online(save_request)