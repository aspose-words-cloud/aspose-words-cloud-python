words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_properties = asposewordscloud.TableProperties(alignment='Right', allow_auto_fit=False, bidi=True, bottom_padding=1.0, cell_spacing=2.0, style_options='ColumnBands')
update_request = asposewordscloud.models.requests.UpdateTablePropertiesRequest(name='Sample.docx', index=1, properties=request_properties)
words_api.update_table_properties(update_request)