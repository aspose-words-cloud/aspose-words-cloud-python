words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_page_number = asposewordscloud.PageNumber(alignment='center', format='{PAGE} of {NUMPAGES}')
insert_request = asposewordscloud.models.requests.InsertPageNumbersRequest(name='Sample.docx', page_number=request_page_number)
words_api.insert_page_numbers(insert_request)