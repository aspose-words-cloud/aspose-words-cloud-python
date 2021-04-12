documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
file_name = 'test_doc.docx'

# Calls AcceptAllRevisionsOnline method for document in cloud.
request = asposewordscloud.models.requests.AcceptAllRevisionsOnlineRequest(document = open(os.path.join(documents_dir, file_name), 'rb'))
accept_all_revisions_online_result = words_api.accept_all_revisions_online(request)
copyfile(accept_all_revisions_online_result.document, 'test_result.docx')