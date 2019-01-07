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

	def post_insert_document_watermark_image(self):
		filename = 'test_multi_pages.docx'
		rotation_angle = 0
		dest_name = 'TestPostInsertDocumentWatermarkImage.docx'
		image = os.path.join(self.dataFolder, 'aspose-cloud.png')

		filePath = os.path.join(self.dataFolder, filename)
		with open(filePath, 'rb') as f:
			fileData = f.read()

		file_upload_response = self.storage_api.put_create(filename, fileData)
		# Check if file uploaded successfully to Cloud Storage
		if(file_upload_response["Code"] == 200 and file_upload_response["Status"] == "OK"):
			request = asposewordscloud.models.requests.PostInsertDocumentWatermarkImageRequest(filename, image, dest_file_name=dest_name, rotation_angle=rotation_angle)
			result = self.words_api.post_insert_document_watermark_image(request)
			print("Result {}".format(result))

table = Table()
table.post_insert_document_watermark_image()
