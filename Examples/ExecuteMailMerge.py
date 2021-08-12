words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
mail_merge_request = asposewordscloud.models.requests.ExecuteMailMergeRequest(name = 'Sample.docx',data = 'TestExecuteTemplateData.txt')
words_api.execute_mail_merge(mail_merge_request)