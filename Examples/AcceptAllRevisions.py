import os
import asposewordscloud
import asposewordscloud.models.requests
from asposewordscloud.rest import ApiException
from shutil import copyfile

documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
file_name = 'test_doc.docx'

# Upload original document to cloud storage.
upload_file_request = asposewordscloud.models.requests.UploadFileRequest(file_content = open(os.path.join(documents_dir, file_name), 'rb'),path = file_name)
words_api.upload_file(upload_file_request)

# Calls AcceptAllRevisions method for document in cloud.
request = asposewordscloud.models.requests.AcceptAllRevisionsRequest(name = file_name)
words_api.accept_all_revisions(request)