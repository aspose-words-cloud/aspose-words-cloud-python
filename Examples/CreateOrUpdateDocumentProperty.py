words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_property = asposewordscloud.DocumentPropertyCreateOrUpdate(value='Imran Anwar')
create_request = asposewordscloud.models.requests.CreateOrUpdateDocumentPropertyRequest(name='Sample.docx', property_name='AsposeAuthor', _property=request_property)
words_api.create_or_update_document_property(create_request)