documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
compare_request = asposewordscloud.models.requests.CompareDocumentOnlineRequest(document = open(os.path.join(documents_dir, 'compareTestDoc1.doc'), 'rb'),compare_data = request_compare_data,comparing_document = open(os.path.join(documents_dir, 'compareTestDoc2.doc'), 'rb'),dest_file_name = '/TestCompareDocumentOut.doc')
words_api.compare_document_online(compare_request)