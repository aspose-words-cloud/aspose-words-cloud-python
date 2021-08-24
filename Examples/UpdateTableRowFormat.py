words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_format = asposewordscloud.TableRowFormat(allow_break_across_pages=True, heading_format=True, height=10.0, height_rule='Exactly')
update_request = asposewordscloud.models.requests.UpdateTableRowFormatRequest(name='Sample.docx', table_path='sections/0/tables/2', index=0, format=request_format)
words_api.update_table_row_format(update_request)