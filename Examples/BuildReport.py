words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
build_report_request = asposewordscloud.models.requests.BuildReportRequest(name = 'Sample.docx',data = 'Data.json',report_engine_settings = request_report_engine_settings)
words_api.build_report(build_report_request)