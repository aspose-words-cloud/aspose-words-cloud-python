words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
remote_file_name= 'Sample.docx'

mail_merge_request = asposewordscloud.models.requests.ExecuteMailMergeRequest(name = remote_file_name,data = 'TestExecuteTemplateData.txt',dest_file_name = remote_file_name)
words_api.execute_mail_merge(mail_merge_request)