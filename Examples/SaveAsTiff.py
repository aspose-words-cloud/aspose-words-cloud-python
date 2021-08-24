words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_save_options = asposewordscloud.TiffSaveOptionsData(save_format='tiff', file_name='/abc.tiff')
save_request = asposewordscloud.models.requests.SaveAsTiffRequest(name='Sample.docx', save_options=request_save_options)
words_api.save_as_tiff(save_request)