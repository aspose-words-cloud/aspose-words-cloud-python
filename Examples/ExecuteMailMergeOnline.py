documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
mail_merge_request = asposewordscloud.models.requests.ExecuteMailMergeOnlineRequest(template = open(os.path.join(documents_dir, 'TestExecuteTemplate.doc'), 'rb'),data = open(os.path.join(documents_dir, 'TestExecuteTemplateData.txt'), 'rb'))
words_api.execute_mail_merge_online(mail_merge_request)