import os
import datetime
import asposestoragecloud
import asposewordscloud
import asposewordscloud.models.requests

class Document(object):

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
		self.dataFolder = os.path.join(ABSPATH, "TestData/DocumentActions/CompareDocument")

	def compare_document_with_original_document(self):
		local_name1 = "compareTestDoc1.doc"
		local_name2 = "compareTestDoc2.doc"
		dest_name = 'CompareOut.doc'
		
		# Upload documents to Cloud Storage
		for filename in [local_name1, local_name2]:
			filePath = os.path.join(self.dataFolder, filename)
			with open(filePath, 'rb') as f:
				fileData = f.read()
			file_upload_response = self.storage_api.put_create(filename, fileData)
		
		compare_data = asposewordscloud.CompareData(local_name2, 'author', datetime.datetime.now())
		request = asposewordscloud.models.requests.PostCompareDocumentRequest(local_name1, compare_data, dest_file_name=dest_name)
		result = self.words_api.post_compare_document(request)
		print("Result {}".format(result))

document = Document()
document.compare_document_with_original_document()