import os
import asposewordscloud
import asposewordscloud.models.requests
from asposewordscloud.rest import ApiException
from shutil import copyfile

words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
file_name= 'test_doc.docx'

# Upload original document to cloud storage.
my_var1 = open(file_name, 'rb')
my_var2 = file_name
upload_file_request = asposewordscloud.models.requests.UploadFileRequest(file_content=my_var1, path=my_var2)
words_api.upload_file(upload_file_request)

# Calls AcceptAllRevisions method for document in cloud.
my_var3 = file_name
request = asposewordscloud.models.requests.AcceptAllRevisionsRequest(name=my_var3)
words_api.accept_all_revisions(request)