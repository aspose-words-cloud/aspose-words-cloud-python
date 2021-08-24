words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_template = open('Sample.docx', 'rb')
request = asposewordscloud.models.requests.GetDocumentFieldNamesOnlineRequest(template=request_template, use_non_merge_fields=True)
words_api.get_document_field_names_online(request)