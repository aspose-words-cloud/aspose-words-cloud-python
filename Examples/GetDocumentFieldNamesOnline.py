documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetDocumentFieldNamesOnlineRequest(template = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),use_non_merge_fields = True)
words_api.get_document_field_names_online(request)