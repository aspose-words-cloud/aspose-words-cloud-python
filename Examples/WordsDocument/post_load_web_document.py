import os
import asposestoragecloud
import asposewordscloud
import asposewordscloud.models.requests

class Table(object):

	def __init__(self):
		api_client = asposewordscloud.ApiClient()
		api_client.configuration.host = 'https://api.aspose.cloud'
		api_client.configuration.api_key['api_key'] = 'xxxx' # Put your appkey here
		api_client.configuration.api_key['app_sid'] = 'xxxx-xxxx-xxxx-xxxx-xxxx' # Put your appSid here

		# Same credentials for storage
		self.storage_api = asposestoragecloud.StorageApi(asposestoragecloud.ApiClient(apiKey='xxxx', appSid='xxxx-xxxx-xxxx-xxxx-xxxx')) # Same credentials for storage
		self.storage_api.api_client.configuration.base_url = 'https://api.aspose.cloud' + '/v1.1'
		self.words_api = asposewordscloud.WordsApi(api_client)

		ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../..")
		self.dataFolder = os.path.join(ABSPATH, "TestData/Common")

	def post_load_web_document(self):
		save_options = asposewordscloud.SaveOptionsData('1', 'doc', 'google.doc', '1', '1', False, False)
        body = asposewordscloud.LoadWebDocumentData('http://google.com', save_options)
        request = asposewordscloud.models.requests.PostLoadWebDocumentRequest(body)
		result = self.words_api.post_load_web_document(request)
		print("Result {}".format(result))

table = Table()
table.post_load_web_document()
