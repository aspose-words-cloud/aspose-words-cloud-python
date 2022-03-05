words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
file_name= 'test_doc.docx'

# Calls AcceptAllRevisionsOnline method for document in cloud.
request_document = open(file_name, 'rb')
request = asposewordscloud.models.requests.AcceptAllRevisionsOnlineRequest(document=request_document)
accept_all_revisions_online_result = words_api.accept_all_revisions_online(request)
open('test_result.docx','wb').write(list(accept_all_revisions_online_result.document.values())[0])