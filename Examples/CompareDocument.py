words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_compare_data = asposewordscloud.CompareData(author='author', comparing_with_document='TestCompareDocument2.doc', date_time=dateutil.parser.isoparse('2015-10-26T00:00:00.0000000Z'))
compare_request = asposewordscloud.models.requests.CompareDocumentRequest(name='TestCompareDocument1.doc', compare_data=request_compare_data, dest_file_name='/TestCompareDocumentOut.doc')
words_api.compare_document(compare_request)