words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
remote_file_name= 'Sample.docx'

append_request = asposewordscloud.models.requests.AppendDocumentRequest(name = remote_file_name,document_list = request_document_list,dest_file_name = remote_file_name)
words_api.append_document(append_request)