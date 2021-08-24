words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request_form_field = asposewordscloud.FormFieldTextInput(name='FullName', enabled=True, calculate_on_exit=True, status_text='', text_input_type='Regular', text_input_default='123', text_input_format='UPPERCASE')
insert_request = asposewordscloud.models.requests.InsertFormFieldRequest(name='Sample.docx', form_field=request_form_field)
words_api.insert_form_field(insert_request)