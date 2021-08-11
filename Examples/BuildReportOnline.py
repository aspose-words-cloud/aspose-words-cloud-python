documents_dir = '...'
words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
build_report_request = asposewordscloud.models.requests.BuildReportOnlineRequest(template = open(os.path.join(documents_dir, 'Sample.docx'), 'rb'),data = 'Data.json',report_engine_settings = request_report_engine_settings)
words_api.build_report_online(build_report_request)