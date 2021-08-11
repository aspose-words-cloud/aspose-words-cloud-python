words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
compare_request = asposewordscloud.models.requests.CompareDocumentRequest(name = 'TestCompareDocument1.doc',compare_data = request_compare_data,dest_file_name = '/TestCompareDocumentOut.doc')
words_api.compare_document(compare_request)