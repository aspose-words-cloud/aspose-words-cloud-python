import os
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
		self.dataFolder = os.path.join(ABSPATH, "TestData/DocumentActions/MailMerge")

	def put_execute_mail_merge_online(self):
		filename = 'SampleMailMergeTemplate.docx'

		filePath = os.path.join(self.dataFolder, filename)
		templateDataFilePath = os.path.join(self.dataFolder, 'SampleMailMergeTemplateData.txt')

		request = asposewordscloud.models.requests.PutExecuteMailMergeOnlineRequest(filePath, templateDataFilePath)
		result = self.words_api.put_execute_mail_merge_online(request)
		print("Result {}".format(result))

document = Document()
document.put_execute_mail_merge_online()