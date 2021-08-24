words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_save_options_data = asposewordscloud.SaveOptionsData(save_format='docx', file_name='/TestSaveAsFromPdfToDoc.docx')
save_request = asposewordscloud.models.requests.SaveAsRequest(name='Sample.docx', save_options_data=request_save_options_data)
words_api.save_as(save_request)