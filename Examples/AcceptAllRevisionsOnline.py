words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
file_name = 'test_doc.docx'

# Calls AcceptAllRevisionsOnline method for document in cloud.
request_document = open(file_name, 'rb')
request = asposewordscloud.models.requests.AcceptAllRevisionsOnlineRequest(document=request_document)
accept_all_revisions_online_result = words_api.accept_all_revisions_online(request)
copyfile(accept_all_revisions_online_result.document, 'test_result.docx')