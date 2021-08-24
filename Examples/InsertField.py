words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_field = asposewordscloud.FieldInsert(field_code='{ NUMPAGES }')
insert_request = asposewordscloud.models.requests.InsertFieldRequest(name='Sample.docx', field=request_field)
words_api.insert_field(insert_request)