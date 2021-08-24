words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
classify_request = asposewordscloud.models.requests.ClassifyRequest(text='Try text classification', best_classes_count='3')
words_api.classify(classify_request)