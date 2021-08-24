words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_report_engine_settings_report_build_options = ['AllowMissingMembers', 'RemoveEmptyParagraphs']
request_report_engine_settings = asposewordscloud.ReportEngineSettings(data_source_type='Json', report_build_options=request_report_engine_settings_report_build_options)
build_report_request = asposewordscloud.models.requests.BuildReportRequest(name='Sample.docx', data='Data.json', report_engine_settings=request_report_engine_settings)
words_api.build_report(build_report_request)