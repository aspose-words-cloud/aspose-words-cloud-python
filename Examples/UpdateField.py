words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_field = asposewordscloud.FieldUpdate(field_code='{ NUMPAGES }')
update_request = asposewordscloud.models.requests.UpdateFieldRequest(name='Sample.docx', index=0, field=request_field, node_path='sections/0/paragraphs/0')
words_api.update_field(update_request)