words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################') 
reset_request = asposewordscloud.models.requests.ResetCacheRequest()
words_api.reset_cache(reset_request)