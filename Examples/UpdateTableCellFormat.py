words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_format = asposewordscloud.TableCellFormat(bottom_padding=5.0, fit_text=True, horizontal_merge='First', wrap_text=True)
update_request = asposewordscloud.models.requests.UpdateTableCellFormatRequest(name='Sample.docx', table_row_path='sections/0/tables/2/rows/0', index=0, format=request_format)
words_api.update_table_cell_format(update_request)