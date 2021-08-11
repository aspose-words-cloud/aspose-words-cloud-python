words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
request = asposewordscloud.models.requests.GetAvailableFontsRequest()
words_api.get_available_fonts(request)